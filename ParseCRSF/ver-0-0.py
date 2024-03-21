import serial

# Настройки подключения к приёмнику
SERIAL_PORT = '/dev/usbserial-1110'
BAUD_RATE = 420000  # Стандартная скорость при включении

# Параметры пакета данных
CRSF_SYNC = 0xC8
CRSF_SYNC_EDGETX = 0xEE

# Функция для проверки, является ли байт началом пакета
def isPacketStart(byte):
    return byte in [CRSF_SYNC, CRSF_SYNC_EDGETX]
# Основная функция
def main():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
        print("Starting CRSF packet reader...")
        read_crsf_serial(ser)

# Функция для чтения данных из серийного порта
def read_crsf_serial(ser):
    print("Start reading")
    packet_count = 0
    while packet_count < 5:
        # Читаем один байт
        byte = ser.read(1)
        if byte:
            # Проверяем, является ли этот байт началом пакета
            if isPacketStart(ord(byte)):
                print("Found packet start with byte:", byte.hex())
                packet_count += 1
        else:
            print("No data received. Waiting...")
    print("Finished reading 5 packets.")

if __name__ == "__main__":
    main()