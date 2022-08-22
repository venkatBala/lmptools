from abc import ABC, abstractmethod

from ..core.simulation import DumpSnapshot
from ..dump import DumpCallback


class SnapshotWriter(ABC, DumpCallback):
    """Abstract base class for implementing a snapshot writer"""

    @abstractmethod
    def on_snapshot_parse_end(self, snapshot: DumpSnapshot, *args, **kwargs):
        pass