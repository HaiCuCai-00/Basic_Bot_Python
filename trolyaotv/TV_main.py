from typing import Text
import speech_recognition # thư viện chuyển âm thanh người dùng thành ngôn ngữ máy tính
from gtts import gTTS # giúp trợ lý ảo tạo lời nói quá mv3
import os
from datetime import date, datetime

while True:
    # khởi tạo
    # ai_brain = "suy nghĩ của máy" 
    ai_brain = ""   # ban đầu nó chưa được học gì cả nên chưa biết gì
    ai_ear = speech_recognition.Recognizer() #nghe người dùng nói

    # lấy mic
    with speech_recognition.Microphone() as mic:
        print("AI: Đang nghe |--__--| ")
        #AI nghe trong vòng 5s
        audio = ai_ear.record(mic, duration=5)
        print("\nAI: ...")
    try:
        # nghe và nói giọng Việt Nam
        you = ai_ear.recognize_google(audio, language= 'vi-VN')
        print("\n Người sử dụng: " +you )
    except:
        ai_brain = "Tôi không hiểu bạn nói gì cả! ..."
        print("\nAI: " + ai_brain)
    if "Xin chào" in you:
        ai_brain = "Hí chào bạn."
    elif "thời tiết" in you:
        ai_brain = " Bạn đã chỉ tôi xem thời tiết đâu mà hỏi."
    elif "ngày" in you:
        today = date.today()
        ai_brain = today.strftime("%d/%m/%Y")
    elif "giờ" in you:
        now = datetime.now()
        ai_brain = now.strftime("%H:%M:%S")
    elif "Hẹn gặp lại" in you:
        ai_brain = "Chào tạm biệt và hẹn gặp lại"
        print("\nAI: " +ai_brain)
        tts = gTTS(text= ai_brain, lang= 'vi')
        tts.save("C:\\Users\\HaiCuCai\\Desktop\\AI\\trolyaotv\\ai.mp3")
        os.system("C:\\Users\\HaiCuCai\\Desktop\\AI\\trolyaotv\\ai.mp3")
        exit()
    else:
        ai_brain = "Cảm ơn bạn."
        print("\nAI:" +ai_brain)

    print("\nAI:" +ai_brain)

    tts = gTTS(text= ai_brain, lang= 'vi')
    tts.save("C:\\Users\\HaiCuCai\\Desktop\\AI\\trolyaotv\\ai.mp3")
    os.system("C:\\Users\\HaiCuCai\\Desktop\\AI\\trolyaotv\\ai.mp3")