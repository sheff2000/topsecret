# определеяем статический класс с функциями для обработки каждого типа пакетов
class PacketHandlers:
    @staticmethod
    def handle_gps_packet(packet):
        print("Обработка пакета GPS")

    @staticmethod
    def handle_battery_packet(packet):
        print("Обработка пакета информации о батарее")

    @staticmethod
    def handle_vario_packet(packet):
        print("пакет -  Vertical speed ")

    @staticmethod
    def handle_baroattitude_packet(packet):
        print("пакет -  Barometric altitude, vertical speed (optional) ")
    @staticmethod
    def handle_heartbeat_packet(packet):
        print("пакет -  (CRSFv3) Heartbeat ")

    @staticmethod
    def handle_linkstatistics_packet(packet):
        #print("пакет -  Signal information. Uplink/Downlink RSSI, SNR, Link Quality (LQ), RF mode, transmit power ")
        uplink_rssi_ant1 = packet[1] * -1
        uplink_rssi_ant2 = packet[2] * -1
        uplink_lq = packet[3]
        uplink_snr = int.from_bytes(packet[4:5], byteorder='little', signed=True)
        active_antenna = packet[5]
        rf_mode = packet[6]
        uplink_tx_power = packet[7]
        downlink_rssi = packet[8] * -1
        downlink_lq = packet[9]
        downlink_snr = int.from_bytes(packet[10:11], byteorder='little', signed=True)

        #print(f"Uplink RSSI Ant. 1: {uplink_rssi_ant1} dBm")
        #print(f"Uplink RSSI Ant. 2: {uplink_rssi_ant2} dBm")
        print(f"Uplink LQ: {uplink_lq}% -- RF Mode - {rf_mode} -- Uplink RSSI Ant. 1 - {uplink_rssi_ant1} -- Uplink RSSI Ant. 2 - {uplink_rssi_ant2}")
        #print(f"Uplink SNR: {uplink_snr} dB")
        #print(f"Diversity Active Antenna: {active_antenna} (0=Ant. 1, 1=Ant. 2)")
        #print(f"RF Mode: {rf_mode}")
        #print(f"Uplink TX Power: {uplink_tx_power}")
        #print(f"Downlink RSSI: {downlink_rssi} dBm")
        #print(f"Downlink LQ: {downlink_lq}%")
        #print(f"Downlink SNR: {downlink_snr} dB")

    @staticmethod
    def handle_rcchannelspacked_packet(packet):
        print("пакет -  Channels data (both handset to TX and RX to flight controller)")

    @staticmethod
    def handle_subsetrcchannelspacked_packet(packet):
        print("пакет -  (CRSFv3) Channels subset data")

    @staticmethod
    def handle_linkrxid_packet(packet):
        print("пакет -  Receiver RSSI percent, power?")

    @staticmethod
    def handle_linktxid_packet(packet):
        print("пакет -  Transmitter RSSI percent, power, fps?")

    @staticmethod
    def handle_attitude_packet(packet):
        print("пакет -  Attitude: pitch, roll, yaw")

    @staticmethod
    def handle_flightmode_packet(packet):
        print("пакет -  Flight controller flight mode string")

    @staticmethod
    def handle_deviceping_packet(packet):
        print("пакет -  Sender requesting DEVICE_INFO from all destination devices")

    @staticmethod
    def handle_deviceinfo_packet(packet):
        print("пакет -  Device name, firmware version, hardware version, serial number (PING response)")

    @staticmethod
    def handle_parametersettingentry_packet(packet):
        print("пакет -  Configuration item data chunk")

    @staticmethod
    def handle_parameterread_packet(packet):
        print("пакет -  Configuration item read request")

    @staticmethod
    def handle_parameterwrite_packet(packet):
        print("пакет -  Configuration item write request")

    @staticmethod
    def handle_elrsstatus_packet(packet):
        print("пакет -  !!Non Standard!! ExpressLRS good/bad packet count, status flags")

    @staticmethod
    def handle_command_packet(packet):
        print("пакет -  CRSF command execute")

    @staticmethod
    def handle_radioid_packet(packet):
        print("пакет -  Extended type used for OPENTX_SYNC")

    @staticmethod
    def handle_kissreq_packet(packet):
        print("пакет -  KISS request")

    @staticmethod
    def handle_kissresp_packet(packet):
        print("пакет -  KISS response")

    @staticmethod
    def handle_mspreq_packet(packet):
        print("пакет -  MSP parameter request / command")

    @staticmethod
    def handle_mspresp_packet(packet):
        print("пакет -  MSP parameter response chunk")

    @staticmethod
    def handle_mspwrite_packet(packet):
        print("пакет -  MSP parameter write")

    @staticmethod
    def handle_displayportcmd_packet(packet):
        print("пакет -  (CRSFv3) MSP DisplayPort control command")

    @staticmethod
    def handle_ardupilotresp_packet(packet):
        print("пакет -  Ardupilot output?")

# Словарь типов пакетов и соответствующих методов класса обработки
packet_types = {
    #2: PacketHandlers.handle_gps_packet, # CRSF_FRAMETYPE_GPS
    #7: PacketHandlers.handle_vario_packet, # CRSF_FRAMETYPE_VARIO
    #8: PacketHandlers.handle_battery_packet, # CRSF_FRAMETYPE_BATTERY_SENSOR
    #9: PacketHandlers.handle_baroattitude_packet, # CRSF_FRAMETYPE_BARO_ALTITUDE
    #11: PacketHandlers.handle_heartbeat_packet, # CRSF_FRAMETYPE_HEARTBEAT
    20: PacketHandlers.handle_linkstatistics_packet, # CRSF_FRAMETYPE_LINK_STATISTICS
}