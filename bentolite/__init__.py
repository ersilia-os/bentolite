__version__ = "0.0.0"

from .service import (
    BentoService,
    api_decorator as api,
    artifacts_decorator as artifacts,
)

__all__ = ["__version__", "api", "BentoService", "artifacts"]
