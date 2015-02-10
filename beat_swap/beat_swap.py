#!/usr/bin/env python
# encoding: utf=8
"""
beat_swap.py

Swap the first and second beats in a bar.

By Noran Diaconu, 2015-02-10.
"""
import echonest.remix.audio as audio

usage = """
Usage: 
    python beat_swap.py <input_filename> <output_filename>

Example:
    python beat_swap.py lateralus.mp3 lateralus_swap.mp3
"""

def main(input_filename, output_filename):
    audiofile = audio.LocalAudioFile(input_filename)
    bars = audiofile.analysis.bars
    collect = audio.AudioQuantumList()
    for bar in bars:
        beats = bar.children()
        if (len(beats) >= 3):
            (beats[1], beats[2]) = (beats[2], beats[1])
        for beat in beats:
            collect.append(beat);
    out = audio.getpieces(audiofile, collect)
    out.encode(output_filename)

if  __name__ == '__main__':
    import sys
    try:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    except:
        print usage
        sys.exit(-1)
    main(input_filename, output_filename)
