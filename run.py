import os
import subprocess

# Paths to the directories
papers_dir = "papers"  # Folder with all the PDFs
output_dir = "output"  # Folder where images and captions will be stored

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to extract figures from PDFs using pdffigures2
def extract_figures_from_pdfs(papers_dir, output_dir):
    # Iterate through all PDF files in the papers directory
    for filename in os.listdir(papers_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(papers_dir, filename)
            pdf_name = os.path.splitext(filename)[0]  # Strip extension to use as a folder name

            # Create a folder inside the output directory for each PDF's figures
            pdf_output_dir = os.path.join(output_dir, pdf_name)
            if not os.path.exists(pdf_output_dir):
                os.makedirs(pdf_output_dir)

            # Command to run pdffigures2 via sbt
            command = [
                "sbt",
                f'runMain org.allenai.pdffigures2.FigureExtractorBatchCli {pdf_path} -m {pdf_output_dir}/image -d {pdf_output_dir}/data'
            ]

            # Run the command
            try:
                print(f"Extracting figures and captions from: {filename}")
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error processing {filename}: {e}")

# Run the extraction
extract_figures_from_pdfs(papers_dir, output_dir)

print("Figure extraction completed.")
