![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/1to5pc/python-auth/backend-test.yml?style=for-the-badge&label=Back%20End&logo=github)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/1to5pc/python-auth/github-code-scanning%2Fcodeql?style=for-the-badge&logo=github&label=CodeQL)

[![forthebadge](https://forthebadge.com/images/badges/license-mit.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/0-percent-optimized.svg)](https://forthebadge.com)

# User Authentication System
This Python script provides a simple user authentication system with functionalities to initialize user accounts, test authentication, and manage user data securely.

# Features
- User Initialization: Initialize user accounts with usernames, passwords, and salt for enhanced security.
- Authentication Testing: Test user authentication by providing a username and password.
- Quiet Mode: Enable quiet mode to suppress unnecessary output during authentication testing.
- Configuration Options: Configure parameters such as quiet mode, hashing algorithm, and salt size through a configuration file.
# Setup
1) __Clone the Repository:__ Clone this repository to your local machine.

``` 
git clone https://github.com/1to5pc/python-auth.git
```

2) __Install Dependencies:__ Ensure you have Python installed on your machine.

3) __Configuration:__ Customize the configuration parameters by editing the config.ini file.

# Usage
1) __Initialize User Accounts:__

Run the script and select the option to initialize user accounts. Follow the prompts to create user accounts with usernames and passwords.

2) __Test Authentication:__

Test user authentication by providing a username and password. Choose whether to enable quiet mode to suppress output during testing.

3) __Exit:__

Exit the program when finished.

# Configuration Options
- __Quiet Mode:__ Set to suppress unnecessary output during authentication testing.
- __Hashing Algorithm:__ Configure the hashing algorithm for password hashing (default is SHA256).
- __Salt Size:__ Set the size of the salt used for password hashing (default is 8).
# Contributing
Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.

> [!NOTE]
> Ensure pull requests are directed at the **development** branch.

# License
This project is licensed under the MIT License.

Feel free to customize and expand this documentation further based on your preferences and additional functionalities!
