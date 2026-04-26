from playwright.sync_api import sync_playwright

def extract_quran_pdf(surah_num):
    url = f"https://quran.com/{surah_num}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print(f"Loading {url}...")
        # FIX 1: Change to "load" instead of "networkidle" and increase timeout to 60 seconds
        page.goto(url, wait_until="load", timeout=60000)
        
        # FIX 2: Manually wait 5 seconds for the Next.js React components to finish mounting
        print("Waiting for React to mount...")
        page.wait_for_timeout(5000) 
        
        print("Scrolling to load all dynamic content...")
        for i in range(10):
            page.evaluate("window.scrollBy(0, 1000);")
            # Use Playwright's built-in wait instead of the time module
            page.wait_for_timeout(1000) 
            
        print("Preparing to print...")
        page.evaluate("window.scrollTo(0, 0);")
        page.wait_for_timeout(2000)
        
        output_file = f"Surah_{surah_num}.pdf"
        print(f"Saving to {output_file}...")
        
        page.pdf(path=output_file, format="A4", print_background=True)
        
        browser.close()
        print("PDF generated successfully!")

if __name__ == "__main__":
    extract_quran_pdf(1)
