from _typeshed import Incomplete

from plumbum.commands.processes import CommandNotFound as CommandNotFound
from plumbum.commands.processes import ProcessExecutionError as ProcessExecutionError
from plumbum.commands.processes import ProcessTimedOut as ProcessTimedOut

class PopenAddons:
    def verify(self, retcode, timeout, stdout, stderr) -> None: ...

class BaseMachine:
    def get(self, cmd, *othercommands): ...
    def __contains__(self, cmd) -> bool: ...
    @property
    def encoding(self): ...
    custom_encoding: Incomplete

    # This raises mypy's hackles:
    #   1. "Name \"encoding\" already defined on line 18"
    #   2. "\"Callable[[BaseMachine], Any]\" has no attribute \"setter\""
    # @encoding.setter
    # def encoding(self, value) -> None: ...  # noqa: ERA001

    # Mypy complaint:
    #   Return type "Popen[Any]" of "daemonic_popen" incompatible with return type
    #     "Never" in supertype "BaseMachine"
    # def daemonic_popen(
    #     self,
    #     command,
    #     cwd: str = "/",  # noqa: ERA001
    #     stdout: Incomplete | None = None,  # noqa: ERA001
    #     stderr: Incomplete | None = None,  # noqa: ERA001
    #     append: bool = True,  # noqa: ERA001
    # ) -> Never: ...

    class Cmd:
        def __init__(self, machine) -> None: ...
        def __getattr__(self, name): ...

    @property
    def cmd(self) -> Cmd: ...
    def clear_program_cache(self) -> None: ...
