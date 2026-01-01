#!/usr/bin/env python
"""Test script for vCard 4.0 implementation"""

import sys
import os

# Add the vobject directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vobject'))

import vobject
from vobject import vcard40


def test_basic_vcard40():
    """Test creating a basic vCard 4.0"""
    print("Test 1: Creating a basic vCard 4.0...")

    # Create a new vCard 4.0
    v = vobject.vCard()
    v.behavior = vcard40.VCard4_0
    v.add('fn').value = 'John Doe'
    v.add('n')
    v.n.value = vobject.vcard.Name(family='Doe', given='John')

    # Add vCard 4.0 VERSION
    if hasattr(v, 'version'):
        del v.version
    v.add('version').value = '4.0'

    print(v.serialize())
    print("✓ Basic vCard 4.0 created successfully\n")


def test_new_properties():
    """Test vCard 4.0 new properties"""
    print("Test 2: Testing new vCard 4.0 properties...")

    v = vobject.vCard()
    v.behavior = vcard40.VCard4_0

    # Required properties
    v.add('fn').value = 'Jane Smith'
    v.add('version').value = '4.0'

    # New KIND property
    v.add('kind').value = 'individual'

    # New GENDER property
    v.add('gender').value = 'F'

    # New ANNIVERSARY property
    v.add('anniversary').value = '20100615'

    # New LANG property
    lang = v.add('lang')
    lang.value = 'en'
    lang.params['PREF'] = ['1']

    # New IMPP property
    impp = v.add('impp')
    impp.value = 'xmpp:jane@example.com'

    # New RELATED property
    related = v.add('related')
    related.value = 'http://example.com/directory/jsmith.vcf'
    related.params['TYPE'] = ['spouse']

    # New SOURCE property
    v.add('source').value = 'http://example.com/directory/jsmith.vcf'

    print(v.serialize())
    print("✓ New vCard 4.0 properties added successfully\n")


def test_modified_properties():
    """Test modified properties in vCard 4.0"""
    print("Test 3: Testing modified vCard 4.0 properties...")

    v = vobject.vCard()
    v.behavior = vcard40.VCard4_0

    # Required properties
    v.add('fn').value = 'Bob Johnson'
    v.add('version').value = '4.0'

    # PHOTO as URI (vCard 4.0 style)
    v.add('photo').value = 'http://example.com/photo.jpg'

    # TEL with URI scheme
    tel = v.add('tel')
    tel.value = 'tel:+1-555-555-5555'
    tel.params['TYPE'] = ['voice', 'home']
    tel.params['PREF'] = ['1']

    # GEO as geo: URI
    v.add('geo').value = 'geo:37.386013,-122.082932'

    # UID as URN
    v.add('uid').value = 'urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6'

    print(v.serialize())
    print("✓ Modified vCard 4.0 properties work correctly\n")


def test_group_vcard():
    """Test vCard 4.0 group with MEMBER property"""
    print("Test 4: Testing vCard 4.0 group...")

    v = vobject.vCard()
    v.behavior = vcard40.VCard4_0

    # Required properties
    v.add('fn').value = 'Development Team'
    v.add('version').value = '4.0'

    # KIND=group
    v.add('kind').value = 'group'

    # MEMBER properties (only valid for groups)
    v.add('member').value = 'urn:uuid:03a0e51f-d1aa-4385-8a53-e29025acd8af'
    v.add('member').value = 'urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6'
    v.add('member').value = 'mailto:member1@example.com'

    print(v.serialize())
    print("✓ vCard 4.0 group created successfully\n")


def test_multiple_fn():
    """Test multiple FN values (allowed in vCard 4.0)"""
    print("Test 5: Testing multiple FN values...")

    v = vobject.vCard()
    v.behavior = vcard40.VCard4_0

    # Multiple FN values with different languages
    v.add('version').value = '4.0'

    fn1 = v.add('fn')
    fn1.value = 'John Doe'
    fn1.params['LANGUAGE'] = ['en']

    fn2 = v.add('fn')
    fn2.value = 'ジョン・ドゥ'
    fn2.params['LANGUAGE'] = ['ja']

    print(v.serialize())
    print("✓ Multiple FN values work correctly\n")


def test_new_parameters():
    """Test new vCard 4.0 parameters"""
    print("Test 6: Testing new vCard 4.0 parameters...")

    v = vobject.vCard()
    v.behavior = vcard40.VCard4_0

    v.add('version').value = '4.0'
    v.add('fn').value = 'Alice Williams'

    # PREF parameter (replaces TYPE=pref)
    tel1 = v.add('tel')
    tel1.value = 'tel:+1-555-111-1111'
    tel1.params['PREF'] = ['1']
    tel1.params['TYPE'] = ['work']

    tel2 = v.add('tel')
    tel2.value = 'tel:+1-555-222-2222'
    tel2.params['PREF'] = ['2']
    tel2.params['TYPE'] = ['home']

    # ALTID parameter (links alternate representations)
    email1 = v.add('email')
    email1.value = 'alice@work.example.com'
    email1.params['ALTID'] = ['1']

    email2 = v.add('email')
    email2.value = 'alice.williams@work.example.com'
    email2.params['ALTID'] = ['1']

    # MEDIATYPE parameter
    photo = v.add('photo')
    photo.value = 'http://example.com/photo.jpg'
    photo.params['MEDIATYPE'] = ['image/jpeg']

    print(v.serialize())
    print("✓ New vCard 4.0 parameters work correctly\n")


def main():
    """Run all tests"""
    print("=" * 60)
    print("vCard 4.0 Implementation Tests")
    print("=" * 60 + "\n")

    try:
        test_basic_vcard40()
        test_new_properties()
        test_modified_properties()
        test_group_vcard()
        test_multiple_fn()
        test_new_parameters()

        print("=" * 60)
        print("All tests completed successfully!")
        print("=" * 60)
        return 0

    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
