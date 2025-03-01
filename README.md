
# ProxyConfigCollector 🚀🔧

[![GitHub issues](https://img.shields.io/github/issues/mehrdadmb2/ProxyConfigCollector)](https://github.com/mehrdadmb2/ProxyConfigCollector/issues)
[![GitHub stars](https://img.shields.io/github/stars/mehrdadmb2/ProxyConfigCollector)](https://github.com/mehrdadmb2/ProxyConfigCollector/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mehrdadmb2/ProxyConfigCollector)](https://github.com/mehrdadmb2/ProxyConfigCollector/network)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

ProxyConfigCollector is a **comprehensive toolset** for managing and processing proxy configuration files!  
It helps you **download**, **decrypt**, **clean**, **validate**, and **sort** your proxy configs with ease. ⚙️💻

---

## Table of Contents 📑
- [Features](#features-)
- [Installation](#installation-)
- [Usage](#usage-)
  - [0. Download and Save Configs](#0-download-and-save-configs-)
  - [1. Remove URL from Files](#1-remove-url-from-files-)
  - [2. Decrypt Configs](#2-decrypt-configs-)
  - [3. Config Format Checker](#3-config-format-checker-)
  - [4. File Cleaner and Combiner](#4-file-cleaner-and-combiner-)
  - [5. Config Sorter](#5-config-sorter-)
- [Contributing](#contributing-)
- [License](#license-)
- [Contact](#contact-)

---

## Features ✨
- **Download configs** from a list of URLs. 🌐⬇️
- **Remove unwanted URLs** from config files. ✂️🔗
- **Decrypt** Base64 encrypted config files automatically. 🔓🔑
- **Validate** config formats (supports vmess, vless, ss, trojan, hysteria, clash, cloak, wireguard, ssr). ✅❌
- **Clean up** and **combine** valid/invalid configs for further processing. 🧹📄
- **Sort** your proxy configs into separate files based on protocol. 📂🔀

---

## Installation ⚙️

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mehrdadmb2/ProxyConfigCollector.git
   cd ProxyConfigCollector
   ```

2. **Install dependencies:**

   Ensure you have Python 3.8 or above installed.  
   It is recommended to use a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

   > **Note:** If you see errors related to SOCKS support, install the additional dependency:
   > ```bash
   > pip install requests[socks]
   > ```

---

## Usage 🚀

Each script in this repository performs a specific task in the configuration processing pipeline:

### 0. Download and Save Configs
- **File:** `0.download_and_save_configs.py.py`
- **Description:** Downloads configuration files from URLs provided in a text file.  
- **Usage:**
  ```bash
  python 0.download_and_save_configs.py.py
  ```
- **Output:** Saves raw config files into the `configs/` folder. 📥

---

### 1. Remove URL from Files
- **File:** `1.remove_url_from_files.py`
- **Description:** Removes the URL line (if present) from the top of each config file.  
- **Usage:**
  ```bash
  python 1.remove_url_from_files.py
  ```
- **Output:** Cleaned config files are saved in the `configs_without_url/` folder. ✂️🚫

---

### 2. Decrypt Configs
- **File:** `2.decrypt_configs.py`
- **Description:** Decrypts Base64 encoded configuration files (if applicable).  
- **Usage:**
  ```bash
  python 2.decrypt_configs.py
  ```
- **Output:** Decrypted config files are saved in the `decrypted_configs/` folder. 🔓📄

---

### 3. Config Format Checker
- **File:** `3.ConfigFormatChecker.py`
- **Description:** Validates the format of each config file, separating valid and invalid ones.  
- **Usage:**
  ```bash
  python 3.ConfigFormatChecker.py
  ```
- **Output:** 
  - Valid configs: `valid_configs/`
  - Invalid configs: `invalid_configs/`  
  ✅❌

---

### 4. File Cleaner and Combiner
- **File:** `4.FileCleanerAndCombiner.py`
- **Description:** Cleans and combines the processed config files into a single file for further processing.  
- **Usage:**
  ```bash
  python 4.FileCleanerAndCombiner.py
  ```
- **Output:** Combined files in respective folders; original files are deleted after combining. 📂🗑️

---

### 5. Config Sorter
- **File:** `5.ConfigSorterX.py`
- **Description:** Sorts and categorizes the valid proxy configurations into separate files based on protocol.  
- **Usage:**
  ```bash
  python 5.ConfigSorterX.py
  ```
- **Output:** Sorted configuration files are saved in the `separated_configs/` folder. 🔀📑

---

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.  
- Open issues for bug reports and feature requests.
- Follow the coding guidelines and add comments where necessary.

---

## License 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact 📬

- **Mehrdad M.**  
  - GitHub: [@mehrdadmb2](https://github.com/mehrdadmb2)
  - Email: your.email@example.com

---

> **Happy Config Collecting!** 🎉💡  
> _"Keep your proxies in order, and your connections secure!"_
```

