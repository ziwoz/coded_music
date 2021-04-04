from itertools import cycle

notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]

# from collections import sorte

start_midi = 12

piano_notes = []

scale_interval = {"major": [2, 2, 1, 2, 2, 2], "minor": [2, 1, 2, 2, 1, 2]}


class Piano:
    @staticmethod
    def get_notes(piano_start=21, piano_end=108):
        piano_notes = []
        piano_range = range(piano_start, piano_end)
        for i in range(9):
            for n, note in enumerate(notes):
                pitch = start_midi + (12 * i + n)
                note_name = f"{note}{i}"
                if pitch in piano_range:
                    piano_notes.append(
                        dict(note_name=note_name, pitch=pitch, note=note)
                    )
        return piano_notes

    @staticmethod
    def get_scale(key="c", scale="major"):
        piano_notes = Piano.get_notes()
        piano_scale_notes = []
        note_cycle = cycle(notes)
        scale_notes = []
        for n in notes:
            note = next(note_cycle)
            if note == key:
                scale_notes.append(note)
                intervals = scale_interval.get(scale)
                for interval in intervals:
                    for i in range(interval):
                        note = next(note_cycle)
                    scale_notes.append(note)
        for note in piano_notes:
            if note.get("note") in scale_notes:
                piano_scale_notes.append(note)
        return piano_scale_notes
