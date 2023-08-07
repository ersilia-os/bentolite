
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os
import sys
import tarfile
import logging
import tempfile
import shutil
from functools import wraps
from contextlib import contextmanager
from urllib.parse import urlparse
from pathlib import PureWindowsPath, PurePosixPath

from ..utils.s3 import is_s3_url
from ..utils.gcs import is_gcs_url

logger = logging.getLogger(__name__)

def _is_http_url(bundle_path):
    try:
        return urlparse(bundle_path).scheme in ["http", "https"]
    except ValueError:
        return False


def _is_remote_path(bundle_path):
    return isinstance(bundle_path, str) and (
        is_s3_url(bundle_path) or is_gcs_url(bundle_path) or _is_http_url(bundle_path)
    )