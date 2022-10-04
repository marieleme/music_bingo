"""
Inputs for generating the sheets.
"""
CLIENT_ID = ''
CLIENT_SECRET = ''

""" 
In a sportify "Copy link to playlist"- link, the URI is the section between {[ ]}:

https://open.spotify.com/playlist/ {[37i9dQZEVXcIDk0U5Z8tbq]} ?si=1ec6601cfcf44e5c
"""

PLAYLIST_URI = 'spotify:playlist:37i9dQZEVXcIDk0U5Z8tbq'
AMOUNT_SHEETS = 3


"""
Constants used in the code. Do not alter.
"""
FONT = 'font/Oswald-Regular.ttf'
BINGO_FOLDER = 'BINGO/'
SHEET_NAME = 'bingo_sheet'
PDF = '.pdf'
TMP_SHEET = 'templates/test_sheet.png'
PLAYLIST =  'formatted_playlist.txt'

MERGED_BINGO_SHEETS = 'merged_bingo_sheets.pdf'