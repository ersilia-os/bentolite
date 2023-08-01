from werkzeug.utils import cached_property
from .gcs import is_gcs_url
from .s3 import is_s3_url


__all__ = ["cached_property"]
