class Chord:
    ''' Build a chord by passing a mode with chord position or chord name '''

    def __init__(self, root, name):
        self.root = root
        self.notes = calculateChordNotes(name)

    def getChord(self):
        ''' Return chord notes as an array '''
        return self.notes

    def getRoot(self):
        return root
        
    def calculateChordNotes(self, name):
        chords = {
            'maj': [0, 4, 7],
            'maj7': [0, 4, 7, 11],
            'm': [0, 3, 7],
            'm7': [0, 3, 7, 10]
        }

    def calculateChordByScale(self, scale):
        return scale

def new():
    return Chord() 
