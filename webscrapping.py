{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "619626c5-cc59-4004-955e-1e423ea50f4e",
   "metadata": {},
   "outputs": [],
   "source": [
    " \n",
    "\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import csv\n",
    "\n",
    " \n",
    "BASE_URL = \"https://books.toscrape.com/catalogue/page-{}.html\"\n",
    "\n",
    " \n",
    "with open(\"books_data.csv\", mode=\"w\", newline=\"\", encoding=\"utf-8\") as file:\n",
    "    writer = csv.writer(file)\n",
    "    writer.writerow([\"Title\", \"Price\"])\n",
    "\n",
    "     \n",
    "    for page in range(1, 6):\n",
    "        url = BASE_URL.format(page)\n",
    "        response = requests.get(url)\n",
    "        soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "\n",
    "        books = soup.find_all(\"article\", class_=\"product_pod\")\n",
    "\n",
    "        for book in books:\n",
    "            title = book.h3.a[\"title\"]\n",
    "            price = book.find(\"p\", class_=\"price_color\").text\n",
    "            writer.writerow([title, price])\n",
    "\n",
    "        print(f\"✅ Page {page} scraped successfully.\")\n",
    "\n",
    "print(\"🎯 Scraping complete. Data saved to books_data.csv\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
