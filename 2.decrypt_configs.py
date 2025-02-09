import base64
import os
import re
from tqdm import tqdm

# مسیر پوشه حاوی فایل‌های تکست
input_folder = "I:\\V2ray_col\\Test1\\configs_without_url\\"
output_folder = "I:\\V2ray_col\\Test1\\decrypted_configs\\"  # مسیر خروجی برای فایل‌های رمزگشایی شده

# ایجاد پوشه خروجی در صورت عدم وجود
os.makedirs(output_folder, exist_ok=True)

# الگو برای تشخیص رشته‌های base64 (که معمولاً برای رمزنگاری استفاده می‌شود)
base64_pattern = re.compile(r'^[A-Za-z0-9+/=]+$')

# شمارش فایل‌های موفق و ناموفق
success_count = 0
failed_count = 0
failed_files = []

# الگوی شناسایی URL (برای حذف URL از ابتدا)
url_pattern = re.compile(r'^https?://[^\s]+')

# بررسی هر فایل در پوشه ورودی
for filename in tqdm(os.listdir(input_folder), desc="Decrypting files", unit="file"):
    file_path = os.path.join(input_folder, filename)

    # بررسی اینکه آیا فایل است
    if os.path.isfile(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()

                # حذف URL از ابتدای محتوا
                content_without_url = re.sub(url_pattern, "", content).strip()

                # بررسی اگر محتوای باقی‌مانده رشته Base64 باشد
                if base64_pattern.match(content_without_url):
                    try:
                        # رمزگشایی Base64
                        decoded_content = base64.b64decode(content_without_url).decode("utf-8")

                        # ذخیره فایل رمزگشایی شده
                        output_file_path = os.path.join(output_folder, filename)
                        with open(output_file_path, "w", encoding="utf-8") as output_file:
                            output_file.write(decoded_content)

                        success_count += 1
                        print(f"🔓 {filename} decrypted successfully.")
                    except Exception as e:
                        failed_count += 1
                        failed_files.append(filename)
                        print(f"❌ Failed to decrypt {filename}: {e}")
                else:
                    # در صورتی که فایل رمزنگاری نشده باشد، فایل اصلی را ذخیره می‌کنیم
                    output_file_path = os.path.join(output_folder, filename)
                    with open(output_file_path, "w", encoding="utf-8") as output_file:
                        output_file.write(content)

                    failed_count += 1
                    failed_files.append(filename)
                    print(f"⚠️ {filename} is not valid Base64. Saved as is.")

        except Exception as e:
            failed_count += 1
            failed_files.append(filename)
            print(f"❌ Failed to read {filename}: {e}")

# گزارش نهایی
print(f"\n🔚 Decryption process complete!")
print(f"✅ Successfully decrypted {success_count} files.")
print(f"❌ Failed to decrypt {failed_count} files.")

if failed_files:
    print("\n🚫 Failed files:")
    for failed_file in failed_files:
        print(f"   - {failed_file}")