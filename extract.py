from playwright.sync_api import sync_playwright
import time

def extract_quran_pdf(surah_num):
    url = f"https://quran.com/{surah_num}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print(f"Loading {url}...")
        page.goto(url, wait_until="networkidle")
        
        # Scroll down the page slowly to force React to load all Ayahs
        print("Scrolling to load all dynamic content...")
        for i in range(10):
            page.evaluate("window.scrollBy(0, 1000);")
            time.sleep(1)
            
        # Scroll back to the top before printing
        page.evaluate("window.scrollTo(0, 0);")
        time.sleep(2)
        
        output_file = f"Surah_{surah_num}.pdf"
        print(f"Saving to {output_file}...")
        
        # Print the exact CSS layout and background colors
        page.pdf(path=output_file, format="A4", print_background=True)
        
        browser.close()
        print("PDF generated successfully!")

if __name__ == "__main__":
    # Extract Surah 1 (Al-Fatihah). Change this number for other Surahs.
    extract_quran_pdf(1)

