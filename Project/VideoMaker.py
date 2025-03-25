import streamlit as st
import Passwords  # Assuming you need this elsewhere
import os

from utility.captions.timed_captions_generator import generate_timed_captions
from utility.render.render_engine import get_output_media
from utility.video.background_video_generator import generate_video_url
from utility.video.video_search_query_generator import getVideoSearchQueriesTimed, merge_empty_intervals  # Assuming you need this elsewhere

st.set_page_config(layout="wide")
st.sidebar.subheader = "Stage"

if "menu" not in st.session_state:
    st.session_state["menu"] = "Script Generation"

menu = st.sidebar.selectbox(
    "",
    ["Script Generation", "Voiceover", "Video Generation"],
    index=["Script Generation", "Voiceover", "Video Generation"].index(st.session_state["menu"])
)
VIDEO_SERVER = "pexel"
AUDIO_PATH = "audio_tts.wav"
languages = ["English (United States)", 
             "English (United Kingdom)", 
             "English (Australia)", 
             "English (Canada)",
             "English (India)",
             "English (New Zealand)",
             "English (Ireland)",
             "English (South Africa)"
             ]


voices_codes = {
    "English (United States)": [
        ["en-US-GuyNeural", "en-US-ChristopherNeural"],  # Male voices
        ["en-US-AriaNeural", "en-US-JennyNeural", "en-US-AmberNeural", "en-US-AnaNeural"]  # Female voices
    ],
    "English (United Kingdom)": [
        ["en-GB-RyanNeural", "en-GB-GeorgeNeural"],  # Male voices
        ["en-GB-LibbyNeural", "en-GB-SoniaNeural"]  # Female voices
    ],
    "English (Australia)": [
        ["en-AU-WilliamNeural"],  # Male voices
        ["en-AU-NatashaNeural"]  # Female voices
    ],
    "English (Canada)": [
        ["en-CA-LiamNeural"],  # Male voices
        ["en-CA-ClaraNeural"]  # Female voices
    ],
    "English (India)": [
        ["en-IN-PrabhatNeural"],  # Male voices
        ["en-IN-NeerjaNeural"]  # Female voices
    ],
    "English (New Zealand)": [
        ["en-NZ-MitchellNeural"],  # Male voices
        ["en-NZ-MollyNeural"]  # Female voices
    ],
    "English (Ireland)": [
        ["en-IE-ConnorNeural"],  # Male voices
        ["en-IE-EmilyNeural"]  # Female voices
    ],
    "English (South Africa)": [
        ["en-ZA-ThembaNeural"],  # Male voices
        ["en-ZA-TessaNeural"]  # Female voices
    ]
}



if menu == "Script Generation":
    st.title("Script Generation and Voiceover")

    st.markdown(
        """
        <style>
        .custom-label {
            font-size: 20px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    # Initialize session state variables
    if "textarea_value" not in st.session_state:
        st.session_state["textarea_value"] = ""  # Default value for script
    if "audio" not in st.session_state:
        st.session_state["audio"] = 0 # Default value for

    # Function to generate the script
    def generate_script(user_prompt):
        from utility.script.script_generator import generate_script
        return generate_script(user_prompt)

    # Create columns for input and button
    col1, col2 = st.columns([4, 1])  # Adjust column widths as needed

    # Capture user prompt
    with col1:
        user_prompt = st.text_input(
            "Topic",
            placeholder="Enter your topic here"
        )

    # Add button to generate script
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # Add space to align with text input
        if st.button("Generate Script"):
            if user_prompt.strip():  # Ensure the input is not empty
                st.session_state["textarea_value"] = generate_script(user_prompt)
            else:
                st.warning("Please enter a valid topic to generate a script.")



    # Render the updated text area value
    script = st.text_area("Script", height=300, value=st.session_state["textarea_value"])
    if st.session_state["textarea_value"] != "":
        def script_next():
            st.session_state["menu"] = "Voiceover"

        st.button("Next",on_click=script_next)







if menu == "Voiceover" :
    if st.session_state["textarea_value"] != "":
        # script = "Get ready for some incredible turtle facts! 1. Turtles have been around for 220 million years, surviving alongside dinosaurs. 2. They can't retract their limbs into their shells for protection like other turtles might. 3. Sea turtles can travel up to 22 miles per hour, faster than some cars! 4. Leatherback sea turtles are the largest turtle species, sometimes growing over 6 feet long. 5. A turtle's shell is not just one piece; it's made up of over 50 bones. 6. Despite their slow speed, turtles can live for over 100 years, making them some of the longest-living creatures. 7. Turtle eggs can take up to 100 days to hatch! 8. Turtles play a key role in the ecosystem by controlling jellyfish and sea grass populations. Fascinating, huh?"

        st.title("Voiceover Generation")

        dash, configuration = st.columns([70,30])
        dash.markdown(
            """
            <h3 style="margin-bottom: 10px;">Your script</h3>
            """,
            unsafe_allow_html=True,
        )
        # Display the script
        dash.markdown(
            f"""
            <div style="margin-top: 0px; font-size: 16px; line-height: 1.5; text-align:justify;">
                {st.session_state["textarea_value"]}
            </div>
            """,
            unsafe_allow_html=True,
        )
        col1, col2= configuration.columns([1,3])
        col2.subheader("Audio Settings")

        lang = col2.selectbox("Select Language", languages)
        col2.markdown("<br>", unsafe_allow_html=True)
        gender = col2.selectbox("Select Voice Gender",["Male", "Female"])
        col2.markdown("<br>", unsafe_allow_html=True)
        
        if gender == "Male":
            voices = voices_codes[lang][0]
        else:
            voices = voices_codes[lang][1]
        
        

        voice = col2.selectbox("Select Voice Gender", voices)
        col2.markdown("<br>", unsafe_allow_html=True)

        if col2.button("Generate Voiceover"):
                import asyncio
                from utility.audio.audio_generator import generate_audio
                asyncio.run(generate_audio(st.session_state["textarea_value"], AUDIO_PATH, voice))
                # asyncio.run(generate_audio(script, AUDIO_PATH, voice))
                st.session_state["audio"] = 1



        dash.markdown("<br>", unsafe_allow_html=True)
        
        if os.path.exists(AUDIO_PATH) and st.session_state["audio"] == 1:
            dash.subheader("Voicover Audio")
            dash.audio(AUDIO_PATH)

        col1,col2,col3,col4,col5,col6,col7 = dash.columns(7)
        def voice_prev():
            st.session_state["menu"] = "Script Generation"
        col1.button("Previous", on_click= voice_prev)

        if os.path.exists(AUDIO_PATH) and st.session_state["audio"] == 1:
            def voice_next():
                st.session_state["menu"] = "Video Generation"
            col2.button("Next",on_click=voice_next)

    else:
        st.title("Voiceover Generation")
        st.warning("Please complete the Script Generation and you will be able to generate audio here. ")


if menu == "Video Generation":
    st.title("Video Generation")
    if st.session_state["audio"] == 1 and st.session_state["textarea_value"] != "":
        st.markdown("All Set! Ready for the magic?")
        def generate_video():
            
            timed_captions = generate_timed_captions(AUDIO_PATH)
            print(timed_captions)

            search_terms = getVideoSearchQueriesTimed(st.session_state["textarea_value"], timed_captions)
            print(search_terms)

            background_video_urls = None
            if search_terms is not None:
                background_video_urls = generate_video_url(search_terms, VIDEO_SERVER)
                print(background_video_urls)
            else:
                print("No background video")

            background_video_urls = merge_empty_intervals(background_video_urls)

            if background_video_urls is not None:
                video = get_output_media(AUDIO_PATH, timed_captions, background_video_urls, VIDEO_SERVER)
                print(video)
        st.button("Next",on_click=generate_video)
        
        if os.path.exists("rendered_video.mp4"):
            st.video("rendered_video.mp4")

    else:
        st.warning("Please complete the Script Generation and Voiceover Generation to access Video Generation")