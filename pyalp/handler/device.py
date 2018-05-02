from typing import Optional, Union

from pyalp.api.low.alp import API as ALPAPI
from pyalp.api.low.alp import API as MockAPI
from pyalp.api.low.constant import *


class DeviceHandler:

    def __init__(self, serial_number: Optional[int], api: Union[ALPAPI, MockAPI]) -> None:

        self._serial_number = serial_number
        self._api = api

        self._is_allocated = False
        self._id = None

        return

    def allocate(self) -> None:

        if not self._is_allocated:
            if self._serial_number is None:
                self._id = self._api.allocate_device()
            else:
                self._id = self._api.allocate_device(device_number=self._serial_number)
            self._is_allocated = True

        return

    def release(self) -> None:

        if self._is_allocated:
            self._api.halt_device(self._id)
            self._api.free_device(self._id)
            self._is_allocated = False

        return

    def show_info(self) -> None:

        print("Show info...")

        # TODO complete.

        return

    # # TODO add the following method?
    # def display(self, stimulus):
    #
    #     stimulus.display(self)
    #
    #     return

    def display_white_frame(self, duration: float = 1.0) -> None:
        """Display a white frame.

        Argument:
            duration: float
                The duration of the white frame [s].
                The default value is 1.0.
        """

        # Inquire height and width.
        height = self._api.inquire_device(self._id, DEV_DISPLAY_HEIGHT)
        width = self._api.inquire_device(self._id, DEV_DISPLAY_WIDTH)
        print("height, width: {}, {}".format(height, width))
        # Allocate sequence.
        bit_planes = 8
        number_pictures = 100
        sequence_id = self._api.allocate_sequence(self._id, bit_planes, number_pictures)
        print("sequence_id: {}".format(sequence_id))
        # Put sequence.
        import numpy as np
        picture_offset = 0
        data = 255 * np.ones(number_pictures * height * width, dtype=np.uint8)
        self._api.put_sequence(self._id, sequence_id, picture_offset, number_pictures, data)
        print("put sequence")
        # Start sequence.
        self._api.start_projection(self._id, sequence_id)
        print("start projection")
        # Wait end of projection
        self._api.wait_projection(self._id)
        print("end projection")
        # Free sequence.
        self._api.free_sequence(self._id, sequence_id)
        print("free sequence")

        return

    def display_rectangle(self) -> None:

        print("Display rectangle...")

        # TODO inquire height and width.
        height = self._api.inquire_device(self._id, DEV_DISPLAY_HEIGHT)
        width = self._api.inquire_device(self._id, DEV_DISPLAY_WIDTH)
        print("height, width: {}, {}".format(height, width))
        # TODO allocate sequence.
        bit_planes = 8
        number_pictures = 100
        sequence_id = self._api.allocate_sequence(self._id, bit_planes, number_pictures)
        print("sequence_id: {}".format(sequence_id))
        # TODO put sequence.
        import numpy as np
        picture_offset = 0
        shape = (number_pictures, height, width)
        data = np.zeros(shape, dtype=np.uint8)
        i_min = (1 * width) // 4
        i_max = (3 * width) // 4
        j_min = (1 * height) // 4
        j_max = (3 * width) // 4
        data[:, j_min:j_max, i_min:i_max] = np.iinfo(np.uint8).max
        data = data.flatten()
        self._api.put_sequence(self._id, sequence_id, picture_offset, number_pictures, data)
        print("put sequence")
        # TODO start sequence.
        self._api.start_projection(self._id, sequence_id)
        print("start projection")
        # TODO wait end of projection
        self._api.wait_projection(self._id)
        print("end projection")
        # TODO free sequence.
        self._api.free_sequence(self._id, sequence_id)
        print("free sequence")

        return

    def display_checkerboard(self) -> None:

        print("Display checkerboard...")

        # TODO complete.

        return

    def display_film(self) -> None:

        print("Display film...")

        # TODO complete.

        return
