import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

COOKIE_FOLDER: str = "./Cookie/no_cookies.crx"


def search_genre(artist: str, song_name: str) -> [str]:
    base_url = "https://www.chosic.com/music-genre-finder/"

    options = webdriver.ChromeOptions()
    options.add_extension(COOKIE_FOLDER)
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")  # For resource constraints
    options.add_argument("--no-sandbox")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get(base_url)
    try:
        # Wait for the page to load
        search_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "search-word"))
        )

        query = f"{song_name} {artist}"

        # Fill in the search input and simulate pressing Enter
        search_input.send_keys(query)
        dropdown = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "form-suggestions"))
        )

        # Locate the first result within the dropdown and click it
        first_result = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#form-suggestions .span-class"))
        )
        first_result.click()

        # Wait for the spotify tags section to appear
        spotify_result = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "spotify-result"))
        )

        # Locate the tag cloud within the spotify-result
        tag_cloud = spotify_result.find_element(By.CSS_SELECTOR, ".pl-tags.tagcloud")

        # Extract all genre links
        genre_elements = tag_cloud.find_elements(By.TAG_NAME, "a")
        genres = [genre.text for genre in genre_elements]

        return genres

    except TimeoutException:
        print("[ChosicScraper]: Loading took too much time!")

    except NoSuchElementException as e:
        print("[ChosicScraper]: Element not found: " + str(e))

    driver.quit()
    return []


def main():
    genre = search_genre("Tupac", "hit em up")
    print(genre)


if __name__ == "__main__":
    main()