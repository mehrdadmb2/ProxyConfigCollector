import requests
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# مسیر فایل ورودی شامل URLها
input_file = "DATA(Urls)\\Urls.txt"

# مسیر ذخیره فایل‌های خروجی
output_folder = "configs\\"  # مسیر مورد نظر را اینجا تغییر دهید

# ایجاد پوشه خروجی در صورت عدم وجود
os.makedirs(output_folder, exist_ok=True)

# خواندن لیست URLها از فایل
try:
    with open(input_file, "r", encoding="utf-8") as file:
        urls = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print(f"❌ Error: Input file '{input_file}' not found.")
    exit(1)

# شمارنده برای نام‌گذاری فایل‌ها
success_count = 0
failed_count = 0
failed_urls = []

# تابع برای پردازش یک URL
def process_url(url):
    global success_count, failed_count
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.text.strip():
            file_path = f"{output_folder}{success_count}.txt"
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"URL: {url}\n\n{response.text}")
            success_count += 1
        else:
            failed_count += 1
            failed_urls.append(url)
    except requests.RequestException:
        failed_count += 1
        failed_urls.append(url)

# استفاده از ThreadPoolExecutor برای پردازش همزمان
with ThreadPoolExecutor(max_workers=10) as executor:
    # پردازش URLها به صورت موازی
    list(tqdm(executor.map(process_url, urls), total=len(urls), desc="Processing URLs"))

# گزارش نهایی
print(f"✅ Successfully downloaded {success_count} configurations.")
print(f"❌ Failed to download {failed_count} configurations.")
if failed_urls:
    print("🚫 Failed URLs:")
    for failed_url in failed_urls:
        print(f"   - {failed_url}")
