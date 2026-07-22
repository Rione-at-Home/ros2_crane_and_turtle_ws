
#!/usr/bin/env python3

from dynamixel_sdk import *
import time

PORT = "/dev/ttyUSB1"
BAUDRATE = 1000000
PROTOCOL_VERSION = 1.0

ADDR_PRESENT_POSITION = 36

port = PortHandler(PORT)
packet = PacketHandler(PROTOCOL_VERSION)

port.openPort()
port.setBaudRate(BAUDRATE)

while True:
    print("----------------")

    for dxl_id in range(1, 6):
        pos, result, error = packet.read2ByteTxRx(
            port,
            dxl_id,
            ADDR_PRESENT_POSITION
        )

        print(f"Servo {dxl_id}: {pos}")

    time.sleep(0.2)