from subprocess import run
import config as cf

print("Removing bingo sheets in " + cf.BINGO_FOLDER + " folder and " + cf.MERGED_BINGO_SHEETS)
run(['rm', '-rf', cf.BINGO_FOLDER])
run(['rm', cf.MERGED_BINGO_SHEETS])
print('....Done')

print("Removing " + cf.PLAYLIST)
run(['rm', cf.PLAYLIST])
print('....Done')