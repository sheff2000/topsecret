import serial
import time

CRSF_SYNC = 0xC8 # начало пакета
# Для пакетов, отправляемых EdgeTX, использующих каналы/телеметрию, используется 0xEE
CRSF_SYNC_EDGETX = 0xEE


# Константы типов пакетов CRSF
CRSF_FRAMETYPE_GPS = 0x02
CRSF_FRAMETYPE_BATTERY_SENSOR = 0x08


# Настройки серийного порта
SERIAL_PORT = '/dev/usbserial-1110'
BAUD_RATE = 115200

# Функция для проверки SYNC байта
def is_sync_byte(byte):
    return byte in [bytes([CRSF_SYNC]), bytes([CRSF_SYNC_EDGETX])]

# Генерация таблицы CRC8
def generate_crc8_table(poly=0xD5):
    crc8_table = []
    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ poly
            else:
                crc = crc << 1
        crc8_table.append(crc & 0xFF)
    return crc8_table

# Вычисление CRC8
crc8_table = generate_crc8_table()
def crc8_data(data):
    crc = 0
    for byte in data:
        crc = crc8_table[crc ^ byte]
    return crc
def parse_crsf_packet(packet_type, payload):
    """Распарсивает и выводит информацию из пакета CRSF в зависимости от его типа."""
    if packet_type == CRSF_FRAMETYPE_GPS:
        # Разбор и вывод данных GPS
        # Добавьте здесь логику для распарсивания данных GPS...
        print("GPS Data:", payload)
    elif packet_type == CRSF_FRAMETYPE_BATTERY_SENSOR:
        # Разбор и вывод информации о батарее
        # Добавьте здесь логику для распарсивания данных батареи...
        print("Battery Data:", payload)
    elif packet_type == CRSF_FRAMETYPE_LINK_STATISTICS:
        rssi = payload[0]  # Примерный псевдокод, нужно адаптировать под реальную структуру данных
        lq = payload[1]
        print(f"RSSI: {rssi}, LQ: {lq}")
    elif packet_type == CRSF_FRAMETYPE_RC_CHANNELS_PACKED:
        # Декодирование значений каналов
        channels = payload  # Преобразуйте данные каналов из payload в удобный формат
        print(f"Channels: {channels}")
    else:
        print(f"Unknown packet type: {packet_type}, payload: {payload}")

#def read_crsf_serial(ser):
#    while True:
#        if ser.in_waiting > 0:
#            sync_byte = ser.read(1)
#            if is_sync_byte(sync_byte):
#                length_type = ser.read(2)
#                length = length_type[0] - 1
#                packet_type = length_type[1]
#                payload_crc = ser.read(length + 1)  # Чтение полезной нагрузки и CRC
#               payload, crc = payload_crc[:-1], payload_crc[-1]
#                if crc8_data(length_type + payload) == crc:  # Примерная проверка CRC
#                    parse_crsf_packet(packet_type, payload)
#                else:
#                    print("CRC error")
def read_crsf_serial(ser):
    buffer = bytearray()
    while True:
        if ser.in_waiting > 0:
            buffer += ser.read(ser.in_waiting)
            while len(buffer) > 4:  # Минимальная длина CRSF пакета
                if buffer[0] in [CRSF_SYNC, CRSF_SYNC_EDGETX]:
                    length = buffer[1]
                    if len(buffer) >= length + 2:
                        packet = buffer[:length+2]
                        buffer = buffer[length+2:]
                        if crc8_data(packet[:-1]) == packet[-1]:
                            parse_crsf_packet(packet[2], packet[3:-1])
                        else:
                            print("CRC error")
                    else:
                        break
                else:
                    buffer.pop(0)

def main():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
        print("Starting CRSF packet reader...")
        read_crsf_serial(ser)

if __name__ == "__main__":
    main()
