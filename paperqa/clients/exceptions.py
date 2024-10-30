from collections.abc import Callable


class DOINotFoundError(Exception):
    def __init__(self, message="DOI not found") -> None:
        self.message = message
        super().__init__(self.message)


def make_flaky_ssl_error_predicate(host: str) -> Callable[[BaseException], bool]:
    return lambda exc: isinstance(exc, ClientConnectorError) and exc.host == host
