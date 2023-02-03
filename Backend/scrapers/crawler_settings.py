class Settings:
    def get_company_tickers():
        """
        Returns a zip object of (company, ticker) for each currently supported security.
        """
        tickers = ["TSLA", "MSFT", "AMZN", "AAPL", "GOOGL", "NVDA", "META", "IBM"]
        companies = ["tesla", "microsoft", "amazon", "apple", "google", "nvidia", "meta", "IBM"]
        return zip(companies, tickers)
    
    def get_sources():
        """
        Returns a list of all scraped news sources.
        """
        return ["wsj", "CBNC", "barrons", "bberg", "yahoo"]
    
    def get_database():
        """
        Returns file location of database.
        """
        return "../Backend/ticker_info.db"
    
    def get_keywords():
        """
        Returns a dictionary, with TICKER:[KEYWORD] entries to validate headline relevance.
        """
        return {
            "TSLA": ['tesla', 'elon', 'musk'],
            "MSFT": ['office', 'microsoft'],
        }