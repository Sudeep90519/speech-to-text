import streamlit as st
import tts_stt

st.title("Text to Speech and Speech to Text Conversion")

task = st.selectbox('Select the conversion type',options=['Text to Speech','Speech to Text','Text File to Audio','Audio File to Text'])

#Text to Speech
if task == 'Text to Speech':
    
    txt = st.text_input('Enter the text to convert to speech')
    fn = st.text_input('Enter the filename to save audio file, ensure no duplicate names')

    with st.form(key='my_form_to_submit'):
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        tts_stt.textToSpeech(txt,fn)
        
#Speech to Text   
    
elif task == 'Speech to Text':
    pass
    """
    audio = st.audio_input('record a voice message')
    
    with st.form(key='my_form_to_submit'):
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        tts_stt.speechToText(audio)
    """
#Text File to Audio
elif task == 'Text File to Audio':
    file = st.file_uploader('Upload the text file to convert to audio')


    with st.form(key='my_form_to_submit'):
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        raw_text = file.read()
        tts_stt.textFileToSpeech(raw_text)


#Audio File to Text
elif task == 'Audio File to Text':
    file = st.file_uploader('Upload the audio file to convert to text')
    
    with st.form(key='my_form_to_submit'):
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        out = tts_stt.audioFileToText(file)
        st.write(out)