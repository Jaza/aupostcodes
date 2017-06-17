__version__ = '0.1.1'

# Australian postcode allocation mapping utility.
# State-to-postcode mapping based on information from:

# http://en.wikipedia.org/wiki/Postcodes_in_Australia
# As of 6 Apr 2010

# Includes:
# - General postcode ranges for all states and territories
# - Newer LVR and PO box ranges
# - Special rules, e.g. for postcodes on state borders
# - Postcodes for external territories (islands and Antarctic stations)

STATES_FOR_POSTCODES = {
    # Note: wrapping each range() in list(), this is the most
    # dead-simple way of making this code Python 2 (range() returns a
    # list) and Python 3 (range() returns a generator) compatible.
    'NSW':
        # PO boxes
        list(range(1000, 2000)) +
        # General post codes
        list(range(2000, 2540)) +
        # Exclude 2540 (Jervis Bay)
        list(range(2541, 2600)) +
        # Exclude ACT postcode range
        # Include 2611 (Brindabella)
        [2611, 2619] +
        # Exclude 2620 (Hume)
        # Include 2898 (Lord Howe Is) and 2899 (Norfolk Is)
        list(range(2621, 2900)) +
        # Exclude ACT postcode range
        list(range(2921, 3000)) +
        # Include various Murray postcodes on VIC border
        [3500, 3585, 3586, 3644, 3707],
    'ACT':
        # PO boxes
        list(range(200, 300)) +
        # Include 2540 (Jervis Bay)
        [2540] +
        # General post codes
        list(range(2600, 2611)) +
        # Exclude 2611 (Brindabella)
        list(range(2612, 2619)) +
        # Include 2620 (Hume)
        [2620] +
        list(range(2900, 2921)),
    'VIC':
        # General post codes
        list(range(3000, 3500)) +
        # Exclude 3500 (Paringi)
        list(range(3501, 3585)) +
        # Exclude 3585 (Murray Downs)
        # Exclude 3586 (Mallan)
        list(range(3587, 3644)) +
        # Exclude 3644 (Barooga, Lalalty)
        list(range(3645, 3707)) +
        # Exclude 3707 (Bringenbrong)
        list(range(3708, 4000)) +
        # PO boxes
        list(range(8000, 9000)),
    'QLD':
        # General post codes
        list(range(4000, 5000)) +
        # PO boxes
        list(range(9000, 10000)),
    'SA':
        # Include 0872 (Indulkana)
        [872] +
        # General post codes
        # PO boxes
        list(range(5000, 6000)),
    'WA':
        # General post codes
        # Include 6798 (Christmas Is) and 6799 (Cocos / Keeling Is)
        # PO boxes
        list(range(6000, 7000)),
    'TAS':
        # General post codes
        # Include 7151 (Macquarie Is, Antarctic stations)
        # PO boxes
        list(range(7000, 8000)),
    'NT':
        # General post codes
        list(range(800, 872)) +
        # Exclude 0872 (Indulkana)
        # PO boxes
        list(range(873, 1000)),
}

def state_for_postcode(postcode):
    """Given an Australian postcode, return the state that it belongs in."""

    if postcode == '':
        postcode = 0
    try:
        postcode = int(postcode)
    except ValueError:
        raise ValueError('Unable to cast postcode value to int.')

    for state, postcodes in STATES_FOR_POSTCODES.items():
        if postcode in postcodes:
            return state
