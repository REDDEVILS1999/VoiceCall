import argparse
from config_store import update_config, get_config

parser = argparse.ArgumentParser(description="Update CAPTCHA config")

parser.add_argument("--length", type=int, required=True, help="CAPTCHA length")
parser.add_argument("--retry", type=int, required=True, help="Retry attempts")
parser.add_argument("--prompt", type=str, required=True, help="Path to prompt WAV file")

args = parser.parse_args()

update_config(args.length, args.retry, args.prompt)

print(" Configuration updated successfully!")
print("New Config:", get_config())

