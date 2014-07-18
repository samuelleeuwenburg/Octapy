import note

class Scale:
    ''' Build a scale by passing a root note (tonic) and scale name '''

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
            'octave': self.scale[1]
        }

    def getScale(self):
        ''' Returns scale as an array '''
        return self.scale 

    def getDegree(self, degree):
        ''' Returns a single note when given a degree (tonic, mediant etc.) '''
        return self.degrees[degree];
            
    def calculateScale(self, tonic, scale_name): 
        # scales/mode available
        scales = {
            'ionian':       [1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5],
            'dorian':       [1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0],
            'phrygian':     [0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0],
            'lydian':       [1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5],
            'mixolydian':   [1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 1.0],
            'aeolian':      [1.0, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0],
            'locrian':      [0.5, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0],
        }
        
        # build the scale by starting with the root note
        scale = [tonic]
        for i, step in enumerate(scales[scale_name]):
            n = note.new(scale[i].name, scale[i].accidental)
            n.transpose(step)
            scale.append(n)

        return scale


def new(tonic, scale_name):
    return Scale(tonic, scale_name)
    
