#!/usr/bin/env python3
import argparse
import subprocess
import re

def get_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="enter the interface to change MAC address")
    parser.add_argument("-m", "--new_mac", dest="new_mac", help="enter New MAC address")
    options = parser.parse_args()
    return options


def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    result = subprocess.check_output(["sudo", "ifconfig", interface])
    return result

def output_result(ifconfig_result):
    filter = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if filter:
        print(f"[+] your mac adreess has successfully been changed to >>> {filter.group(0)}")
    else:
        print("[-] This program could not change your Mac address")


opt = get_cli()
new_Mac = change_mac(opt.interface, opt.new_mac)
output_result(new_Mac)
