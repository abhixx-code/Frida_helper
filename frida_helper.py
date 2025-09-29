# frida_helper.py
import frida
import sys
import pyfiglet

def banner():
    print(pyfiglet.figlet_format("FRIDA HELPER abhix"))

def on_message(message, data):
    print("[*] Message from Frida:")
    print(message)

def main():
    banner()
    if len(sys.argv) != 3:
        print("Use: python frida_helper.py <process_name> <hook.js>")
        sys.exit(1)

    process_name = sys.argv[1]
    js_script_path = sys.argv[2]

    try:
        with open(js_script_path) as f:
            js_code = f.read()

        device = frida.get_usb_device(timeout=5)
        session = device.attach(process_name)
        script = session.create_script(js_code)
        script.on("message", on_message)
        script.load()

        print("[*] Hook loaded. Press Enter to exit.")
        input()

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()