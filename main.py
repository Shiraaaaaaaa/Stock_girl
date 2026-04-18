from src.stock_data_storage import StockDataStorage

storage = StockDataStorage()

storage.fetch_stock("AAPL")
storage.fetch_stock("MSFT")

storage.load_from_csv("AAPL")



print(storage.get_stock("AAPL").head())
storage.clear_data() 