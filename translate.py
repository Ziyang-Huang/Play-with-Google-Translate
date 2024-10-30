import time

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

except ModuleNotFoundError:
    import os

    os.system("pip install selenium")

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC


def translate(text, source_lang: str = "SECOND", target_lang: str = "zh-CN") -> str:
    translation_url = f"https://translate.google.com/?sl={source_lang}&tl={target_lang}&text={text.replace(' ', '%20')}&op=translate"
    driver.get(translation_url)
    time.sleep(5)  # 确保页面加载

    translated_paragraphs = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, '//span[@jsname="W297wb"]'))
    )

    full_translation = "\n".join(
        [paragraph.text for paragraph in translated_paragraphs]
    )
    return full_translation


options = Options()
options.headless = True
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)


# 设置语言
FIRST = "zh-CN"
SECOND = "en"

# 定义翻译次数
TIMES = 5

# 定义要翻译的文本
TEXT = """
这里是需要翻译的文本。
"""


records = f"原始文本: {TEXT}\n"
print(records, end="")

try:
    for i in range(1, TIMES + 1):
        TEXT = translate(TEXT, FIRST, SECOND)
        record = f"第{i:2}轮翻译: {FIRST} to {SECOND}\n{TEXT}\n\n"
        print(record, end="")
        records += record

        TEXT = translate(TEXT, SECOND, FIRST)
        record = f"第{i:2}轮翻译: {SECOND} to {FIRST}\n{TEXT}\n\n"
        print(record, end="")
        records += record

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()

with open("translation.txt", "w", encoding="utf-8") as f:
    f.write(records)
