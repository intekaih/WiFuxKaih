#!/data/data/com.termux/files/usr/bin/bash

GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RESET="\033[0m"

echo -e "${GREEN}[+] Setting up local WiFuxKaih environment...${RESET}"

echo -e "${GREEN}[+] Installing Python dependencies...${RESET}"
pip install -r requirements.txt --break-system-packages

chmod +x main.py

echo -e "${GREEN}[+] Setting up 'wifuxkaih' command...${RESET}"

BIN_DIR="$PREFIX/bin"
WIFUXKAIH_BIN="$BIN_DIR/wifuxkaih"
SCRIPT_DIR="$(pwd)"

cat > "$WIFUXKAIH_BIN" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
cd "$SCRIPT_DIR" || exit

# Update Logic
if [ "\$1" == "update" ]; then
    echo -e "\033[1;32m[+] Fetching latest updates...\\033[0m"
    git reset --hard HEAD > /dev/null 2>&1
    git pull origin main
    
    echo -e "\033[1;32m[+] Checking for new requirements...\\033[0m"
    pip install -r requirements.txt --break-system-packages > /dev/null 2>&1
    
    chmod +x main.py
    echo -e "\033[1;32m[✓] WiFuxKaih updated successfully!\\033[0m"
    exit 0
fi

# Run Logic
if [ -z "\$1" ]; then
    sudo python main.py -i wlan0 -K
else
    sudo python main.py "\$@"
fi
EOF

chmod +x "$WIFUXKAIH_BIN"

echo -e "\n${GREEN}[✓] Local setup complete!${RESET}"
echo -e "${YELLOW}[✓] Type 'wifuxkaih' from anywhere to run the tool.${RESET}"