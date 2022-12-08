import subprocess

def lambda_handler(event, context):
    command = event['command']
    out = subprocess.check_output(
        command,
        shell=True,
        stderr=subprocess.STDOUT
        ).decode().rstrip()

    return {
        'file_size': out
    }
