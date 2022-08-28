#recreating webscraping
import requests
url = "https://brookpad.com/en-int/products/samsung-np340xla-ka6us-14-64gb-galaxy-book-go-with-snapdragon-silver-2022?variant=43615594545416&utm_source=google&utm_medium=organic&utm_campaign=EFLcomEN+USD&utm_content=Samsung+NP340XLA-KA6US+14%22+64GB+Galaxy+Book+Go+with+Snapdragon+-+Silver+%282022%29"
page = requests.get(url)

Output:
https://brookpad.com/en-int/products/samsung-np340xla-ka6us-14-64gb-galaxy-book-go-with-snapdragon-silver-2022?variant=43615594545416&utm_source=google&utm_medium=organic&utm_campaign=EFLcomEN+USD&utm_content=Samsung+NP340XLA-KA6US+14%22+64GB+Galaxy+Book+Go+with+Snapdragon+-+Silver+%282022%29
