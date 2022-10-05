"""
Inputs for generating the sheets.
"""
CLIENT_ID = 'fc159782247541d5ae69990c5da06a11'
CLIENT_SECRET = '15fe05d936394bb192b619018dac92c5'

""" 
In a sportify "Copy link to playlist"- link, the URI is the section between {[ ]}:

https://open.spotify.com/playlist/ {[37i9dQZEVXcIDk0U5Z8tbq]} ?si=1ec6601cfcf44e5c
"""

PLAYLIST_PREFIX = 'spotify:playlist:'
PLAYLIST_URI = '37i9dQZEVXcIDk0U5Z8tbq'
PLAYLIST_URI = PLAYLIST_PREFIX + PLAYLIST_URI

AMOUNT_SHEETS = 3


""" 
Constants used for logo placement (leave LOGO empty if not in use)
"""
LOGO = '' # Leave LOGO empty if not in use
LOGO_DIM = 400 # Choose size of logo
# if logo isn't 1:1 scale you can change the X and Y scale manually
LOGO_DIM_X = LOGO_DIM
LOGO_DIM_Y = LOGO_DIM
# Choose placement of logo from the border
LOGO_X = 0
LOGO_Y = 0

"""
Constants used in the code. Do not alter.
"""
FONT = 'font/Oswald-Regular.ttf'
BINGO_FOLDER = 'BINGO/'
SHEET_NAME = 'bingo_sheet'
PDF = '.pdf'
TMP_SHEET = 'templates/blank_sheet.png'
PLAYLIST =  'formatted_playlist.txt'




MERGED_BINGO_SHEETS = 'merged_bingo_sheets.pdf'