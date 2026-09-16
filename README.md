# Persian_text_analyzer
A Python tool for cleaning perrsian texts, filtering stop_words, and calculating word frequency.
# 📊 تحلیل‌گر بسامد واژگان متون فارسی (Persian Text Frequency Analyzer)

یک ابزار سبک و کارآمد در پایتون برای پیش‌پردازش متن، پاک‌سازی علائم نگارشی، حذف کلمات توخالی (Stop Words) و استخراج کلیدواژه‌های اصلی متن و شعر فارسی.

## 🚀 ویژگی‌ها (Features)
- پاک‌سازی با RegEx: حذف خودکار تمامی علائم نگارشی و کاراکترهای نامربوط بدون آسیب به رسم‌الخط متن.
- فیلتر کلمات ایست (Stop Words Filtering): غربال حروف اضافه و کلمات پرتکرار غیرمحتوایی (مانند: از، به، در، که، و...).
- شمارش بهینه با Counter: پردازش پرسرعت و استخراج دقیق بسامد واژگان به سبک پایتونیک.
- یافتن هسته معنایی متن: شناسایی کلمات کلیدی با متد most_common.

## 🛠 پیش‌نیازها و نصب (Requirements)
این پروژه از کتابخانه‌های استاندارد پایتون استفاده می‌کند و نیاز به نصب هیچ پیش‌نیازی ندارد:
- Python 3.7+
- ماژول‌های re و collections (داخلی پایتون)

## 💻 نحوه استفاده (Usage)
```python
from analyzer import get_word_frequencies

text = """
تن آدمی شریف است به جان آدمیت
نه همین لباس زیباست نشان آدمیت
"""

top_words = get_word_frequencies(text, top_n=3)
print(top_words)
# خروجی: [('آدمیت', 2), ('آدمی', 1), ('شریف', 1)]
