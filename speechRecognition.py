import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.WavFile('sound\hello.wav') as source:
    audio = recognizer.record(source)

recognizer.energy_threshold = 300

# in sr the energy threshold can be thought as the loudness of audio which is considered speech
# here, values below 300 are considered silence (a silent room is usually between 0 and 100)
# values above 300 are considered speech
# preprocessing is necessary and if our file format is not AudioData, we have to change it
# AudioFile can do preprocessing for us

# DataCamp course:
# Convert audio to AudioFile
clean_support_call = sr.AudioFile('sound\hello.wav')

# Convert AudioFile to AudioData
with clean_support_call as source:
    clean_support_call_audio = recognizer.record(source)

# Transcribe AudioData to text
text = recognizer.recognize_google(clean_support_call_audio,
                                   language="pl-PL")
print(text)

# my version
# show_all shows all possible translations
print(recognizer.recognize_google(audio, language='pl-PL', show_all=True))

# if we don't want the entire audio file, the duration and offset parameters of the record() method can help with this:

# with clean_support_call as source:
#    cut_5 = recognizer.record(source,
#                              duration=None,
#                              offset=10)

# text2 = recognizer.recognize_google(cut_5, language="pl-PL")
# print(text2)
# if recognize_google() method is not able to match the words you speak with any of the words in its repository,
# an exception is thrown - that is why code above is commented out

