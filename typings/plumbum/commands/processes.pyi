import math
from _typeshed import Incomplete
from collections.abc import Collection, Generator
from queue import Queue
from typing import Literal

from plumbum._typing import PopenLike

_iter_lines = ...

class ProcessExecutionError(OSError):
    message: Incomplete
    host: Incomplete
    argv: Incomplete
    retcode: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    def __init__(
        self,
        argv,
        retcode,
        stdout,
        stderr,
        message: Incomplete | None = None,
        *,
        host: Incomplete | None = None,
    ) -> None: ...

class ProcessTimedOut(Exception):
    argv: Incomplete
    def __init__(self, msg, argv) -> None: ...

class ProcessLineTimedOut(Exception):
    argv: Incomplete
    machine: Incomplete
    def __init__(self, msg, argv, machine) -> None: ...

class CommandNotFound(AttributeError):
    program: Incomplete
    path: Incomplete
    def __init__(self, program, path) -> None: ...

class MinHeap:
    def __init__(self, items=()) -> None: ...
    def __len__(self) -> int: ...
    def push(self, item) -> None: ...
    def pop(self) -> None: ...
    def peek(self): ...

_timeout_queue: Queue
_shutting_down: bool
bgthd: Incomplete

def run_proc(
    proc: PopenLike, retcode: int | Collection | None, timeout: float | None = None
) -> tuple[
    Incomplete, str | Incomplete | Literal[b""], str | Incomplete | Literal[b""]
]: ...

BY_POSITION: Incomplete
BY_TYPE: Incomplete
DEFAULT_ITER_LINES_MODE = BY_POSITION
DEFAULT_BUFFER_SIZE: float = math.inf

def iter_lines(
    proc,
    retcode: int | Collection | None = 0,
    timeout: Incomplete | None = None,
    linesize: int = -1,
    line_timeout: Incomplete | None = None,
    buffer_size: float | None = None,
    mode: Incomplete | None = None,
    _iter_lines=...,
) -> Generator[
    tuple[Incomplete | None, ...] | tuple[int, Incomplete], Incomplete, Incomplete
]: ...
