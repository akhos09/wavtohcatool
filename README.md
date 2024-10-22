
# YouTube to WAV Downloader and Converter to .HCA

This Python script allows you to download audio from YouTube videos in `.wav` format and convert multiple `.wav` files into `.hca` and looping that files using `VGAudiocli.exe`. 

## Table of Contents
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Dependencies

This script requires the following libraries and tools:

1. **yt-dlp**: A command-line program to download videos from YouTube and other sites.
2. **ffmpeg**: A multimedia framework for handling video, audio, and other multimedia files and streams, does all the proccess of downloading the `.wav` file of the URL from YouTube.
3. **SciPy**: For reading `.wav` files and the metadata of them.
4. **Tkinter**: For the file dialog to select `.wav` files.
5. **VGAudioCLI**: An executable which utility is to convert selected `.wav` files to `.hac`.
6. **(Optional) PyTube**: Library that is required for the URL extractor tool.
### Install Required Libraries

You can install the necessary Python libraries using `pip`. Run the following command:

```
pip install yt-dlp scipy
```

### Install FFmpeg
1. Download the .exe from [FFmpeg's official site](https://ffmpeg.org/download.html). or [FFmpeg's repository](https://github.com/BtbN/FFmpeg-Builds/releases) (Personally I prefer the repository). 
2. Extract the downloaded ZIP file to the directory where the script is located at.

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/akhos09/wavtohac.git
   cd WavToHac
   ```

2. Ensure that all dependencies are installed as outlined above.

3. Place `ffmpeg.exe` in the same directory as this script or specify the correct path in the code.

## Usage

1. **Run the script**:

   Open a terminal or command prompt and navigate to the directory containing the script. Run the following command:

   ```bash
   python wavtohac.py
   ```

2. **Download Music**:

   - When prompted, type `y` to download music.
   - Paste the YouTube URL and ensure it is valid. You can paste one per input until you hit enter.
   - Specify the name for the `.wav` file without the extension ``.
   - Repeat for multiple URLs as desired.

3. **Convert WAV Files**:

   - After downloading, you will be prompted to select multiple `.wav` files using a file dialog.
   - For each selected file, specify the output `.hca` filename.
   - The script will run `VGAudiocli.exe` to convert each file.

4. **Stop the Process**:

   - You can stop entering URLs by simply pressing Enter when asked for another URL.

## Troubleshooting

- Ensure that `ffmpeg` is in the same directory as the script.
- Make sure `yt-dlp` is updated to the latest version for compatibility.
- If any errors occur while executing the commands, check the output for error messages for troubleshooting.
- If the script is not executed where the script is located at, it will not recognise the .exe of VGAudioCLI, so just make sure you are in the directory of the script and the VGAudioCLI.exe.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
