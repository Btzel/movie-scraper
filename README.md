# Empire's Top 100 Movies Scraper
A Python web scraping application that extracts and formats Empire Magazine's top 100 movies list using BeautifulSoup4.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-Scraping-red)
![Movies](https://img.shields.io/badge/Movies-Top100-green)
![Data](https://img.shields.io/badge/Data-Processing-orange)

## 🎯 Overview
This project creates a data extraction tool that:
1. Scrapes movie rankings
2. Processes HTML content
3. Extracts movie titles
4. Formats release years
5. Creates organized output

## 🎬 Application Features
### Web Scraping
- BeautifulSoup4 integration
- HTML parsing
- Content extraction
- Error handling
- Automated processing

### Data Processing
- Title extraction
- Year formatting
- Ranking organization
- File output generation
- Data structuring

## 🔧 Technical Components
### Web Scraping System
```python
webpage = BeautifulSoup(response.text,"html.parser")
span_content = webpage.find_all(name="span", class_="content_content__i0P3p")
h_content = [span.find_all(name="h2") for span in span_content 
            if span.find_all(name="h2") != []]
```

### Key Features
1. **Content Extraction**
   - HTML parsing
   - Element selection
   - Data filtering
   - Text processing

2. **Data Organization**
   - Ranking preservation
   - Title formatting
   - Year extraction
   - File output

3. **Error Handling**
   - Request validation
   - Content verification
   - Response checking
   - Data validation

## 💻 Implementation Details
### Class Structure
- BeautifulSoup for parsing
- Requests for web access
- File handling for output
- String processing

### Data Management
- Movie title extraction
- Release year parsing
- Ranking organization
- Text file generation

## 🚀 Usage
1. Install required packages:
```bash
pip install requests beautifulsoup4
```

2. Run the scraper:
```bash
python main.py
```

3. Check output:
```bash
cat movies.txt
```

## 🎯 Scraping Rules
1. Access Empire website
2. Extract movie data
3. Process content
4. Format output
5. Save to file

## 🛠️ Project Structure
```
movie-scraper/
├── main.py           # Scraping script
└── movies.txt        # Output file
```

## 📊 Features
### Input Processing
- Website access
- HTML parsing
- Element selection
- Content extraction

### Output Management
- Ranking preservation
- Title formatting
- Year organization
- File generation

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL