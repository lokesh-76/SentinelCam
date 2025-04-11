# 📷 Mobile Camera to Desktop Webcam

Use your smartphone's camera as a live video feed for your desktop — wirelessly and in real-time. No need for external webcams or expensive gear!

## 🚀 Features
- Stream mobile camera feed to desktop using IP
- Real-time video capture with low latency
- Simple UI to display live feed
- Works over WiFi — no cables needed

## 🛠️ Tech Stack
- Python
- OpenCV
- Flask (optional if you want to scale it later)
- Mobile IP webcam app (like [IP Webcam for Android](https://play.google.com/store/apps/details?id=com.pas.webcam))

## 🖥️ How It Works
1. Install an IP camera app on your mobile.
2. Connect both devices to the same WiFi.
3. Run the Python script on your desktop.
4. Enter the mobile's camera stream URL when prompted.
5. View your mobile feed on your desktop!


## 📦 Installation

```bash
git clone https://github.com/lokesh-7676/MobileCamera_To_Desktop
cd MobileCamera_To_Desktop
pip install -r requirements.txt
python main.py

