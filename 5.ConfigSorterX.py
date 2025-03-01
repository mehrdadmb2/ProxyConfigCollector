import re
import os
import time

# مسیر فایل ورودی
input_file = "valid_configs\\combined_valid.txt"

# پوشه ذخیره خروجی‌ها
output_folder = "separated_configs"

# اطمینان از اینکه پوشه خروجی وجود دارد
os.makedirs(output_folder, exist_ok=True)

# تعریف فرمت‌های معتبر و نام فایل‌های خروجی
valid_formats = {
    r"^vmess://": "vmess.txt",
    r"^vless://": "vless.txt",
    r"^ss://": "shadowsocks.txt",
    r"^trojan://": "trojan.txt",
    r"^hysteria://": "hysteria.txt",
    r"^hysteria2://": "hysteria2.txt",
    r"^clash://": "clash.txt",
    r"^cloak://": "cloak.txt",
    r"^wireguard://": "wireguard.txt",
    r"^ssr://": "ssr.txt"
}

# دیکشنری برای ذخیره کانفیگ‌های جدا شده
separated_configs = {key: [] for key in valid_formats.values()}
unrecognized_configs = []  # لیست برای کانفیگ‌های ناشناس

# خواندن فایل ورودی
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# تعداد کل کانفیگ‌ها
total_configs = len(lines)
if total_configs == 0:
    print("[INFO] No configurations found in the input file.")
    exit()

print(f"[INFO] Total configurations found: {total_configs}")
print("[INFO] Starting the categorization process...\n")

# شروع زمان پردازش
start_time = time.time()

# پردازش هر خط و تشخیص نوع پروتکل
for index, line in enumerate(lines, start=1):
    line = line.strip()
    categorized = False

    for pattern, filename in valid_formats.items():
        if re.match(pattern, line):
            separated_configs[filename].append(line)
            categorized = True
            break  # پس از تشخیص، دیگر نیازی به بررسی بقیه الگوها نیست

    if not categorized:
        unrecognized_configs.append(line)  # ذخیره کانفیگ‌های ناشناس

    # گزارش پیشرفت هر 500 کانفیگ
    if index % 500 == 0 or index == total_configs:
        print(f"[PROGRESS] Processed {index}/{total_configs} configurations...")

# ذخیره کانفیگ‌های جدا شده در فایل‌های مربوطه
for filename, configs in separated_configs.items():
    if configs:
        output_path = os.path.join(output_folder, filename)
        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write("\n".join(configs))
        print(f"[✅] {len(configs)} configs saved in {filename}")

# ذخیره کانفیگ‌های ناشناس (در صورت وجود)
if unrecognized_configs:
    unknown_file = os.path.join(output_folder, "unknown_configs.txt")
    with open(unknown_file, 'w', encoding='utf-8') as out_file:
        out_file.write("\n".join(unrecognized_configs))
    print(f"[⚠️] {len(unrecognized_configs)} unrecognized configs saved in unknown_configs.txt")

# پایان زمان پردازش
end_time = time.time()
duration = end_time - start_time

# گزارش نهایی
print("\n================ FINAL REPORT ================")
processed_configs = sum(len(configs) for configs in separated_configs.values())
print(f"📂 Total Configurations Processed: {total_configs}")
print(f"✅ Successfully Categorized: {processed_configs} ({(processed_configs / total_configs) * 100:.2f}%)")
print(f"⚠️ Unrecognized Configs: {len(unrecognized_configs)} ({(len(unrecognized_configs) / total_configs) * 100:.2f}%)")
print(f"⏳ Total Processing Time: {duration:.2f} seconds")
print("=============================================")
