#!/usr/bin/env python3
import requests, socket, errno, json
import base64 as b64
from python_helper import ansicolors as colors

''' 
This script checks if all the challenges are online and operational.
Currently these challenges are being checked:
Basically Gambling
Business Inquiry
Looking Good
'''
CTF_IP = '84.200.106.95'
CTF_DOMAIN = 'ctf.minzkraut.com'

def print_ok(str_out, symbol=u'\u2714', symcol=colors.OKGREEN, str_color=colors.OKBLUE):
    print("{sym_color}| {sym} |{str_color}{string}{endc}".format(
        sym_color=symcol, sym=symbol, str_color=str_color, string=str_out, endc=colors.ENDC
    ))
def print_fail(str_out, symbol=u'\u2716', symcol=colors.FAIL, str_color=colors.OKBLUE):
    print("{sym_color}| {sym} |{str_color}{string}{endc}".format(
        sym_color=symcol, sym=symbol, str_color=str_color, string=str_out, endc=colors.ENDC
    ))
def print_info(str_out, symbol=u'\u21B3', symcol=colors.OKBLUE, str_color=colors.OKBLUE):
    print_message("-- {}".format(str_out), symbol, symcol, str_color)
def print_message(str_out, symbol=u'\u2610', symcol=colors.HEADER, str_color=colors.OKBLUE):
    print("{sym_color}| {sym} |{str_color}{string}{endc}".format(
        sym_color=symcol, sym=symbol, str_color=str_color, string=str_out, endc=colors.ENDC
    ))
def chk_port(ip, port):
    success = True
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((ip, port))
    except socket.error as e:
        return (False, e)
    finally:
        client.close()
    return (True)

def check_server():
    #Check for SSH
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((CTF_IP, 22))
    except socket.error as e:
        print_fail("Server Offline! (SSH) {} - {}".format(e.errno, e.strerror))
        return False
    finally:
        client.close()
    print_ok("Server Online! (SSH)")
    
    #Check if webserver is ok
    try:
        requests.get("http://{}".format(CTF_DOMAIN))
    except requests.exceptions.ConnectionError as e:
        print_info("Webserver: FAILED at {}! (Connection Error!)".format(CTF_DOMAIN), symcol=colors.FAIL)
    except requests.exceptions.HTTPError as e:
        print_info("Webserver: FAILED with HTTPError {} at {}".format(e.message, CTF_DOMAIN))
    else:
        print_info("Webserver: OK")

    #Check if FTP is ok
    ftp_chk = chk_port(CTF_IP, 21)
    if ftp_chk[0] == True:
        print_info("FTP: Ok")
    else:
        print_info("FTP: FAILED! {}".format(ftp_chk[1].strerror), symcol=colors.FAIL)

    return True

def check_business_inquiry():
    try:
        response = requests.get("http://loremcorp.{}".format(CTF_DOMAIN))
        html = response.text
        if "challenge_chk" in html:
            print_ok("LoremCorp challenge: OK")
            return True
    except requests.exceptions.RequestException:
        print_fail("LoremCorp challenge: Connection Error!")
        return False
    print_fail("LoremCorp Challenge: Not working, chk flag not found!")
    return False

def check_looking_good():
    try:
        response = requests.get("http://loremcorp.{}:8787/login.php".format(CTF_DOMAIN))
        html = response.text
        response = requests.post("http://loremcorp.{}:8787/view.php".format(CTF_DOMAIN), data={'username':'factory_admin', 'password': 'CHANGE_THIS_BEFORE_SHIPPING!'})
        html = html + response.text
        if not "challenge_chk_login" in html:
            print_fail("LookingGood Challenge: challenge_chk_login flag not found!")
        if not "challenge_chk_view" in html:
            print_fail("LookingGood Challenge: challenge_chk_view flag not found!")
        else:
            print_ok("LookingGood challenge: OK")
            return True
    except requests.exceptions.RequestException:
        print_fail("LookingGood challenge: Connection Error!")
        return False
    return False

def check_basically_gambling():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = ""
    try:
        client.connect((CTF_IP, 6646))
        data = client.recv(512)
        data=data.decode()
        data = data.replace('\n', '')
        if b64.b64encode(b64.b64decode(data)) == data.encode():
            print_ok("LuckyNr64 challenge: OK")
            return True
        else:
            print_fail("LuckyNr64 challenge not returning valid base64!")
            print_info(data)
    except socket.error as e:
        print_fail("LuckyNr64 challenge: Socket error! ({} - {})".format(e.errno, e.strerror))
    except UnicodeDecodeError:
        print_fail("LuckyNr64 challenge returning non unicode characters!")
        print_info(data)
    return False

def run_checks():
    print("Checking Server Status")
    if not check_server():
        return False
    print("\n")
    print("Checking Challenges...")
    challenges = [check_business_inquiry, check_looking_good, check_basically_gambling]
    working = 0
    for challenge in challenges:
        if challenge():
            working += 1
    print("{}/{} challenges working".format(working, len(challenges)))

if __name__ == "__main__":
    run_checks()