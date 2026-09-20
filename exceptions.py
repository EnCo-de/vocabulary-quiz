class AppError(Exception):
    """Base exception for application errors."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class NotFoundError(AppError):
    """Requested resource does not exist."""

    pass


class ConflictError(AppError):
    """Request conflicts with existing application state."""

    pass
