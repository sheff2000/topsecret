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
        print("пакет -  Signal information. Uplink/Downlink RSSI, SNR, Link Quality (LQ), RF mode, transmit power ")

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
    0x02: PacketHandlers.handle_gps_packet, # CRSF_FRAMETYPE_GPS
    0x07: PacketHandlers.handle_vario_packet, # CRSF_FRAMETYPE_VARIO
    0x08: PacketHandlers.handle_battery_packet, # CRSF_FRAMETYPE_BATTERY_SENSOR
    0x09: PacketHandlers.handle_baroattitude_packet, # CRSF_FRAMETYPE_BARO_ALTITUDE
    0x0B: PacketHandlers.handle_heartbeat_packet, # CRSF_FRAMETYPE_HEARTBEAT
    0x14: PacketHandlers.handle_linkstatistics_packet, # CRSF_FRAMETYPE_LINK_STATISTICS
    0x16: PacketHandlers.handle_rcchannelspacked_packet, # CRSF_FRAMETYPE_RC_CHANNELS_PACKED
    0x17: PacketHandlers.handle_subsetrcchannelspacked_packet, # CRSF_FRAMETYPE_SUBSET_RC_CHANNELS_PACKED
    0x1C: PacketHandlers.handle_linkrxid_packet, # CRSF_FRAMETYPE_LINK_RX_ID
    0x1D: PacketHandlers.handle_linktxid_packet, # CRSF_FRAMETYPE_LINK_TX_ID
    0x1E: PacketHandlers.handle_attitude_packet, # CRSF_FRAMETYPE_ATTITUDE
    0x21: PacketHandlers.handle_flightmode_packet, # CRSF_FRAMETYPE_FLIGHT_MODE
    0x28: PacketHandlers.handle_deviceping_packet, # CRSF_FRAMETYPE_DEVICE_PING
    0x29: PacketHandlers.handle_deviceinfo_packet, # CRSF_FRAMETYPE_DEVICE_INFO
    0x2B: PacketHandlers.handle_parametersettingentry_packet, # CRSF_FRAMETYPE_PARAMETER_SETTINGS_ENTRY
    0x2C: PacketHandlers.handle_parameterread_packet, # CRSF_FRAMETYPE_PARAMETER_READ
    0x2D: PacketHandlers.handle_parameterwrite_packet, # CRSF_FRAMETYPE_PARAMETER_WRITE
    0x2E: PacketHandlers.handle_elrsstatus_packet, # CRSF_FRAMETYPE_ELRS_STATUS
    0x32: PacketHandlers.handle_command_packet, # CRSF_FRAMETYPE_COMMAND
    0x3A: PacketHandlers.handle_radioid_packet, # CRSF_FRAMETYPE_RADIO_ID
    0x78: PacketHandlers.handle_kissreq_packet, # CRSF_FRAMETYPE_KISS_REQ
    0x79: PacketHandlers.handle_kissresp_packet, # CRSF_FRAMETYPE_KISS_RESP
    0x7A: PacketHandlers.handle_mspreq_packet, # CRSF_FRAMETYPE_MSP_REQ
    0x7B: PacketHandlers.handle_mspresp_packet, # CRSF_FRAMETYPE_MSP_RESP
    0x7C: PacketHandlers.handle_mspwrite_packet, # CRSF_FRAMETYPE_MSP_WRITE
    0x7D: PacketHandlers.handle_displayportcmd_packet, # CRSF_FRAMETYPE_DISPLAYPORT_CMD
    0x80: PacketHandlers.handle_ardupilotresp_packet # CRSF_FRAMETYPE_ARDUPILOT_RESP
}