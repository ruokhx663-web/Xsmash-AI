import os
import sys
import time
import requests
from config import API_KEY, API_URL, MODEL, SYSTEM_PROMPT

def clear_screen():
    os.system('clear')

def print_banner():
    clear_screen()
    
    # ANSI Escape Codes
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    # ASCII Art Xsmash (Versi gede & sangar)
    ascii_art = f"""{RED}{BOLD}
██╗  ██╗███████╗███╗   ███╗ █████╗ ███████╗██╗  ██╗
╚██╗██╔╝██╔════╝████╗ ████║██╔══██╗██╔════╝██║  ██║
 ╚███╔╝ ███████╗██╔████╔██║███████║███████╗███████║
 ██╔██╗ ╚════██║██║╚██╔╝██║██╔══██║╚════██║██╔══██║
██╔╝ ██╗███████║██║ ╚═╝ ██║██║  ██║███████║██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{RESET}"""

    # Efek animasi kedip 3 kali
    for _ in range(3):
        print(ascii_art)
        time.sleep(0.1)
        clear_screen()
        time.sleep(0.05)
        
    # Tampilkan permanen
    print(ascii_art)
    
    # Info Dev
    print(f"{RED}  [ Xsmash AI ]{RESET}")
    print(f"{RED}  [ Dev: RuningByte ]{RESET}")
    print("\033[90m" + "-" * 52 + "\033[0m")

def tanya_ai(pertanyaan):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": pertanyaan}
        ],
        "temperature": 0.5
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        hasil = response.json()
        return hasil['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"\033[91m[Error] Koneksi gagal atau API key salah. ({e})\033[0m"
    except KeyError:
        return "\033[91m[Error] Format respon dari server tidak valid.\033[0m"

def main():
    if not API_KEY:
        print("\033[91m[Error] API Key tidak ditemukan! buat file .env dulu lalu masukan api dari console.groq.com\033[0m")
        sys.exit(1)

    print_banner()

    while True:
        try:
            user_input = input("\033[96m┌─[RuningByte@xsmash]\n└──╼ $\033[0m ")
            if user_input.lower() in ['exit', 'quit', 'keluar']:
                print("Turut berduka cita... (eh, sampai jumpa!)")
                break
            if user_input.lower() == 'clear':
                print_banner()
                continue
            if not user_input.strip():
                continue

            print("\033[93m[+] Xsmash sedang berpikir...\033[0m")
            jawaban = tanya_ai(user_input)
            
            print("\n\033[92m[Xsmash]:\033[0m")
            print(jawaban)
            print("-" * 40)

        except KeyboardInterrupt:
            print("\nKeluar.")
            break

if __name__ == "__main__":
    main()