from elevenlabslib import ElevenLabsUser
import os
from tqdm import tqdm
import json

user = ElevenLabsUser("f316517857e3440132d1461b83d1ac10")
emotions = {"Happy": "gnvwAqyOCqIZvFwKkjrL", 
        "Sad": "veA4m8Z1vsC4gldrGbZe", 
        "Angry": "PluiXb1yLydMsqGb0AoD",
        "Astonished": "mo72GKoVPleyLUwvA5Jf"}

def generate_samples(dialogue, emotion, id, num_variations=5, path="samples"):
    # check if path exists, if not, create it
    if not os.path.exists(path):
        os.makedirs(path)
        
    voice = user.get_voice_by_ID(emotions[emotion])
    performances = []
    # make sample options and generate a UID for each
    for i in range(num_variations):
        performances.append(voice.generate_audio_bytes(dialogue))

    # save the samples to disk with the UID as the filename
    flenames = []
    for i, performance in enumerate(performances):
        fn = os.path.join(path, f"{id}_{i}.mp3")
        with open(fn, "wb") as f:
            f.write(performance)
            # convert to windows format
            fn = fn.replace("/", "\\")
            flenames.append(fn)
    return flenames


with open("lines.txt", "r") as f:
    lines = f.readlines()

generated_samples = []
for line in tqdm(lines):
    t = eval(line)
    emotion = t[0]
    dialogue = t[1]
    # hash the dialogue to get a unique ID
    dialogue_hash = hash(dialogue)
    sample_fns = generate_samples(dialogue, emotion, dialogue_hash, path="tracks_mp3")
    for i, sample_fn in enumerate(sample_fns):
        # convert to wav and save to disk        
        # move the mp3 to the archive
        generated_samples.append({"Name": f"{str(dialogue_hash)}_{i}", "emotion": emotion, "text": dialogue, "mp3": sample_fn, "wav": sample_fn.replace("mp3", "wav")})

with open("generated_samples.json", "w") as f:
    json.dump(generated_samples, f)