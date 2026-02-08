"""
Example test file to demonstrate testing in this repository.
This tests the Animal class from the Property.py example.
"""
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from exercise.Decorators.Property import Animal


def test_animal_creation():
    """Test that an Animal can be created with a name."""
    animal = Animal("Buddy")
    assert animal.name == "Buddy"


def test_animal_display_name():
    """Test that the display_name property works correctly."""
    animal = Animal("Max")
    assert animal.display_name == "Max"


def test_animal_display_name_is_property():
    """Test that display_name is a property, not a method."""
    animal = Animal("Charlie")
    # Should be able to access without parentheses
    name = animal.display_name
    assert name == "Charlie"


if __name__ == "__main__":
    # Allow running tests directly
    test_animal_creation()
    test_animal_display_name()
    test_animal_display_name_is_property()
    print("All tests passed!")
