
# Sh
Sh is a minimal shell scripting language with a very few number of commands
## How to set it up?
Clone the git repository
`git clone https://github.com/pranavbaburaj/sh.git`
and run

- Create an app named data
`python -B main.py new data`
- Run the app
- ```python -B main.py run data```

## How to use it ?
All the commands that you can use with sh are listed down below

-  Create a new project
	```python -B main.py new <project-name>```
 - Run the project
	 if you are on the parent directory run
	 ```python -B main.py run <project-name>```
	 if you are on the project directory , run:
	 ```python -B main.py run .```
 - Download packages
		Apped the url in to the `packages` field in the `<project-name>.json` file . get into the project directory
		and run `python -B main.py get . `
		You will see the package in the `<project-name>/mod` directory
	
### Shell commands
 - Get the list of files and folder : `ls` or `dir`
 - Open up the current directory in file explorer : `explorer` or `file`
 - Get into a directory : `cd:<dir-name>`
 - Remove a directory or file : `rm:<file-name>`
 - Create a directory : `mkdir:<dir-name>`
 - Create a file : `touch:<file-name>`
 - Search duckduckgo : `search:<search>`
 Example : `search:hello-world`
 spaces are represented by (-)
 - say something : `say:<text-to-say>` 
 - Current working directory : `path` or `cwd`
 - The directory basename : `directory`

<hr>
<div align="center">
if you find any issues, report <a href="https://github.com/pranavbaburaj/sh/issues">
here</a>
</div>
<hr>
<div align="center">
  Created by <a style="text-decoration:none;" href="https://github.com/pranavbaburaj">Pranav Baburaj</a>
</div>
