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
    'NSW':
        # PO boxes
        range(1000, 2000) +
        # General post codes
        range(2000, 2540) +
        # Exclude 2540 (Jervis Bay)
        range(2541, 2600) +
        # Exclude ACT postcode range
        # Include 2611 (Brindabella)
        [2611, 2619] +
        # Exclude 2620 (Hume)
        # Include 2898 (Lord Howe Is) and 2899 (Norfolk Is)
        range(2621, 2900) +
        # Exclude ACT postcode range
        range(2921, 3000) +
        # Include various Murray postcodes on VIC border
        [3500, 3585, 3586, 3644, 3707],
    'ACT':
        # PO boxes
        range(200, 300) +
        # Include 2540 (Jervis Bay)
        [2540] +
        # General post codes
        range(2600, 2611) +
        # Exclude 2611 (Brindabella)
        range(2612, 2619) +
        # Include 2620 (Hume)
        [2620] +
        range(2900, 2921),
    'VIC':
        # General post codes
        range(3000, 3500) +
        # Exclude 3500 (Paringi)
        range(3501, 3585) +
        # Exclude 3585 (Murray Downs)
        # Exclude 3586 (Mallan)
        range(3587, 3644) +
        # Exclude 3644 (Barooga, Lalalty)
        range(3645, 3707) +
        # Exclude 3707 (Bringenbrong)
        range(3708, 4000) +
        # PO boxes
        range(8000, 9000),
    'QLD':
        # General post codes
        range(4000, 5000) +
        # PO boxes
        range(9000, 10000),
    'SA':
        # Include 0872 (Indulkana)
        [872] +
        # General post codes
        # PO boxes
        range(5000, 6000),
    'WA':
        # General post codes
        # Include 6798 (Christmas Is) and 6799 (Cocos / Keeling Is)
        # PO boxes
        range(6000, 7000),
    'TAS':
        # General post codes
        # Include 7151 (Macquarie Is, Antarctic stations)
        # PO boxes
        range(7000, 8000),
    'NT':
        # General post codes
        range(800, 872) +
        # Exclude 0872 (Indulkana)
        # PO boxes
        range(873, 1000),
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
