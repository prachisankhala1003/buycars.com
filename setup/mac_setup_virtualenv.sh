#!/bin/bash

# Define the Python version you want to install
PYTHON_VERSION="3.12.1"

# Determine the directory of the current script
DIR=$(dirname "${BASH_SOURCE[0]}")
DIR=$(realpath "${DIR}")
BYellow='\033[1;93m'
On_Black='\033[40m'
NC='\033[0m'

# Change to the parent directory of the script's location
cd "$DIR"
cd ./..

# Set the environment path to the parent directory
ENV_DIR=$(pwd)

# Check if pyenv is installed, and install if it's not
check_dir="/Users/$USER/.pyenv"
if [ ! -d "$check_dir" ]; then
  echo -e "${BYellow}${On_Black}Installing pyenv since it was not found...${NC}"
  curl https://pyenv.run | bash
fi

# Add pyenv initialization to shell configuration files
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Reload shell configuration files
echo " "
echo " "
echo "${BYellow}${On_Black}Reloading RC files...${NC}"
source ~/.bashrc
source ~/.zshrc

# Install the specified Python version
echo " "
echo " "
echo "${BYellow}${On_Black}Installing Python $PYTHON_VERSION...${NC}"
pyenv install "$PYTHON_VERSION"

# Install virtualenv
echo " "
echo " "
echo "${BYellow}${On_Black}Installing virtual environment...${NC}"
~/.pyenv/versions/"$PYTHON_VERSION"/bin/python -m pip install virtualenv

# Create the virtual environment in the parent directory
echo " "
echo " "
echo "${BYellow}${On_Black}Creating virtual environment...${NC}"
~/.pyenv/versions/"$PYTHON_VERSION"/bin/python -m venv "$ENV_DIR/env"

# Activate the virtual environment
echo " "
echo " "
echo "${BYellow}${On_Black}Activating virtual environment...${NC}"
source "$ENV_DIR/env/bin/activate"

# Check if the OS is macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
  # If macOS, remove pywin32 from requirements.txt if it exists
  sed -i '' '/pywin32/d' "$DIR/requirements.txt"
fi

# Install the required packages from requirements.txt located in the Commands folder
echo " "
echo " "
echo "${BYellow}${On_Black}Installing virtual environment packages...${NC}"
pip install -r "$DIR/requirements.txt"

# Install local packages
echo " "
echo " "
echo "${BYellow}${On_Black}Installing local packages...${NC}"
echo "$ENV_DIR" > "$ENV_DIR/env/lib/python${PYTHON_VERSION}/site-packages/localpackages.pth"
