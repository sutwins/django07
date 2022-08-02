# # pip : pypi.org 에서 다른 개발자들이 개발해놓은 
# # 코드를 가져다 사용할 수 있도록 만든 프로그램

# # import : 다른 파일의 클래스, 함수, 변수를 가져다
# # 사용할 수 있도록 만든 구문!! 

import googletrans
from googletrans import Translator
from gtts import gTTS

text1 = "The U.S. offered to trade an imprisoned Russian arms dealer, Viktor Bout, for the W.N.B.A. star Brittney Griner and another American. Follow updates."
translator = Translator()
trans1 = translator.translate(text1, src='en', dest='zh-cn')

tts = gTTS(trans1.text, lang='zh-cn')
tts.save('hello.mp3')