def get_frequency(note):
    note_frequencies = {
        'C': 261.63,
        'D': 293.66,
        'E': 329.63,
        'F': 349.23,
        'G': 392.00,
        'A': 440.00,
        'B': 493.88}
  
    letter = note[0]
    octave = int(note[1])

#Adjust frequency for different octaves

    base_frequency = note_frequencies[letter]
    base_frequency /= (2 ** (4 - octave))
    return base_frequency

input_note_user = input("Please type note (like A4,B4 etc) :  ").upper()     
frequency = get_frequency(input_note_user)

if frequency:
    print(f"The frequency of {input_note_user} is {frequency:.1f} Hz.")
else:
    print("Invalid note input.")