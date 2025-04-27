from typing import Literal

from plumbum.commands.base import (
    ERROUT,
    BaseCommand,
    ConcreteCommand,
    shquote,
    shquote_list,
)
from plumbum.commands.modifiers import (
    BG,
    FG,
    NOHUP,
    RETCODE,
    TEE,
    TF,
    ExecutionModifier,
    Future,
)
from plumbum.commands.processes import (
    CommandNotFound,
    ProcessExecutionError,
    ProcessLineTimedOut,
    ProcessTimedOut,
    run_proc,
)

__all__ = (
    "BG",
    "ERROUT",
    "FG",
    "NOHUP",
    "RETCODE",
    "TEE",
    "TF",
    "BaseCommand",
    "CommandNotFound",
    "ConcreteCommand",
    "ExecutionModifier",
    "Future",
    "ProcessExecutionError",
    "ProcessLineTimedOut",
    "ProcessTimedOut",
    "run_proc",
    "shquote",
    "shquote_list",
)

def __dir__() -> (
    tuple[
        Literal["BaseCommand"],
        Literal["ConcreteCommand"],
        Literal["shquote"],
        Literal["shquote_list"],
        Literal["ERROUT"],
        Literal["BG"],
        Literal["FG"],
        Literal["NOHUP"],
        Literal["RETCODE"],
        Literal["TEE"],
        Literal["TF"],
        Literal["ExecutionModifier"],
        Literal["Future"],
        Literal["CommandNotFound"],
        Literal["ProcessExecutionError"],
        Literal["ProcessLineTimedOut"],
        Literal["ProcessTimedOut"],
        Literal["run_proc"],
    ]
): ...
