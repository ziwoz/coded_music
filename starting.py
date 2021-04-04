from midiutil import MIDIFile
import random

from notes import Piano


degrees = Piano.get_scale(key="a", scale="minor")

track = 0
channel = 0
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

volume_choices = [40, 60, 80, 100]

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track
# automatically created)
MyMIDI.addTempo(track, time, tempo)

for note in degrees:
    pitch = note.get("pitch")
    for i in range(1):
        volume = random.choice(volume_choices)
        MyMIDI.addNote(
            track=track,
            channel=channel,
            pitch=pitch + i,
            time=time,
            duration=duration,
            volume=volume,
        )
    time = time + 1

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
