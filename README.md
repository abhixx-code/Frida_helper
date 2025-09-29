# 🛠️ FRIDA HELPER – Termux ke liye Simple Frida Tool

**FRIDA HELPER** ek Python script hai jo Frida ke basic use ko asaan aur stylish tarike se samjhata hai. Ye specially Termux users ke liye banaya gaya hai jo Android apps ko ethically reverse engineer karna chahte hain.

## 🔧 Features
- Stylish banner using `pyfiglet`
- USB device se Frida attach hota hai
- JavaScript hook script load karta hai
- Beginner-friendly error messages

## 📦 Files Included
- `frida_helper.py` – Main Python script
- `hook.js` – Sample Frida hook script
- `README.md` – Hindi + English guide

## 🧠 Kaise Use Kare (Step-by-Step)

### 1. Termux Setup
```bash
pkg update && pkg upgrade
pkg install python
pip install frida-tools pyfiglet
