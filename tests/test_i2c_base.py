from collections import defaultdict
from unittest.mock import patch
from nio.common.signal.base import Signal
from nio.util.support.block_test_case import NIOBlockTestCase
from ..i2c_base import I2CBase, I2CDevice, FT232H_I2CDevice


class TestI2CBase(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    def test_defaults(self):
        blk = I2CBase()
        self.configure_block(blk, {})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, I2CDevice))

    @patch(I2CBase.__module__ + ".FT232H_I2CDevice", spec=FT232H_I2CDevice)
    def test_ft232h(self, mock_ft232h):
        blk = I2CBase()
        self.configure_block(blk, {'platform': 'ft232h'})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, FT232H_I2CDevice))
