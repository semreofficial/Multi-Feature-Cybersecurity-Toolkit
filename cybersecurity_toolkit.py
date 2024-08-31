import argparse
import socket
import requests
from itertools import product
from string import ascii_lowercase, ascii_uppercase, digits
from colorama import Fore, Style, init

init()

intro = f"""
{Fore.CYAN}{Style.BRIGHT}
************************************
*                                  *
*           EMRE0X02               *
*                                  *
************************************
{Style.RESET_ALL}
"""

print(intro)

def port_scanner(ip, ports):
    print(f"Port taraması başlatılıyor: {ip}")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Açık port: {port}")
            else:
                print(f"Kapalı port: {port}")

def directory_brute_forcer(url, wordlist):
    print(f"Dizin brute force taraması başlatılıyor: {url}")
    with open(wordlist, 'r') as file:
        directories = file.readlines()
    for directory in directories:
        directory = directory.strip()
        full_url = url.rstrip('/') + '/' + directory
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Bulundu: {full_url}")

def password_strength_checker(password):
    if len(password) < 8:
        print("Şifre çok kısa! En az 8 karakter olmalı.")
        return
    if not any(char.isdigit() for char in password):
        print("Şifre bir rakam içermeli.")
        return
    if not any(char.islower() for char in password):
        print("Şifre bir küçük harf içermeli.")
        return
    if not any(char.isupper() for char in password):
        print("Şifre bir büyük harf içermeli.")
        return
    print("Şifre güçlü!")

def basic_web_vulnerability_scanner(url):
    payloads = ["' OR '1'='1", "<script>alert('XSS');</script>"]
    for payload in payloads:
        test_url = f"{url}?search={payload}"
        response = requests.get(test_url)
        if payload in response.text:
            print(f"Potansiyel açık bulundu: {test_url}")

def main():
    parser = argparse.ArgumentParser(description="Multi-Feature Cybersecurity Toolkit")
    subparsers = parser.add_subparsers(dest='command')
    
    port_parser = subparsers.add_parser('portscan', help='Port tarayıcı')
    port_parser.add_argument('ip', help='Tarama yapılacak IP adresi')
    port_parser.add_argument('ports', nargs='+', type=int, help='Tarama yapılacak portlar')
    
    dir_parser = subparsers.add_parser('dirbrute', help='Dizin brute force')
    dir_parser.add_argument('url', help='Hedef URL')
    dir_parser.add_argument('wordlist', help='Kelimeler listesi dosyası')
    
    pass_parser = subparsers.add_parser('passstrength', help='Şifre güvenliği kontrolü')
    pass_parser.add_argument('password', help='Güçlendirilecek şifre')
    
    vuln_parser = subparsers.add_parser('webvuln', help='Web güvenlik açıkları tarayıcısı')
    vuln_parser.add_argument('url', help='Hedef URL')
    
    args = parser.parse_args()
    
    if args.command == 'portscan':
        port_scanner(args.ip, args.ports)
    elif args.command == 'dirbrute':
        directory_brute_forcer(args.url, args.wordlist)
    elif args.command == 'passstrength':
        password_strength_checker(args.password)
    elif args.command == 'webvuln':
        basic_web_vulnerability_scanner(args.url)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
