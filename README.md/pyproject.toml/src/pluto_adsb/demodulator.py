class Demodulator():
    #Returns a list of complete raw messages for the decoder to interpret
    # Each object is 14 bytes long for decoding into 112 bit messages

    def process(samples): 
        #Takes in I/Q samples, retains a tail of messages, and then returns zero or more complete messages