import subprocess
import sys

sys.path.append(".")

import os

import proto_files

COMMAND = "venv/bin/python -m grpc_tools.protoc -I ../protobufs --python_out=./proto/ --grpc_python_out=./proto/ ../protobufs/{file_name}"


# TODO: This should be done in a safer way
REMOVE_PROTOS_COMMAND = "rm ./proto/*pb2*"

try:
    subprocess.run([REMOVE_PROTOS_COMMAND], check=True)
except (subprocess.CalledProcessError, FileNotFoundError):
    pass

for proto_file in proto_files.PROTO_FILES:
    os.system(COMMAND.format(file_name=proto_file))
