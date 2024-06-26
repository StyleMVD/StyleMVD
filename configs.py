import configargparse

def parse_config():
    parser = configargparse.ArgumentParser(
                        prog='StyleMVD',
                        description='Generate texture given mesh and style image')
    # File Config
    parser.add_argument('--config', type=str, required=True, is_config_file=True)
    parser.add_argument('--style_img', type=str, required=True)
    parser.add_argument('--mesh', type=str, required=True)
    parser.add_argument('--mesh_config_relative', action='store_true', help="Search mesh file relative to the config path instead of current working directory")
    parser.add_argument('--output', type=str, default="exp_results", help="If not provided, use the parent directory of config file for output")
    parser.add_argument('--prefix', type=str, default='StyleMVD')
    parser.add_argument('--use_mesh_name', action='store_true')
    parser.add_argument('--timeformat', type=str, default='%d%b%Y-%H%M%S', help='Setting to None will not use time string in output directory')
    # Diffusion Config
    parser.add_argument('--prompt', type=str, required=True)
    parser.add_argument('--negative_prompt', type=str, default='text, watermark, lowres, low quality, worst quality, deformed, glitch, low contrast, noisy, saturation, blurry')
    parser.add_argument('--num_inference_steps', type=int, default=20)
    parser.add_argument('--ip_adapter_scale', type=float, default=1.0, help='IP Adapter scale factor (lambda_{img})')
    parser.add_argument('--guidance_scale', type=float, default=5.0, help='Recommend above 12 to avoid blurriness')
    parser.add_argument('--seed', type=int, default=0)
    # ControlNet Config
    parser.add_argument('--cond_type', type=str, default='canny', help='Support canny and depth')
    parser.add_argument('--guess_mode', action='store_true')
    parser.add_argument('--conditioning_scale', type=float, default=0.5)
    parser.add_argument('--conditioning_scale_end', type=float, default=0.9, help='Gradually increasing conditioning scale for better geometry alignment near the end')
    parser.add_argument('--control_guidance_start', type=float, default=0.0)
    parser.add_argument('--control_guidance_end', type=float, default=0.99)
    parser.add_argument('--guidance_rescale', type=float, default=0.0, help='Not tested')
    # Multi-View Config
    parser.add_argument('--latent_view_size', type=int, default=96, help='Larger resolution, less aliasing in latent images; quality may degrade if much larger trained resolution of networks')
    parser.add_argument('--latent_tex_size', type=int, default=1536, help='Originally 1536 in paper, use lower resolution save VRAM')
    parser.add_argument('--rgb_view_size', type=int, default=1024)
    parser.add_argument('--rgb_tex_size', type=int, default=1024)
    parser.add_argument('--camera_azims', type=int, nargs="*", default=[-180, -135, -90, -45, 0, 45, 90, 135], help='Place the cameras at the listed azim angles')
    parser.add_argument('--no_top_cameras', action='store_true', help='Two cameras added to paint the top surface')
    parser.add_argument('--mvd_end', type=float, default=0.0, help='Time step to stop texture space aggregation')
    parser.add_argument('--ref_attention_end', type=float, default=0.2, help='Lower->better quality; higher->better harmonization (t_{ref})')
    parser.add_argument('--shuffle_bg_change', type=float, default=0.4, help='Use only black and white background after certain timestep')
    parser.add_argument('--shuffle_bg_end', type=float, default=0.8, help='Don\'t shuffle background after certain timestep. background color may bleed onto object')
    parser.add_argument('--mesh_scale', type=float, default=1.0, help='Set above 1 to enlarge object in camera views')
    parser.add_argument('--mesh_autouv', action='store_true', help='Use Xatlas to unwrap UV automatically')
    # Logging Config
    parser.add_argument('--log_interval', type=int, default=10)
    parser.add_argument('--view_fast_preview', action='store_true', help='Use color transformation matrix instead of decoder to log view images')
    parser.add_argument('--tex_fast_preview', action='store_true', help='Use color transformation matrix instead of decoder to log texture images')
    
    options = parser.parse_args()

    return options
