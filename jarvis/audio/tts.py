import io
import wave
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from TTS.api import TTS

# Initialize the TTS model
tts_model = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=True)

def split_text(text, max_length=150):
    """Splits text into smaller chunks to avoid memory issues."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 <= max_length:
            current_chunk.append(word)
            current_length += len(word) + 1
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def say(text: str, speaker="p267"): # p267 (m), p243 (f)
    """Generate and play speech using pydub."""
    print(f"[INFO] Speaking: {text} (Speaker: {speaker})")

    try:
        # Generate speech using the chosen speaker
        audio_data = tts_model.tts(text, speaker=speaker)

        if isinstance(audio_data, list):
            import numpy as np
            audio_data = np.array(audio_data, dtype=np.float32)

        sample_rate = 22050
        audio_data_int16 = (audio_data * 32767).astype(np.int16)

        from pydub import AudioSegment
        from pydub.playback import play

        audio_segment = AudioSegment(
            audio_data_int16.tobytes(),
            frame_rate=sample_rate,
            sample_width=2,
            channels=1
        )

        play(audio_segment)
        print("[INFO] Finished playing audio.")
        return audio_segment

    except MemoryError:
        print("[ERROR] MemoryError occurred during TTS processing.")
