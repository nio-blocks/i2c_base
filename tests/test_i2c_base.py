from collections import defaultdict
from unittest.mock import patch
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..i2c_base import I2CBase, I2CDevice, FT232H_I2CDevice, \
    RaspberryPi_I2CDevice


class TestI2CBase(NIOBlockTestCase):

    @patch(I2CBase.__module__ + ".RaspberryPi_I2CDevice", spec=I2CDevice)
    def test_defaults(self, mock_i2c):
        """Test default configuration is used with i2c device."""
        blk = I2CBase()
        self.configure_block(blk, {})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, I2CDevice))

    @patch(I2CBase.__module__ + ".RaspberryPi_I2CDevice", spec=I2CDevice)
    def test_address(self, mock_i2c):
        """Test that address is configurable and passed to i2c device."""
        blk = I2CBase()
        self.configure_block(blk, {'address': 0x11})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, I2CDevice))
        mock_i2c.assert_called_once_with(0x11)

    @patch(I2CBase.__module__ + ".RaspberryPi_I2CDevice",
           spec=RaspberryPi_I2CDevice)
    def test_raspberry_pi(self, mock_i2c):
        """Test that a Raspberry Pi can be used as i2c adaptor."""
        blk = I2CBase()
        self.configure_block(blk, {'platform': 'raspberry_pi'})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, RaspberryPi_I2CDevice))
        mock_i2c.assert_called_once_with(0x00)

    @patch(I2CBase.__module__ + ".FT232H_I2CDevice", spec=FT232H_I2CDevice)
    def test_ft232h(self, mock_i2c):
        """Test that FT232h chip can be used as i2c adaptor."""
        blk = I2CBase()
        self.configure_block(blk, {'platform': 'ft232h'})
        self.assertTrue(blk._i2c)
        self.assertTrue(isinstance(blk._i2c, FT232H_I2CDevice))
        mock_i2c.assert_called_once_with(0x00)
