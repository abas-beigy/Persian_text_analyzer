def analyze_text(text):
    """
    تحلیل آماری و سبک‌شناختی متن و شعر فارسی
    خروجی‌ها:
    - تعداد ابیات (خطوط)
    - تعداد کل کلمات
    - تعداد کل حروف
    - میانگین طول کلمات
    - شاخص تنوع واژگانی (TTR)
    """
    if not text.strip():
        return 0, 0, 0, 0, 0

    lines = text.strip().split('\n')
    words = text.split()
    
    total_chars = sum(len(word) for word in words)
    num_words = len(words)
    num_lines = len(lines)
    
    avg_word_length = total_chars / num_words if num_words > 0 else 0
    
    unique_words = set(words)
    ttr = len(unique_words) / num_words if num_words > 0 else 0
    
    return num_lines, num_words, total_chars, avg_word_length, ttr
