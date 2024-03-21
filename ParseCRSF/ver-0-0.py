import serial
import time

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

# Функция для безопасного чтения данных из серийного порта
def safe_read(ser, length):
    buffer = bytearray()
    timeout_start = time.time()
    timeout = 2  # Таймаут в секундах для чтения всего пакета
    while len(buffer) < length:
        time_left = timeout - (time.time() - timeout_start)
        if time_left <= 0:
            # Если вышло время ожидания
            print("Timeout reached. Incomplete packet.")
            return None
        ser.timeout = time_left  # Устанавливаем таймаут для чтения
        buffer += ser.read(length - len(buffer))
    return buffer

# Функция для чтения данных из серийного порта
def read_crsf_serial(ser):
    print("Start reading")
    packet_count = 0
    while packet_count < 5:
        # Читаем один байт
        start_byte = ser.read(1)
        if start_byte:
            # Проверяем, является ли этот байт началом пакета
            if isPacketStart(ord(start_byte)):
                print("Found packet start with byte:", start_byte.hex())

                # Нашли начало пакета данных
                len_byte = safe_read(ser, 1)  # Безопасное чтение длины пакета
                if len_byte is None:
                    continue  # Пропускаем этот пакет, если не удалось прочитать длину

                packet_length = ord(len_byte)
                print(f"LEN Packet = {packet_length}")

                # Читаем оставшуюся часть пакета
                remaining_packet = safe_read(ser, packet_length)
                if remaining_packet is None:
                    continue  # Пропускаем, если не удалось прочитать весь пакет

                print(f"Remaining Packet Data: {remaining_packet.hex()}")
                packet_count += 1
        else:
            print("No data received. Waiting...")
    print("Finished reading 5 packets.")

if __name__ == "__main__":
    main()