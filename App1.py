import streamlit as st
from PIL import Image
from gtts import gTTS
import tempfile
from streamlit_option_menu import option_menu
with st.sidebar:
    selected=option_menu(
        menu_title=None,
        options=['About','Generate Speech by Text','Generate Speech by uploading a .txt file'],
        icons=['house','book','book'],
        orientation='vertical')

st.title("T2S.ai 🔊")

url = 'https://images.squarespace-cdn.com/content/v1/584ee3cc2994cac9e545aadd/1614723936610-2YKDTL8LYQ5H2HT147LG/image2.png'
st.image(url, use_column_width=True)


st.header("A Text to Speech Application")
st.markdown("This web app is an AI powered text to speech generation app.Enter text in your language, select the language code.")

if selected=='About':
    st.markdown("This is an AI application useful to generate SPEECH by TEXT. It is developed for translating text to speech which includes many languages. All that you have to do is, enter text in your preferred language and select the language code in the given dropdown menu.")
if selected=='Generate Speech by Text':
    mytext = st.text_area("ENTER TEXT IN YOUR LANGUAGE : ")
    

    ln=st.selectbox("SELECT YOUR LANGUAGE : ",['af:Afrikaans',   'ar:Arabic',   'bg:Bulgarian',   'bn:Bengali',   'bs:Bosnian',  'ca:Catalan',  'cs:Czech',  'cy:Welsh',  'da: Danish',  'de:German',  'el:Greek', 'en:English',  'eo:Esperanto',  'es:Spanish',   'et:Estonian',  'fi:Finnish',   'fr:French',  'gu:Gujarati',  'hi: Hindi',  'hr: Croatian',  'hu:Hungarian',  'hy:Armenian',  'id: Indonesian',  'is:Icelandic',  'it: Italian',  'ja: Japanese',  'jw:Javanese',  'km: Khmer',  'kn: Kannada',  'ko: Korean',   'la: Latin',   'lv: Latvian',  'mk:Macedonian',  'ml:Malayalam', 'mr:Marathi',  'my:Myanmar (Burmese)',  'ne: Nepali',  'nl: Dutch',  'no: Norwegian',  'pl: Polish',  'pt: Portuguese',  'ro: Romanian', 'ru: Russian',  'si:Sinhala',  'sk:Slovak',  'sq:Albanian',  'sr:Serbian',  'su:Sundanese', 'sv:Swedish', 'sw:Swahili', 'ta:Tamil', 'te:Telugu', 'th:Thai',  'tl:Filipino',  'tr:Turkish',  'uk:Ukrainian', 'ur:Urdu','vi:Vietnamese','zh-CN:Chinese', 'zh-TW:Chinese (Mandarin/Taiwan)', 'zh:Chinese (Mandarin)'])

    #ln = st.text_input("Enter language code")

    if mytext and ln:
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
            myobj = gTTS(text=mytext, lang=ln[:2], slow=False)
            myobj.save(temp_audio.name)
            if st.button("Play Audio"):
                st.audio(temp_audio.name, format='audio/mp3')
                st.download_button(label='Download Audio', data=open(temp_audio.name, 'rb').read(),
                                   file_name='audio.mp3', mime='audio/mp3')

if selected == 'Generate Speech by uploading a .txt file':
    st.header("Text File Uploader and Reader")
    
    tfile = st.file_uploader("Upload a text file", type=["txt"])

    if tfile is not None:
        text1 = tfile.read()
        mytext1=text1.decode("utf-8")        
        ln=st.selectbox("SELECT YOUR LANGUAGE : ",['af:Afrikaans',   'ar:Arabic',   'bg:Bulgarian',   'bn:Bengali',   'bs:Bosnian',  'ca:Catalan',  'cs:Czech',  'cy:Welsh',  'da: Danish',  'de:German',  'el:Greek', 'en:English',  'eo:Esperanto',  'es:Spanish',   'et:Estonian',  'fi:Finnish',   'fr:French',  'gu:Gujarati',  'hi: Hindi',  'hr: Croatian',  'hu:Hungarian',  'hy:Armenian',  'id: Indonesian',  'is:Icelandic',  'it: Italian',  'ja: Japanese',  'jw:Javanese',  'km: Khmer',  'kn: Kannada',  'ko: Korean',   'la: Latin',   'lv: Latvian',  'mk:Macedonian',  'ml:Malayalam', 'mr:Marathi',  'my:Myanmar (Burmese)',  'ne: Nepali',  'nl: Dutch',  'no: Norwegian',  'pl: Polish',  'pt: Portuguese',  'ro: Romanian', 'ru: Russian',  'si:Sinhala',  'sk:Slovak',  'sq:Albanian',  'sr:Serbian',  'su:Sundanese', 'sv:Swedish', 'sw:Swahili', 'ta:Tamil', 'te:Telugu', 'th:Thai',  'tl:Filipino',  'tr:Turkish',  'uk:Ukrainian', 'ur:Urdu','vi:Vietnamese','zh-CN:Chinese', 'zh-TW:Chinese (Mandarin/Taiwan)', 'zh:Chinese (Mandarin)'])

        if mytext1 and ln:
            with tempfile.NamedTemporaryFile(delete=False) as temp_audio1:
                myobj = gTTS(text=mytext1, lang=ln[:2], slow=False)
                myobj.save(temp_audio1.name)
                if st.button("Play Audio"):
                    st.audio(temp_audio1.name, format='audio/mp3')
                    st.download_button(label='Download Audio', data=open(temp_audio1.name, 'rb').read(),
                                       file_name='audio.mp3', mime='audio/mp3')