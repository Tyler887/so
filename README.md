# Stack Overflow Command Line
This is the Stack Overflow CLI, which Stack Overflow refused to write.
I had to write it because I'm a developer, but `stackoverflow.com` is going
weird and I almost have no way to do SO-related stuff from my CLI.
## Features
* Use a small wysiwyg editor (`micro`)
* Works properly in scripts
* Runs on any operating system (Windows, macOS, Un\*x)
## Usage
### Log in
[Authenticate](https://api.stackexchange.com/docs/authentication) your Stack Overflow account with OAuth 2.0 to use SE API v2:
```shell
$ so login
# Logging in...
# Logged in as tyler2213!
```
### Ask a question
Ask a new question and it will appear on Stack Overflow:
```shell
$ so question ask
# (?) Title (15+ chars): Python has problem
# /!\ WARNING: Many questions with a similar title received downvotes
#              or requests for feedback. Please update your title.
# (?) Title (15+ chars): SyntaxError: "(" was never closed
# (?) Body [Press enter to launch micro]
# (?) Tags (up to 5, at least 1 required): [python] [python-3.10] [brackets]
# (i) Asked question successfully.
# (?) Open the question in your browser (y/n)? Yes
# (i) Opening...
# --> xdg-open stackoverflow.com/questions/XXXXXXXXX/syntaxerror-(-was-never-closed
```
If `micro` was not found, this throws an error. Install the `micro` editor
if you do not have it, as this app depends on it.
