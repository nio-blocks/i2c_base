from enum import Enum
import logging
from nio.common.block.base import Block
from nio.metadata.properties import SelectProperty, StringProperty


class I2CDevice():

    def __init__(self, address):
        self._address = address

    def write_list(self, register, data):
        """ Write a list of bytes """
        raise NotImplemented()

    def read_bytes(self, length):
        """ Read a length number of bytes (without register). Results are
        returned as a bytearray """
        raise NotImplemented()


class FT232H_I2CDevice(I2CDevice):

    def __init__(self, address):
        super().__init__(address)
        import Adafruit_GPIO.FT232H as FT232H
        # Temporarily disable FTDI serial drivers.
        FT232H.use_FT232H()
        # Find the first FT232H device.
        ft232h = FT232H.FT232H()
        # Get the I2C device for the configured address
        self._device = FT232H.I2CDevice(ft232h, address)

    def write_list(self, register, data):
        return self._device.writeList(register, data)

    def read_bytes(self, length):
        return self._device.readBytes(length)


class Platform(Enum):
    raspberry_pi = 0
    ft232h = 1


class I2CBase(Block):

    """ Communicate I2C using the selected Platform """

    platform = SelectProperty(Platform,
                              title='Platform',
                              default=Platform.raspberry_pi)
    address = StringProperty(title='I2C Address', default="0x00")

    def __init__(self):
        super().__init__()
        self._i2c = None

    def configure(self, context):
        super().configure(context)
        address = int(self.address, 0)
        self._logger.debug(
            "Creating device adaptor: {}, address: {}".format(
                self.platform.name, address))
        if self.platform.value == Platform.raspberry_pi.value:
            self._i2c = I2CDevice(address) # TODO: make a raspi device
        elif self.platform.value == Platform.ft232h.value:
            logging.getLogger('Adafruit_GPIO.FT232H').setLevel(
                self._logger.logger.level)
            self._i2c = FT232H_I2CDevice(address)
        else:
            self._logger.warning("Warning! Unknown device adaptor type.")
            self._i2c = I2CDevice(address)
        self._logger.debug("Created device adaptor")
