# AKR -> Image Steganography
# Content of this repo
- ``example_pictures/`` it is a folder with some encoded pictures <br>
- ``steganography_code/`` folder that contains the code itself
# Initial setup
#### Windows setup:
- firstly, cd into project file   
> in``steganography_code`` is the code(i think at least)
- then create a vtirtual enviroment with this command:
 ```shell
$ python -m venv vevn
```
 - now run venv
```shell
$ venv\Scripts\activate.bat
```
> use to correct ``\``, or you will suffer greatly
- now it should display ``venv`` before your current directory.
- And lastly install requered modules:
```shell
$ pip install dependencies
```

* * *
 #### Linux setup:
 - Once again, like in windows, cd to project file (or open terminal in intellij)
 - create an enviroment:
```shell
$ python3 -m venv .venv
```
- activate venv:
```shell
$ source .venv/bin/activate
```
<!---
I hope at least :)
-->
- And lastly install dependencies:
> You should be in the ``.venv/``, if not, cd there
 ```shell
 $ pip install dependencies
 ```
> I found out, that ``tk`` package needs to be installed in the OS itself, so:<br>
> This depends on your linux distro, for example in arch based distros:
> ```shell
> $ Sudo pacman -S tk
> ```
> And if there are any issues with installing required modules, use this command: <br>
> ```shell
> $ pip install -r Requirements.txt
> ```

# What is this repo about?
- This repo is used for final version of our project in AKR.  
- So it is a python code with gui that decodes and encodes string inputs into the image.

