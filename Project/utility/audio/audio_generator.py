import edge_tts

async def generate_audio(text,outputFilename, voice):
    communicate = edge_tts.Communicate(text,voice)
    await communicate.save(outputFilename)





