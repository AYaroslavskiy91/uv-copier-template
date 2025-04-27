from _typeshed import Incomplete
from logging import DEBUG as logging_DEBUG
from logging import INFO as logging_INFO
from typing import Any, LiteralString, Self

class Future:
    def __init__(
        self, proc, expected_retcode, timeout: Incomplete | None = None
    ) -> None: ...
    def poll(self) -> bool: ...

    ready = poll
    def wait(self) -> None: ...
    @property
    def stdout(self): ...
    @property
    def stderr(self): ...
    @property
    def returncode(self): ...

class ExecutionModifier:
    @classmethod
    def __call__(cls, *args, **kwargs) -> Self: ...

class _BG(ExecutionModifier):
    retcode: Incomplete
    kargs: Incomplete
    timeout: Incomplete
    def __init__(
        self, retcode: int = 0, timeout: Incomplete | None = None, **kargs
    ) -> None: ...
    def __rand__(self, cmd) -> Future: ...

class _FG(ExecutionModifier):
    retcode: Incomplete
    timeout: Incomplete
    def __init__(self, retcode: int = 0, timeout: Incomplete | None = None) -> None: ...
    def __rand__(self, cmd) -> None: ...

class _TEE(ExecutionModifier):
    retcode: Incomplete
    buffered: Incomplete
    timeout: Incomplete
    def __init__(
        self, retcode: int = 0, buffered: bool = True, timeout: Incomplete | None = None
    ) -> None: ...
    def __rand__(self, cmd) -> tuple[Any, LiteralString, LiteralString]: ...

class _TF(ExecutionModifier):
    retcode: Incomplete
    FG: Incomplete
    timeout: Incomplete
    def __init__(
        self, retcode: int = 0, FG: bool = False, timeout: Incomplete | None = None
    ) -> None: ...
    @classmethod
    @classmethod
    def __call__(cls, *args, **kwargs) -> Self: ...
    def __rand__(self, cmd) -> bool: ...

class _RETCODE(ExecutionModifier):
    foreground: Incomplete
    timeout: Incomplete
    def __init__(self, FG: bool = False, timeout: Incomplete | None = None) -> None: ...
    @classmethod
    def __call__(cls, *args, **kwargs) -> Self: ...
    def __rand__(self, cmd): ...

class _NOHUP(ExecutionModifier):
    cwd: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    append: Incomplete
    def __init__(
        self,
        cwd: str = ".",
        stdout: str = "nohup.out",
        stderr: Incomplete | None = None,
        append: bool = True,
    ) -> None: ...
    def __rand__(self, cmd): ...

class LogPipe:
    line_timeout: Incomplete
    kw: Incomplete
    levels: Incomplete
    prefix: Incomplete
    log: Incomplete
    def __init__(self, line_timeout, kw, levels, prefix, log) -> None: ...
    def __rand__(self, cmd): ...

class PipeToLoggerMixin:
    DEFAULT_LINE_TIMEOUT: Incomplete
    DEFAULT_STDOUT: str
    DEFAULT_STDERR: str
    INFO = logging_INFO
    DEBUG = logging_DEBUG
    def pipe(
        self,
        out_level: Incomplete | None = None,
        err_level: Incomplete | None = None,
        prefix: Incomplete | None = None,
        line_timeout: Incomplete | None = None,
        **kw,
    ) -> LogPipe: ...
    def pipe_info(self, prefix: Incomplete | None = None, **kw) -> LogPipe: ...
    def pipe_debug(self, prefix: Incomplete | None = None, **kw) -> LogPipe: ...
    def __rand__(self, cmd): ...

BG = ...
FG = ...
NOHUP = ...
RETCODE = ...
TEE = ...
TF = ...
