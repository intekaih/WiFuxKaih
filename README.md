# WiFuxKaih - WiFi Hacking Tool

> Advanced WiFi security testing tool for Termux (Android)

## ⚡ One-Command Installation

```bash
curl -sLo installer.sh https://raw.githubusercontent.com/intekaih/WiFuxKaih/main/installer.sh && bash installer.sh
```

Lệnh này sẽ tự động:
- Cài đặt tất cả packages cần thiết
- Clone repository
- Cài đặt Python dependencies
- Tạo lệnh `wifuxkaih` để chạy từ bất kỳ đâu

## 🚀 Cách sử dụng

```bash
# Chạy mặc định
wifuxkaih

# Chạy với tùy chọn
wifuxkaih -i wlan0 -K

# Cập nhật WiFuxKaih
wifuxkaih update
```

## 📋 Yêu cầu

- Termux (Android)
- Root access
- WiFi adapter hỗ trợ monitor mode

## 🔧 Cài đặt thủ công

```bash
git clone https://github.com/intekaih/WiFuxKaih
cd WiFuxKaih
bash install.sh
```

## 📜 License

For educational purposes only.
