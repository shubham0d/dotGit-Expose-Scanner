# dotGit-Expose-Scanner
Tool to scan for domains having .git repos exposed publically

### Usage
To run the program `python script.py <filename>`

### Working

Website hosted from git directory have risk to expose .git repo to public.<br />
This tool will check different domains passed as argument if they have .git <br />
exposed or not. <br />
We are verifying this by trying to read `.git/HEAD` for the input domain.
