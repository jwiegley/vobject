#!/usr/bin/env python
"""Test the vCard4() helper function"""

import vobject


def test_vcard4_helper():
    """Test that vCard4() creates a vCard 4.0 object"""
    print("Testing vCard4() helper function...")

    # Create a vCard 4.0 using the helper
    v = vobject.vCard4()

    # Add some content
    v.add('fn').value = 'Test Person'
    v.add('n')
    v.n.value = vobject.vcard.Name(family='Person', given='Test')

    # Add vCard 4.0 specific properties
    v.add('kind').value = 'individual'
    v.add('gender').value = 'M'

    # Serialize (this will auto-generate VERSION if not present)
    result = v.serialize()
    print(result)

    # Verify it's vCard 4.0
    assert 'VERSION:4.0' in result, "VERSION:4.0 not found in output"
    assert 'KIND:individual' in result, "KIND property not found"
    assert 'GENDER:M' in result, "GENDER property not found"

    # Now check the version after serialization
    assert v.version.value == '4.0', f"Expected version 4.0, got {v.version.value}"

    print("\n✓ vCard4() helper function works correctly!")


def test_comparison():
    """Compare vCard 3.0 and 4.0"""
    print("\n" + "=" * 60)
    print("Comparison: vCard() vs vCard4()")
    print("=" * 60)

    # vCard 3.0
    v3 = vobject.vCard()
    v3.add('fn').value = 'John Doe'
    print("\nvCard 3.0:")
    print(v3.serialize())
    assert v3.version.value == '3.0'

    # vCard 4.0
    v4 = vobject.vCard4()
    v4.add('fn').value = 'John Doe'
    print("\nvCard 4.0:")
    print(v4.serialize())
    assert v4.version.value == '4.0'

    print("\n✓ Both versions work correctly!")


if __name__ == '__main__':
    test_vcard4_helper()
    test_comparison()
    print("\n" + "=" * 60)
    print("All tests passed!")
    print("=" * 60)
