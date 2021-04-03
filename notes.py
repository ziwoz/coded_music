notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]

# from collections import sorte

start_midi = 12

piano_notes = []


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
                    piano_notes.append(dict(note=note_name, pitch=pitch))
        return piano_notes
