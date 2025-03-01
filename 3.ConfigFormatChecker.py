import os
import re
from tqdm import tqdm

# مسیر پوشه حاوی فایل‌ها
input_folder = "decrypted_configs\\"  # مسیر پوشه ورودی
valid_output_folder = "valid_configs\\"  # مسیر خروجی برای فایل‌های تایید شده
invalid_output_folder = "invalid_configs\\"  # مسیر خروجی برای فایل‌های غیر معتبر

# ایجاد پوشه‌های خروجی در صورت عدم وجود
os.makedirs(valid_output_folder, exist_ok=True)
os.makedirs(invalid_output_folder, exist_ok=True)

# الگوهای شناسایی URL (برای حذف URL از ابتدا)
url_pattern = re.compile(r'^https?://[^\s]+')

# الگوهای شناسایی فرمت‌های معتبر (vmess، vless، ss، trojan، hysteria، cloak، clash، wireguard، ssr)
valid_formats = [
    r"^vmess://",
    r"^vless://",
    r"^ss://",
    r"^trojan://",
    r"^hysteria://",
    r"^clash://",
    r"^cloak://",
    r"^wireguard://",
    r"^ssr://"
]

# شمارش فایل‌های تایید شده و رد شده
valid_count = 0
invalid_count = 0

# بررسی هر فایل در پوشه ورودی
for filename in tqdm(os.listdir(input_folder), desc="Checking files", unit="file"):
    file_path = os.path.join(input_folder, filename)

    # بررسی اینکه آیا فایل است
    if os.path.isfile(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()

                # حذف URL از ابتدای محتوا
                content = re.sub(url_pattern, "", content).strip()

                # حذف محتوای اضافی از فایل‌های تایید نشده
                if content.startswith("#"):
                    # حذف تمامی خطوطی که با "#" شروع می‌شوند (حذف توضیحات اضافی)
                    content = "\n".join([line for line in content.split("\n") if not line.startswith("#")]).strip()

                # بررسی اینکه آیا فرمت معتبر است
                if any(re.match(fmt, content) for fmt in valid_formats):
                    valid_count += 1
                    # ذخیره فایل تایید شده در پوشه valid_configs
                    output_file_path = os.path.join(valid_output_folder, filename)
                    with open(output_file_path, "w", encoding="utf-8") as output_file:
                        output_file.write(content)

                    print(f"✅ {filename} is valid and saved.")
                else:
                    invalid_count += 1
                    # ذخیره فایل غیر معتبر در پوشه invalid_configs
                    invalid_file_path = os.path.join(invalid_output_folder, filename)
                    with open(invalid_file_path, "w", encoding="utf-8") as invalid_file:
                        invalid_file.write(content)

                    print(f"❌ {filename} is invalid format.")
        except Exception as e:
            invalid_count += 1
            print(f"❌ Failed to read {filename}: {e}")

# گزارش نهایی
print(f"\n🔚 File format checking complete!")
print(f"✅ Successfully validated {valid_count} files.")
print(f"❌ {invalid_count} files are invalid.")
