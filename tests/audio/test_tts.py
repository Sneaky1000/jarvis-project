import pytest
import numpy as np
from jarvis.audio.tts import say, split_text
from pydub import AudioSegment

def test_split_text():
    """Ensure text is split correctly into smaller chunks."""
    text = "This is a long test sentence that should be split into multiple chunks because it is too long."
    chunks = split_text(text, max_length=20)
    
    assert isinstance(chunks, list)
    assert all(len(chunk) <= 20 for chunk in chunks)  # Each chunk should be within the limit
    assert sum(len(chunk) for chunk in chunks) >= len(text) - len(chunks)  # Approximate check

@pytest.mark.parametrize("text", [
    "Hello, world!",
    "This is a short test.",
    "Here is a slightly longer text to see if Coqui TTS handles it correctly.",
    "This is a very long sentence that should be properly chunked and processed in multiple pieces to avoid memory errors and ensure the system remains stable without crashing due to excessive memory allocation.",
])
def test_say(text):
    """Ensure the TTS engine processes speech without crashing and produces valid audio."""
    try:
        # Generate audio
        audio_segment = say(text)

        # Validate that the returned object is an AudioSegment
        assert isinstance(audio_segment, AudioSegment), "say() should return a pydub AudioSegment"

        # Ensure that the audio contains data (not empty)
        assert len(audio_segment) > 0, "Generated audio should not be empty"

        # Convert to NumPy array and check min/max values
        samples = np.array(audio_segment.get_array_of_samples())
        assert samples.size > 0, "Generated audio samples should not be empty"
        assert samples.min() < samples.max(), "Audio should have variable amplitude"

    except MemoryError:
        pytest.fail("say() caused a MemoryError!")  # Fail the test if MemoryError occurs
    except Exception as e:
        pytest.fail(f"say() raised an unexpected exception: {e}")
