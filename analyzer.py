import re
from collections import Counter

# لیست نمونه از کلمات ایست (Stop Words) زبان فارسی
STOP_WORDS = {
    "و", "در", "به", "از", "که", "این", "را", "با", "است", "برای",
    "آن", "یک", "تا", "بر", "هم", "نیز", "شد", "اما", "یا", "ز"
}

def clean_text(text: str) -> str:
    """حذف علائم نگارشی، ارقام و کاراکترهای غیرحرفی از متن"""
    # نگه‌داشتن حروف فارسی/انگلیسی و فاصله‌ها
    cleaned = re.sub(r"[^\w\s]", " ", text)
    # حذف اعداد
    cleaned = re.sub(r"\d+", " ", cleaned)
    return cleaned

def get_word_frequencies(text: str, top_n: int = 5):
    """پاک‌سازی، حذف کلمات ایست و شمارش بسامد کلمات"""
    cleaned = clean_text(text)
    words = cleaned.split()
    
    # فیلتر کلمات ایست
    filtered_words = [w for w in words if w not in STOP_WORDS]
    
    # شمارش با Counter
    counts = Counter(filtered_words)
    return counts.most_common(top_n)

if name == "__main__":
    sample_text = """
    تن آدمی شریف است به جان آدمیت
    نه همین لباس زیباست نشان آدمیت
    اگر آدمی به چشم است و دهان و گوش و بینی
    چه میان نقش دیوار و میان آدمیت
    """
    
    print("--- پرتکرارترین کلمات معنادار متن ---")
    top_words = get_word_frequencies(sample_text, top_n=3)
    for word, count in top_words:
        print(f"کلمه: «{word}» | تعداد تکرار: {count}")
