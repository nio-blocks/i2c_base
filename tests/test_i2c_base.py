from collections import defaultdict
from unittest.mock import patch
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..i2c_base import I2CBase, I2CDevice, FT232H_I2CDevice


class TestI2CBase(NIOBlockTestCase):

    def test_defaults(self):
        blk = I2CBase()
        self.configure_block(blk, {})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, I2CDevice))

    @patch(I2CBase.__module__ + ".I2CDevice", spec=I2CDevice)
    def test_address(self, mock_i2c):
        blk = I2CBase()
        self.configure_block(blk, {'address': 0x11})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, I2CDevice))
        mock_i2c.assert_called_once_with(0x11)

    @patch(I2CBase.__module__ + ".FT232H_I2CDevice", spec=FT232H_I2CDevice)
    def test_ft232h(self, mock_i2c):
        blk = I2CBase()
        self.configure_block(blk, {'platform': 'ft232h'})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, FT232H_I2CDevice))
        mock_i2c.assert_called_once_with(0x00)
