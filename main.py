import requests
from bs4 import BeautifulSoup
WEBSITE_URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(WEBSITE_URL)
response.raise_for_status()
webpage = BeautifulSoup(response.text,"html.parser")
span_content = webpage.find_all(name="span", class_="content_content__i0P3p")
h_content = [span.find_all(name="h2") for span in span_content if span.find_all(name="h2") != []]
strong_content = [h2[0].find_all(name="strong")[0].getText() for h2 in h_content if h2[0].find_all(name="strong") != []][::-1]
with open("movies.txt","w") as file:
    file.writelines(movie.split(sep=")")[0] + "." +
                    movie.split(sep="(")[0].split(sep=")")[1] +
                    movie.split(sep=" ")[-1] + "\n" for movie
                    in strong_content)







