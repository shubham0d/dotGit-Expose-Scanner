# dotGit-Expose-Scanner
Tool to scan for domains having .git repos exposed publically

### Usage
To run the program `python script.py <filename>`

### Working

Website hosted from git directory have risk to expose .git repo to public.\n
This tool will check different domains passed as argument if they have .git \n
exposed or not. \n
We are verifying this by trying to read `.git/HEAD` for the input domain.
