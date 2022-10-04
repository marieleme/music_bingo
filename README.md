# music_bingo
Code for generating bingo sheets based on spotify playlist.
## Requirements
* python 3.x <br>
### pip3 install
* pillow
* spotipy
* PyPDF2
* tqdm

## How to generate bingo sheets
REMEMBER: The spotify lists must have a minimum of 25 songs!
#### Extract songs from playlist
Insert your **CLIENT_ID**, **CLIENT_SECRET**, **PLAYLIST_URI** and **AMOUNT_SHEETS** in the `config.py` file. To extract the songs from the spotify playlist, run `step 1` in your compiler. 
> step 1 : Run 
    ```python3 read_spotify_list.py``` 

If you are going to combine more playlists, only alter the **PLAYLIST_URI** by inserting the next playlist uri and do `step 1` again. All the songs from the playlists will be in `formatted_playlist.txt`. If you had more playlists, see that the index numbers is in correct increasing order. If you will tweak on how the songs are presented on the bingo sheets, do this now before moving to the next step.
<br>

#### Generate bingo sheets
Now to make the bingo sheets, run `step 2`. Unique bingo sheets will be made inside the `BINGO/` folder. This folder must be manually made if it does not exist. This process may take a minute, depending on the amount of sheets to be made. 
> step 2 : Run
    ```python3 bingo_map_songs2000.py``` 


#### Merge bingo sheets to one pdf
To Merge the bingo sheets to one pdf, run `step 3`. The merged sheets is now called `merged_bingo_sheets.pdf`.
> step 3 : Run 
    ```python3 merge_the_fuckers.py```

#### Remove old sheets
To remove all old sheets in the `BINGO/` folder, `merged_bingo_sheets.pdf` and `formatted_playlist.txt`, run `step 4`. Be aware that this action will remove the the sheets and files from the computer all together and can not be recovered later. 
> step 4 : Run 
    ```bash delete_sheets.sh```

