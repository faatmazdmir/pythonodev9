import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("Books_Data_Clean.csv")
print(data.head())
print(data.shape)
print(data.info())
print(data.isnull().sum())
print(data.columns)
print(data["language_code"].unique())
print(data["Author_Rating"].unique())
print(data["genre"].unique())
print(data["units sold"].mean())
print(data["sale price"].mean())
print(data["Book_average_rating"].mean())
print(data["Author_Rating"].value_counts())
print(data["language_code"].value_counts())

columns = list(data.columns)
print(columns)

max_sale_price = data["sale price"].max()
min_sale_price = data["sale price"].min()
max_book_average_rating = data["Book_average_rating"].max()
min_book_average_rating = data["Book_average_rating"].min()
print(max_sale_price)
print(min_sale_price)
print(max_book_average_rating)
print(min_book_average_rating)

print(data[data["Author"] == "Stephen King"].value_counts())

most_common_language_code = data['language_code'].mode()[0]
print(f"Most common language code: {most_common_language_code}")

author_rating_distribution = data['Author_Rating'].value_counts()
author_rating_distribution.plot(kind='pie', autopct='%1.1f%%')
plt.title("Distribution of Author Ratings")
plt.ylabel('')
plt.show()

genre_sale_price = data.groupby("genre")[["sale price"]].mean().reset_index()
print(genre_sale_price)
plt.figure(figsize=(10,5))
plt.bar(x = "genre",height = "sale price",data = genre_sale_price)
plt.xlabel("Genre")
plt.ylabel("Sale Price")
plt.title("Sale Price by Genre")
plt.show()

genre_counts = data["genre"].value_counts()
print(genre_counts)
plt.figure(figsize=(8, 6))
genre_counts.plot(kind='bar')
plt.title("Genre Counts")
plt.xticks(rotation=0)
plt.show()

genre_gross_sales = data.groupby("genre")[["gross sales"]].sum().reset_index()
print(genre_gross_sales)
plt.figure(figsize=(10,5))
plt.bar(x = "genre",height = "gross sales",data = genre_gross_sales)
plt.xlabel("Genre")
plt.ylabel("Gross Sales")
plt.title("Gross Sales by Genre")
plt.show()

books = data.groupby("Author_Rating")[["Book_average_rating"]].mean().reset_index()
print(books)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Author_Rating', y='Book_average_rating', data=books)
plt.title('Book Average Rating by Author Rating')
plt.xlabel('Author Rating')
plt.ylabel('Book Average Rating')
plt.show()

books_genre = data.groupby(["Author_Rating","genre"])[["Book_average_rating"]].mean().reset_index()
print(books_genre)