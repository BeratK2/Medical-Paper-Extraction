from paperscraper.pubmed import get_and_dump_pubmed_papers
from paperscraper.pdf import save_pdf_from_dump
proton = ['Proton Therapy']
query = [proton]

get_and_dump_pubmed_papers(query, output_filepath='proton2.jsonl')

# Save PDFs/XMLs in current folder and name the files by their DOI
#save_pdf_from_dump('proton2.jsonl', pdf_path='.', key_to_save='doi')