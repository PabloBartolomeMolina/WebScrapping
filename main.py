import csvLocal
import scrapping

URL_example = "https://racingnews365.com/every-world-champion-in-formula-1-history"


def main():
    scrapping.webScrapping_Table(URL_example)


if __name__ == "__main__":
    main()
