import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
str1 = "整个系统中，数据的读出和写入是处理的第一步，" \
       "各企业中原有系统的复杂性，决定了与原有系统的对" \
       "接不可能采用统一的方式，为此，在数据集成系统中，" \
       "归纳了以下几种方式，需要根据实际情况，优化选择"
speaker.Speak(str1)
