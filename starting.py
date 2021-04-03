from midiutil import MIDIFile
import random

from notes import Piano

# degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number

degrees = Piano.get_notes()

# degrees = range(12, 100)
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

for note in degrees[42:52]:
    pitch = note.get("pitch")
    for i in range(1):
        volume = random.choice(volume_choices)
        MyMIDI.addNote(
            track=track,
            channel=channel,
            pitch=pitch + i,
            time=time,
            duration=duration / 8,
            volume=volume,
        )
    time = time + 1 / 8

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
