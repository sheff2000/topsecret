import serial
import time

# Настройки подключения к приёмнику
SERIAL_PORT = '/dev/cu.usbserial-1110'
BAUD_RATE = 420000  # Стандартная скорость при включении

# Параметры пакета данных
CRSF_SYNC = 0xC8
CRSF_SYNC_EDGETX = 0xEE

# Основная функция
def main():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
        print("Starting CRSF packet reader...")
        read_crsf_serial(ser)

# Функция для чтения данных из серийного порта
def read_crsf_serial(ser):
    print("Start reading")
    packet_count = 0
    while packet_count < 5000:
        # Читаем один байт
        start_byte = ser.read(1)
        if start_byte == bytes([CRSF_SYNC]):
            print("FIND START PACKET")
            len_byte = ser.read(1)
            type_byte = ser.read(1)
            if int.from_bytes(type_byte, byteorder='big') in [0x08, 0x07, 0x09, 0x0B, 0x14, 0x16]:
                print(f"---------FOUND --------{type_byte}-------")
                fff = input("dfdfdf")
            # Преобразование байтов в десятичные значения для вывода
            #len_value = int.from_bytes(len_byte, byteorder='big')
            #type_value = int.from_bytes(type_byte, byteorder='big')
            print(f"Start - {start_byte.hex()}  Len - {len_byte.hex()}  Type - {type_byte.hex()}")
            packet_count += 1
    print("Finished reading 5 packets.")

if __name__ == "__main__":
    main()
