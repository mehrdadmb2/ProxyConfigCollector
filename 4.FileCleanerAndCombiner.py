import os

# مسیر پوشه‌ها
valid_output_folder = "I:\\V2ray_col\\Test1\\valid_configs\\"  # پوشه فایل‌های تایید شده
invalid_output_folder = "I:\\V2ray_col\\Test1\\invalid_configs\\"  # پوشه فایل‌های غیرمعتبر

# فایل خروجی که تمام محتوای فایل‌ها در آن ذخیره می‌شود
valid_output_txt = os.path.join(valid_output_folder, "combined_valid.txt")
invalid_output_txt = os.path.join(invalid_output_folder, "combined_invalid.txt")

# تابع برای ترکیب محتوای فایل‌ها و نوشتن گزارش پیشرفت
def combine_files_to_txt(folder_path, output_txt_path, folder_type):
    try:
        # شمارش فایل‌های موجود در پوشه
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        total_files = len(files)
        files_processed = 0

        with open(output_txt_path, "w", encoding="utf-8") as output_file:
            for filename in files:
                file_path = os.path.join(folder_path, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read().strip()
                        # نوشتن محتوای فایل در فایل خروجی
                        output_file.write(content + "\n\n")  # اضافه کردن دو خط جدید بعد از هر فایل

                    # حذف فایل بعد از اضافه کردن محتوا به فایل نهایی
                    os.remove(file_path)
                    files_processed += 1
                    # گزارش پیشرفت
                    print(f"✅ {filename} added to {output_txt_path} and deleted. Progress: {files_processed}/{total_files}")

                except Exception as e:
                    print(f"❌ Failed to read or delete {filename}: {e}")

        # نوشتن گزارش نهایی در کنسول
        print(f"\n📂 Operation Summary for {folder_type} files:")
        print(f"Total files in {folder_type} folder: {total_files}")
        print(f"Successfully processed files: {files_processed}")
        print(f"Failed to process files: {total_files - files_processed}")

    except Exception as e:
        print(f"❌ Failed to create or write to {output_txt_path}: {e}")


# ترکیب فایل‌های valid
combine_files_to_txt(valid_output_folder, valid_output_txt, "Valid")

# ترکیب فایل‌های invalid
combine_files_to_txt(invalid_output_folder, invalid_output_txt, "Invalid")

print("\n📂 Files have been combined, original files deleted, and reports printed in the console.")
