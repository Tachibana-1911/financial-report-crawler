from src.scraper import scrape_pdfs_from_ir

if __name__ == "__main__":
    company_name = "cover"
    base_url = "https://cover-corp.com/ir/library"
    save_folder = f"data/{company_name}_pdfs"

    scrape_pdfs_from_ir(base_url, save_folder)