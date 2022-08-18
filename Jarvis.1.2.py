import JarvisAI
from JarvisAI import InputsMethods, OutputMethods


# create your own function
# It must contain parameter 'feature_command' which is the command you want to execute
# Return is optional
# If you want to provide return value it should only return text (str)
# Your return value will be displayed or call out by the choice of OutputMethods of JarvisAI

def custom_function(
        feature_command="custom command (which is the command you want to execute)"):
    # write your code here to do something with the command
    # perform some tasks
    # return is optional
    return feature_command + ' Executed'


obj = JarvisAI.JarvisAI(input_method=InputsMethods.voice_input_google_api,
                        output_method=OutputMethods.voice_output,
                        backend_tts_api='pyttsx3',
                        api_key="5ba317a681c5d42361cda5b9f9ba7d0e",
                        detect_wake_word=False,
                        wake_word_detection_method=InputsMethods.voice_input_google_api,
                        bot_name="Jarvis",
                        display_intent=True,
                        google_speech_recognition_input_lang='en',
                        google_speech_recognition_key=None,
                        google_speech_recognition_duration_listening=5
                        )

obj.register_feature(feature_obj=custom_function, feature_command='custom feature')

obj.start()