import itertools
from typing import Iterable, Iterator, Sequence, Tuple

from ..types import (
    ApiFuncReturnValue,
    HTTPResponse,
    InferenceResult,
    InferenceTask,
    Output,
)


def regroup_return_value(
    return_values: Iterable, tasks: Sequence[InferenceTask]
) -> Iterator[Tuple[Output, InferenceTask]]:
    iter_rv = iter(return_values)
    try:
        for task in tasks:
            if task.batch is None:
                yield next(iter_rv), task
            else:
                yield tuple(itertools.islice(iter_rv, task.batch)), task
    except StopIteration:
        for task in tasks:
            task.discard(
                http_status=500,
                err_msg="The return values of Api Function doesn't match tasks",
            )


class BaseOutputAdapter:
    """
    OutputAdapter is an layer between result of user defined API callback function
    and final output in a variety of different forms,
    such as HTTP response, command line stdout.
    """

    def __init__(self, cors='*'):
        self.cors = cors

    @property
    def config(self):
        return dict(cors=self.cors,)

    @property
    def pip_dependencies(self):
        """
        :return: List of PyPI package names required by this OutputAdapter
        """
        return []

    def pack_user_func_return_value(
        self, return_result: ApiFuncReturnValue, tasks: Sequence[InferenceTask],
    ) -> Sequence[InferenceResult]:
        """
        Pack the return value of user defined API function into InferenceResults
        """
        raise NotImplementedError()

    def to_http_response(self, result: InferenceResult) -> HTTPResponse:
        """
        Converts InferenceResults into HTTP responses.
        """
        raise NotImplementedError()

    def to_cli(self, results: Iterable[InferenceResult]) -> int:
        """
        Converts InferenceResults into CLI output.
        """
        raise NotImplementedError()