class Scale:
    """ Build a scale by passing a root note (tonic) and scale name """

    def __init__(self, tonic, scale_name):
        self.scale = self.calculateScale(tonic, scale_name)
        self.degrees = {
            'tonic': self.scale[0],
            'supertonic': self.scale[1],
            'mediant': self.scale[2],
            'subdominant': self.scale[3],
            'dominant': self.scale[4],
            'submediant': self.scale[5],
            'leadingtone': self.scale[6],
            'octave': self.scale[7]
        }

    def getScale(self):
        """ Returns scale in array form """
        return self.scale 

    def getDegree(self, degree):
        """ Returns a single note when given a degree (tonic, mediant etc.)"""
        return self.degrees[degree];
            
    def calculateScale(self, tonic, scale_name): 
        # scales available
        scales = {
            'ionian':       [0, 2, 4, 5, 7, 9, 11, 12],
            'dorian':       [0, 2, 3, 5, 7, 9, 10, 12],
            'phrygian':     [0, 1, 3, 5, 7, 8, 10, 12],
            'lydian':       [0, 2, 4, 6, 7, 9, 11, 12],
            'mixolydian':   [0, 2, 4, 5, 7, 9, 10, 12],
            'aeolian':      [0, 2, 3, 5, 7, 8, 10, 12],
            'locrian':      [0, 1, 3, 5, 6, 8, 10, 12]
        }

        # notation variants 
        flat_notes = [
            'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 
            'G', 'Ab', 'A', 'Bb', 'B'
        ]
        sharp_notes = [
            'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 
            'G', 'G#', 'A', 'A#', 'B'
        ]

        # TODO add logic to determine if the scale has flats or sharps 
        # or make interface so both methods are retrievable
        notes = sharp_notes;

        # find the tonic position
        index = notes.index(tonic)
        # rearrange the notes so they start from the tonic 
        head = notes[0:index]
        tail = notes[index:len(notes)]
        notes = tail + head
        # add the trailing octave note
        notes.append(tonic)

        # build scale based on selected notes and steps in the scale
        scale = []
        for step in scales[scale_name]:
             scale.append(notes[step])

        return scale


def new(tonic, scale_name):
    return Scale(tonic, scale_name)
    
