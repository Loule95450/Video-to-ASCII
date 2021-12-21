
#  Video to ASCII

Launch your MP4 videos on the terminal


## Installation

* On **Linux**: 
    * Run `sudo apt install ffmpeg`
    * Run `pip install -r requirements.txt`

* On **Windows**:
    * Download the installer from [here](https://www.gyan.dev/ffmpeg/builds/) or [here](https://github.com/BtbN/FFmpeg-Builds/releases) and run it
    * Add `ffmpeg` to your `Path`:
        * Go to [Environment Variables](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/)
        * Select `Path` -> Edit -> New and add `C:\FFmpeg\bin` (or wherever you installed `ffmpeg` at the previous step)

    * Run `pip install -r requirements.txt`
* On **MacOS**:
    * Install [Homebrew](https://brew.sh/)
    * Run `brew install ffmpeg`
    * Run `pip install -r requirements.txt`
## Deployment

To deploy this project run

```bash
  python3 main.py my-video.mp4
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

