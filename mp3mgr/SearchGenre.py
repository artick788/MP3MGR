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
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(base_url)

    genre: [str] = []
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

        # Wait for the page to load
        spotify_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "spotify-tags"))
        )

        # The spotify box contains a list of genres
        spotify_result = spotify_box.find_element(By.CLASS_NAME, "spotify-result")
        tag_cloud = spotify_result.find_element(By.CSS_SELECTOR, ".p1-tags.tagcloud")


        print("Done")
        time.sleep(5)

    except TimeoutException:
        print("[ChosicScraper]: Loading took too much time!")

    except NoSuchElementException as e:
        print("[ChosicScraper]: Element not found: " + str(e))

    driver.quit()
    return genre


def main():
    genre = search_genre("Skrillex", "Bangarang")
    print(genre)


if __name__ == "__main__":
    main()