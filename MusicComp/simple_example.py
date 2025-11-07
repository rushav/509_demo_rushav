"""
Simple Example: Using the Melody Generator

This script shows basic usage of the melody generator functions.
Perfect for quick testing and experimentation!
"""

import random
from collections import defaultdict

# Set seed for reproducibility
random.seed(42)


# ============================================================================
# CORE FUNCTIONS (simplified versions for quick use)
# ============================================================================

def build_bigram_model(melodies, add_tokens=False):
    """Build a bigram model from melodies."""
    bigram_model = defaultdict(lambda: defaultdict(int))
    
    for melody in melodies:
        if add_tokens:
            melody = ['^'] + melody + ['$']
        
        for i in range(len(melody) - 1):
            current_note = melody[i]
            next_note = melody[i + 1]
            bigram_model[current_note][next_note] += 1
    
    return {k: dict(v) for k, v in bigram_model.items()}


def weighted_random_choice(choices_dict):
    """Choose randomly based on weights."""
    if not choices_dict:
        return None
    
    items = []
    for item, count in choices_dict.items():
        items.extend([item] * count)
    
    return random.choice(items)


def generate_melody(bigram_model, start_note='^', max_length=20, use_end_token=True):
    """Generate a melody using the bigram model."""
    melody = []
    current_note = start_note
    
    while len(melody) < max_length:
        if current_note not in bigram_model:
            break
        
        next_notes = bigram_model[current_note]
        next_note = weighted_random_choice(next_notes)
        
        if next_note is None:
            break
        
        if use_end_token and next_note == '$':
            break
        
        if next_note not in ['^', '$']:
            melody.append(next_note)
        
        current_note = next_note
    
    return melody


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("🎵 Melody Generator - Quick Example")
    print("=" * 60)
    print()
    
    # Example 1: Simple training data
    print("Example 1: Basic C Major Melodies")
    print("-" * 60)
    
    training_melodies = [
        ['C4', 'D4', 'E4', 'F4', 'G4'],
        ['G4', 'F4', 'E4', 'D4', 'C4'],
        ['C4', 'E4', 'G4', 'C5'],
        ['E4', 'F4', 'G4', 'A4', 'G4'],
    ]
    
    print("Training melodies:")
    for i, mel in enumerate(training_melodies, 1):
        print(f"  {i}. {' '.join(mel)}")
    
    # Build model with tokens
    model = build_bigram_model(training_melodies, add_tokens=True)
    
    print("\nGenerated melodies:")
    for i in range(5):
        melody = generate_melody(model, start_note='^', max_length=15)
        print(f"  {i+1}. {' '.join(melody)}")
    
    print()
    
    # Example 2: More complex patterns
    print("Example 2: Mixed Patterns with Sharps")
    print("-" * 60)
    
    complex_melodies = [
        ['E4', 'F#4', 'G4', 'A4', 'B4'],
        ['B4', 'A4', 'G4', 'F#4', 'E4'],
        ['D4', 'E4', 'F#4', 'G4', 'A4'],
        ['A4', 'G4', 'F#4', 'E4', 'D4'],
    ]
    
    print("Training melodies:")
    for i, mel in enumerate(complex_melodies, 1):
        print(f"  {i}. {' '.join(mel)}")
    
    model2 = build_bigram_model(complex_melodies, add_tokens=True)
    
    print("\nGenerated melodies:")
    for i in range(5):
        melody = generate_melody(model2, start_note='^', max_length=12)
        print(f"  {i+1}. {' '.join(melody)}")
    
    print()
    
    # Example 3: Your turn!
    print("Example 3: Create Your Own!")
    print("-" * 60)
    print("Try adding your own melodies here:")
    print()
    print("my_melodies = [")
    print("    ['C4', 'D4', 'E4'],  # Add your melody 1")
    print("    ['E4', 'F4', 'G4'],  # Add your melody 2")
    print("    # ... add more ...")
    print("]")
    print()
    print("model = build_bigram_model(my_melodies, add_tokens=True)")
    print("melody = generate_melody(model)")
    print("print(' '.join(melody))")
    print()
    print("=" * 60)
    print("🎵 Happy melody generating!")
