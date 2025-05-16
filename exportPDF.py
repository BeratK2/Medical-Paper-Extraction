from paperscraper.pubmed import get_and_dump_pubmed_papers
from paperscraper.pdf import save_pdf_from_dump

# Save PDFs/XMLs in pages folder and name the files by their DOI
save_pdf_from_dump('proton2_first10.jsonl', pdf_path='./papers', key_to_save='doi')