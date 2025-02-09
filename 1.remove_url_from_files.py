import os
import re
from tqdm import tqdm

# مسیر پوشه حاوی فایل‌های تکست
input_folder = "I:\\V2ray_col\\Test1\\configs\\"
output_folder = "I:\\V2ray_col\\Test1\\configs_without_url\\"  # مسیر خروجی برای فایل‌های بدون URL

# ایجاد پوشه خروجی در صورت عدم وجود
os.makedirs(output_folder, exist_ok=True)

# الگوی شناسایی URL در خط اول (برای حذف URL)
url_pattern = re.compile(r'^URL: https?://[^\s]+')

# شمارش فایل‌های موفق و ناموفق
success_count = 0
failed_count = 0
failed_files = []

# بررسی هر فایل در پوشه ورودی
for filename in tqdm(os.listdir(input_folder), desc="Processing files", unit="file"):
    file_path = os.path.join(input_folder, filename)

    # بررسی اینکه آیا فایل است
    if os.path.isfile(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

                # بررسی اینکه آیا خط اول یک URL است
                if url_pattern.match(lines[0].strip()):
                    # حذف خط اول (URL)
                    lines.pop(0)

                # ذخیره فایل جدید بدون URL
                output_file_path = os.path.join(output_folder, filename)
                with open(output_file_path, "w", encoding="utf-8") as output_file:
                    output_file.writelines(lines)

            success_count += 1
            print(f"✔️ {filename} processed successfully.")
        except Exception as e:
            failed_count += 1
            failed_files.append(filename)
            print(f"❌ Failed to process {filename}: {e}")

# گزارش نهایی
print("\n🔚 Process complete!")
print(f"✅ Successfully processed {success_count} files.")
print(f"❌ Failed to process {failed_count} files.")

if failed_files:
    print("\n🚫 Failed files:")
    for failed_file in failed_files:
        print(f"   - {failed_file}")
