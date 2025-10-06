# Music Compoaser Problem Definition


## Input
* Key signature (ex. C major, A minor, B flat minor)
* Time signature (ex. 4/4, 6/8, 3/4)
* Tempo in beats per minute
* Melody length in time
* Instrumentation (what does it sound like ex. piano, violin)

## Output
* Generate a **.wav** or **.midi file** (typically easier than .mp3)
* Generate music sheet in a text file. Example:
  * Measure 1: C4-q  E4-q  G#4-q  C5-q
  * Measure 2: Bb4-q  G4-q  E4-q  C4-q

## Representation
* Notes will be represented as **strings** with the following format:

    `[Note][Accidental][Octave]-[Duration]`

**Examples:**
* `C4-q` = C note in the 4th octave as a quarter note
* `F#5-h` = F sharp in the 5th octave as a half note
* `Bb3-e` = B flat in the 3rd octave as an eighth note

**Rules:**
* **Note letter**: A, B, C, D, E, F, G
* **Accidental** (optional): `#` for sharp, `b` for flat
* **Octave number**: 0-8 (where 4 is the middle octave)
* **Duration code**:
  * `w` = whole note (4 beats in 4/4)
  * `h` = half note (2 beats)
  * `q` = quarter note (1 beat)
  * `e` = eighth note (0.5 beats)
  * `s` = sixteenth note (0.25 beats)

## Logic
* Start with the root note of the key
* Each next note is randomly chosen from notes that "fit" in the key

Add some rules to try to form a pattern:
* Prefer notes that are close in pitch (within 3-5 note steps)
* Occasionally allow large jumps in notes for variety
* End on the root note or the fifth for resolution (might change later to have more interesting music)
* Maybe have some presets like arpeggio for more common music "flows"

**The program knows to stop when:**

* Measure count is reached based on user specified length
* Beat count reached based on user specified length
* Natural ending detected:
    * Last note is the root note of the key
    * Last measure feels complete (ends on a strong beat)

**Need to have a combination of all three components for ending**

## Extensions
**Repetitiveness**
* Random notes become boring after 16-32 measures
* Solution: 
    * Add structure (verse, chorus, bridge sections)
    * Introduce themes that repeat with variation

**Memory/File size**
* MIDI files can stay small even for longer pieces
* WAV files get large (1 minute ≈ 10 MB)
* Solution: Use MIDI format, or compress audio


**Lack of musicality**
* Pure randomness doesn't sound good if it goes on for too long
* Solution: 
    * Add rhythm patterns, phrase structure
    * Implement simple harmony (chords in the background)

**Processing time**
* Generating and rendering audio for 5+ minutes takes time
* Solution: Show progress bar and maybe generate in chunks