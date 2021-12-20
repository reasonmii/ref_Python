'''
Tip: How to Set up Python 3 and pip 3 as default
https://www.30secondsofcode.org/articles/s/setup-python3-pip3-as-default

※ One of the most common headaches when working with Python is
   having to ★"remember to use Python 3.x" instead of Python 2.x

1) Figure out where each one is installed using the which command
- Make a note of each response,
  so that you can add the paths as aliases to your shell environment's configuration file
'''

which python3   # /usr/local/bin/python3
which pip3      # /usr/local/bin/pip3

'''
2) Use echo to add a line for each one
  to either .zshrc or .bashrc depending on your environment
'''

# Linux or other bash environment
echo "alias python=/usr/local/bin/python3" >> ~/.bashrc
echo "alias pip=/usr/local/bin/pip3" >> ~/.bashrc

# Mac OS or other zsh environment
echo "alias python=/usr/local/bin/python3" >> ~/.zshrc
echo "alias pip=/usr/local/bin/pip3" >> ~/.zshrc

# You're all done! python and pip are both mapped to their 3.x versions
