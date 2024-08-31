# Multi-Feature Cybersecurity Toolkit

Multi-Feature Cybersecurity Toolkit, siber güvenlik uzmanları ve meraklıları için çeşitli güvenlik testleri sunan bir Python aracıdır. Bu araç, port taraması, dizin brute force, şifre güvenliği kontrolü ve basit web güvenlik açıklarını tarama gibi özellikler içerir.

## Özellikler

- **Port Scanner**: Belirli bir IP'deki açık portları tarar.
- **Directory Brute Forcer**: Belirli bir URL'deki gizli dizinleri brute force ile bulur.
- **Password Strength Checker**: Şifrelerin güvenliğini değerlendirir.
- **Basic Web Vulnerability Scanner**: Basit web açıklarını tarar.

## Kurulum

1. **Gerekli Kütüphaneleri Kurun**

    ```bash
    pip install requests
    ```

2. **Repository'yi Klonlayın**

    ```bash
    git clone <repository-url>
    cd cybersecurity-toolkit
    ```

3. **Script'i Çalıştırın**

    - Port Scanner: `python cybersecurity_toolkit.py portscan <IP> <PORTS>`
    - Directory Brute Forcer: `python cybersecurity_toolkit.py dirbrute <URL> <WORDLIST>`
    - Password Strength Checker: `python cybersecurity_toolkit.py passstrength <PASSWORD>`
    - Basic Web Vulnerability Scanner: `python cybersecurity_toolkit.py webvuln <URL>`

## Lisans

Bu proje açık kaynaklıdır ve MIT lisansı altında lisanslanmıştır.
