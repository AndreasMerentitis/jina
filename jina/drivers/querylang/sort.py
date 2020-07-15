__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from typing import Iterable

from .. import BaseRecursiveDriver
from ...helper import rgetattr


class SortQL(BaseRecursiveDriver):
    """Restrict the size of the ``topk_results`` to ``k`` (given by the request)

    This driver works on both chunk and doc level
    """

    def __init__(self, field: str, reverse: bool = False, *args, **kwargs):
        """

        :param reverse: sort the value from big to small
        """

        super().__init__(*args, **kwargs)
        self.reverse = reverse
        self.field = field

    def apply_all(self, docs: Iterable['jina_pb2.Document'], *args, **kwargs):
        docs.sort(keys=lambda x: rgetattr(x, self.field), reverse=self.reverse)


class SortResultQL(SortQL):
    """Sort the ``topk_results``

    This driver works on both chunk and doc level
    """

    def apply(self, doc: 'jina_pb2.Document', *args, **kwargs):
        doc.topk_results.sort(key=lambda x: rgetattr(x, self.field), reverse=self.reverse)