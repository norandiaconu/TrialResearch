# TrialResearch
Beat Swap Module

#Problem
We want to swap the first two beats in each bar of a song.

#Question
1. Will this work for any song?
2. How do you identify the bars in a song?
3. How do you identify the beats in a song?

#Resources
1. [Pyechonest]
2. [Remix Examples]

###Abstract
After importing the mp3, it can be analyzed using the Echonest API. You are able to find and make the necessary changes in a for loop.
```python
for bar in bars:
        beats = bar.children()
        if (len(beats) >= 3):
            (beats[1], beats[2]) = (beats[2], beats[1])
        for beat in beats:
            collect.append(beat);
```
You can then call the program on a file and supply an output filename to run the program.
```python
python beat_swap.py <input_filename> <output_filename>
python beat_swap.py lateralus.mp3 lateralus_swap.mp3
```

[Pyechonest]: https://github.com/echonest/pyechonest
[Remix Examples]: https://github.com/echonest/remix-examples
