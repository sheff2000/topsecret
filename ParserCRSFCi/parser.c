#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <termios.h>

#define SERIAL_PORT1 "/dev/cu.usbserial-1140"
#define SERIAL_PORT2 "/dev/cu.usbserial-1110"
#define BAUD_RATE B9600

int open_serial_port(const char* serial_port) {
    int fd = open(serial_port, O_RDWR | O_NOCTTY | O_SYNC);
    if (fd < 0) {
        printf("%s - Device disconnected or unavailable.\n", serial_port);
        return -1;
    }
    // Настройка порта (опущено для краткости)
    return fd;
}

void close_serial_port(int fd) {
    close(fd);
}

/*void read_and_process(int serial_fd, const char* device_name) {
    unsigned char buf[64];
    int n = read(serial_fd, buf, sizeof(buf));
    if (n > 0) {
        printf("%s - LQ = %d\n", device_name, n); // Пример вывода
    }
}*/
void read_and_process(int* serial_fd, const char* device_name) {
    unsigned char buf[64];
    int n;
    unsigned char start_byte;
    unsigned char packet_type;
    unsigned char len_packet;

    while (1) {
        // Чтение одного байта (ожидание начала пакета)
        n = read(*serial_fd, &start_byte, 1);
        if (n > 0 && start_byte == 0xC8) { // Начало пакета найдено
            // Чтение длины пакета
            n = read(*serial_fd, &len_packet, 1);
            if (n > 0) {
                // Чтение типа пакета
                n = read(*serial_fd, &packet_type, 1);
                if (n > 0 && packet_type == 0x14) { // Если тип пакета - Link statistics
                    // Читаем оставшуюся часть пакета в зависимости от длины
                    n = read(*serial_fd, buf, len_packet-1); // len_packet-1 потому что тип пакета уже прочитан
                    if (n > 0) {
                        // Декодируем Link quality
                        unsigned char uplink_lq = buf[2]; // Индекс 2, потому что начинаем с 0, и у нас уже есть RSSI Ant. 1 и 2
                        printf("%s - LQ = %d%%\n", device_name, uplink_lq);
                    }
                }
            }
        }
    }
}

int check_device_connection(int* serial_fd, const char* serial_port) {
    if (*serial_fd < 0) {
        *serial_fd = open_serial_port(serial_port);
        if (*serial_fd >= 0) {
            printf("%s - Device connected.\n", serial_port);
            return 1; // Устройство подключено
        }
    }
    return 0; // Устройство не подключено
}


int main() {
    int serial_fd1 = -1, serial_fd2 = -1;

    while (1) {
        check_device_connection(&serial_fd1, SERIAL_PORT1);
        check_device_connection(&serial_fd2, SERIAL_PORT2);

        if (serial_fd1 >= 0) {
            read_and_process(&serial_fd1, SERIAL_PORT1);
        }

        if (serial_fd2 >= 0) {
            read_and_process(&serial_fd2, SERIAL_PORT2);
        }

        sleep(1); // Уменьшение загрузки процессора
    }

    // Закрытие портов при выходе из программы (по факту, до сюда не дойдем из-за бесконечного цикла)
    if (serial_fd1 >= 0) close_serial_port(serial_fd1);
    if (serial_fd2 >= 0) close_serial_port(serial_fd2);
    return 0;
}