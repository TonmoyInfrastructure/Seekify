import os
import shlex
import subprocess


SUBP_ENV = {
    "PATH": os.environ["PATH"],
    "LC_ALL": "C",
    "LANGUAGE": "",
}


def execute_subpro(args, **kwargs):
    if not isinstance(args, (list, tuple)):
        args = shlex.split(args)
    kwargs["env"] = kwargs.get("env", SUBP_ENV)
    kwargs["encoding"] = kwargs.get("encoding", "UTF-8")
    kwargs["stdout"] = subprocess.PIPE
    # kwargs["stderr"] = subprocess.STDOUT
    kwargs["stderr"] = subprocess.PIPE
