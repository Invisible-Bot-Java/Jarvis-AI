def intro():
    from pydub import AudioSegment
    from pydub.playback import play

    song = AudioSegment.from_wav("Files_Jarvis\\JARVIS_Sound.wav")
    play(song)