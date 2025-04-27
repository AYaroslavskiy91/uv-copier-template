from typing import Any, AnyStr, Protocol, type_check_only

@type_check_only
class PopenLike(Protocol[AnyStr]):
    # Adapted from
    # https://github.com/python/typeshed/blob/281dd351a2f40e6bfb733fd805a58bf8d33ce236/stdlib/subprocess.pyi#L1845
    returncode: int | Any
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None: ...
    # morally the members of the returned tuple should be optional
    # TODO this should allow ReadableBuffer for Popen[bytes], but adding
    # overloads for that runs into a mypy bug (python/mypy#14070).
    def communicate(
        self, input: AnyStr | None = None, timeout: float | None = None
    ) -> tuple[AnyStr, AnyStr]: ...
    def verify(self, retcode, timeout, stdout, stderr) -> None: ...
