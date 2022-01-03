#
import unittest
from datasets.stcar_ds import StcarDs

class TStcarDs(unittest.TestCase):
    # python -m unittest -v utc.datasets.t_stcar_ds.TStcarDs.test_draw_bbox
    def test_draw_bbox(self):
        ds = StcarDs()
        ds.draw_bbox()