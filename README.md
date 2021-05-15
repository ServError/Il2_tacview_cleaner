# IL2 TacView Cleaner

This quick and dirty utility for IL2 TacView files accomplishes two things:

*Sets Axis colors to blue and Allied colors to red, even when merging recordings from inconsistent clients.
*Removes positionless entries for bombs and some other objects so that they appear on the field when and where they should.

## Usage

* Install Python3
* Download/Extract il2_trackview_cleaner.py
* Open and/or merge all relevant TacView recordings and then save them somewhere as .txt.acmi
* Drag and drop your .txt.acmi file onto il2_trackview_cleaner.py, or call it as follows
```
python3 .\il2_trackview_cleaner.py <filename>
```
* A _cleaned.txt.acmi file will be created in the same directory as your input file
* Load this file in TacView and enjoy