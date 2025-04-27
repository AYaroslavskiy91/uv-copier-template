import sys
from typing import Literal

import plumbum.path
from plumbum.commands import (
    BG,
    ERROUT,
    FG,
    NOHUP,
    RETCODE,
    TEE,
    TF,
    CommandNotFound,
    ProcessExecutionError,
    ProcessLineTimedOut,
    ProcessTimedOut,
)
from plumbum.machines import BaseRemoteMachine, PuttyMachine, SshMachine, local
from plumbum.path import LocalPath, Path, RemotePath
from plumbum.version import version

from . import cmd

__author__ = ...
__version__ = ...
__all__ = (
    "BG",
    "ERROUT",
    "FG",
    "NOHUP",
    "RETCODE",
    "TEE",
    "TF",
    "BaseRemoteMachine",
    "CommandNotFound",
    "LocalPath",
    "Path",
    "ProcessExecutionError",
    "ProcessLineTimedOut",
    "ProcessTimedOut",
    "PuttyMachine",
    "RemotePath",
    "SshMachine",
    "__author__",
    "__version__",
    "cmd",
    "local",
)

def __dir__() -> (
    tuple[
        Literal["BG"],
        Literal["ERROUT"],
        Literal["FG"],
        Literal["NOHUP"],
        Literal["RETCODE"],
        Literal["TEE"],
        Literal["TF"],
        Literal["CommandNotFound"],
        Literal["ProcessExecutionError"],
        Literal["ProcessLineTimedOut"],
        Literal["ProcessTimedOut"],
        Literal["BaseRemoteMachine"],
        Literal["PuttyMachine"],
        Literal["SshMachine"],
        Literal["local"],
        Literal["LocalPath"],
        Literal["Path"],
        Literal["RemotePath"],
        Literal["__author__"],
        Literal["__version__"],
        Literal["cmd"],
    ]
): ...
