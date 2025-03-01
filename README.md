
# ProxyConfigCollector 🚀🔧

[![GitHub issues](https://img.shields.io/github/issues/mehrdadmb2/ProxyConfigCollector)](https://github.com/mehrdadmb2/ProxyConfigCollector/issues)
[![GitHub stars](https://img.shields.io/github/stars/mehrdadmb2/ProxyConfigCollector)](https://github.com/mehrdadmb2/ProxyConfigCollector/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mehrdadmb2/ProxyConfigCollector)](https://github.com/mehrdadmb2/ProxyConfigCollector/network)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

**ProxyConfigCollector** is a comprehensive toolkit for downloading, processing, and organizing your proxy configuration files. With a fully automated pipeline—from downloading raw configs to sorting them by protocol—this project helps you keep your proxy settings clean and in order. 🔥💻

---

## Table of Contents 📑
- [Overview](#overview-)
- [Pipeline Overview](#pipeline-overview-)
- [Installation](#installation-)
- [Usage](#usage-)
  - [0. Download and Save Configs](#0-download-and-save-configs-)
  - [1. Remove URL from Files](#1-remove-url-from-files-)
  - [2. Decrypt Configs](#2-decrypt-configs-)
  - [3. Config Format Checker](#3-config-format-checker-)
  - [4. File Cleaner and Combiner](#4-file-cleaner-and-combiner-)
  - [5. Config Sorter](#5-config-sorter-)
- [Dependencies](#dependencies-)
- [Contributing](#contributing-)
- [License](#license-)
- [Contact](#contact-)

---

## Overview ✨

ProxyConfigCollector is designed to simplify the entire process of working with proxy configurations. Whether you're collecting new configs from a list of URLs or cleaning up and sorting existing ones, this toolset provides a modular, easy-to-use pipeline for every step.

---

## Pipeline Overview 🔄

The project consists of **six** Python scripts that run sequentially:

1. **Download and Save Configs**  
   Downloads raw configuration files from a list of URLs provided in `DATA(Urls)/Urls.txt` and saves them in the `configs/` folder. 🌐⬇️

2. **Remove URL from Files**  
   Strips out any leading URL lines from the downloaded files and writes the cleaned content to `configs_without_url/`. ✂️🔗

3. **Decrypt Configs**  
   Attempts to decrypt Base64-encoded config files (if applicable) and saves the output in `decrypted_configs/`. 🔓🔑

4. **Config Format Checker**  
   Validates each decrypted config against a set of supported proxy protocols (vmess, vless, ss, trojan, hysteria, clash, cloak, wireguard, ssr). Valid files are moved to `valid_configs/`, and invalid ones to `invalid_configs/`. ✅❌

5. **File Cleaner and Combiner**  
   Combines individual valid (and invalid) config files into single text files (`combined_valid.txt` and `combined_invalid.txt`) while cleaning up and deleting the originals. 📂🧹

6. **Config Sorter**  
   Reads the combined valid config file and categorizes each configuration into separate files (e.g., `vless.txt`, `trojan.txt`, etc.) in the `separated_configs/` folder. If a config does not match any known protocol, it is stored in `unknown_configs.txt`. 🔀📑

---

## Installation ⚙️

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mehrdadmb2/ProxyConfigCollector.git
   cd ProxyConfigCollector
   ```

2. **Set Up a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** If you encounter errors related to SOCKS support, install:
   >
   > ```bash
   > pip install requests[socks]
   > ```

---

## Usage 🚀

Each step of the pipeline is handled by a dedicated Python script. Run them in the following order:

### 0. Download and Save Configs

- **File:** `0.download_and_save_configs.py.py`
- **Description:** Downloads raw proxy configuration files from a list of URLs.
- **Usage:**

  ```bash
  python 0.download_and_save_configs.py.py
  ```

- **Output:** Files are saved in the `configs/` folder.  
  _Progress is displayed using a progress bar (tqdm) and a final report is printed._

---

### 1. Remove URL from Files

- **File:** `1.remove_url_from_files.py`
- **Description:** Removes any URL line (usually at the top of the file) from each config file.
- **Usage:**

  ```bash
  python 1.remove_url_from_files.py
  ```

- **Output:** Cleaned files are saved in `configs_without_url/`.

---

### 2. Decrypt Configs

- **File:** `2.decrypt_configs.py`
- **Description:** Checks if the config content is Base64 encoded, then decrypts it if necessary.
- **Usage:**

  ```bash
  python 2.decrypt_configs.py
  ```

- **Output:** Decrypted config files are written to the `decrypted_configs/` folder.  
  _Files not matching Base64 format are saved as is with a warning._

---

### 3. Config Format Checker

- **File:** `3.ConfigFormatChecker.py`
- **Description:** Validates the format of each config file against supported protocols.
- **Usage:**

  ```bash
  python 3.ConfigFormatChecker.py
  ```

- **Output:**  
  - Valid configs → `valid_configs/`  
  - Invalid configs → `invalid_configs/`  
  _The script prints progress using a progress bar and final validation stats._

---

### 4. File Cleaner and Combiner

- **File:** `4.FileCleanerAndCombiner.py`
- **Description:** Combines individual valid (and invalid) config files into single files while cleaning up originals.
- **Usage:**

  ```bash
  python 4.FileCleanerAndCombiner.py
  ```

- **Output:**  
  - Combined valid configs: `valid_configs/combined_valid.txt`  
  - Combined invalid configs: `invalid_configs/combined_invalid.txt`  
  _Progress and summary are printed in the console._

---

### 5. Config Sorter

- **File:** `5.ConfigSorterX.py`
- **Description:** Sorts the combined valid configurations into separate files by protocol (e.g., vmess, vless, ss, etc.).
- **Usage:**

  ```bash
  python 5.ConfigSorterX.py
  ```

- **Output:** Sorted configuration files are saved in the `separated_configs/` folder.  
  _A final report detailing processing statistics is printed at the end._

---

## Dependencies 📦

- **Python 3.8+**
- **requests** – for HTTP requests (with SOCKS support via `requests[socks]`)
- **tqdm** – for progress bars
- **concurrent.futures** – for parallel downloads
- **re**, **os**, **json**, **time**, **signal**, **platform** – (standard libraries)

Install all required dependencies with:

```bash
pip install -r requirements.txt
```

---

## Contributing 🤝

Contributions are highly welcome! If you wish to report bugs, request features, or contribute code improvements, please:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request with a detailed description of your changes.

---

## License 📄

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact 📬

- **Mehrdad M.**  
  - GitHub: [@mehrdadmb2](https://github.com/mehrdadmb2)  
  - Email: your.email@example.com

---

> **Happy Proxy Config Collecting!** 🎉🔐  
> _"Keep your proxies clean, sorted, and secure!"_
```
