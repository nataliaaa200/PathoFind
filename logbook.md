
---

Date: 18.09.2026
Author: Natalia (nati22)
Cluster: PCSS Eagle (eagle)
Environment: pathofind (/mnt/storage_6/project_data/pl1038-01/nati22/miniconda3/envs/pathofind)

Accomplishments Today:

1. Repository & Version Control Setup:
   - Configured `.gitignore` to prevent tracking large bioinformatics outputs (`.fastq.gz`, `.bam`, `.k2d`, `data/`).
   - Defined Conda environment (`environment.yml`) containing `sra-tools`, `fastp`, `bowtie2`, `samtools`, `kraken2`, `bracken`, and `pigz`.
   - Updated `README.md` and pushed code/configuration files to GitHub.

2. Metadata Processing & Ground Truth Mapping:
   - Fetched NCBI SRA metadata (`SRA_RunInfo.csv`) and clinical records (`Supplemental Table S2`) for BioProject PRJNA516289.
   - Developed `scripts/00_prepare_metadata.py` to trim `_DNA`/`_RNA` suffixes and merge diagnostic labels with SRA run IDs.
   - Verified metadata integration: mapped 190 SRR runs across 95 patient samples into `data/metadata/samples_ground_truth.csv`.

Plan for Next Session:

1. Download representative test FASTQ files (e.g., SRR8580952, SRR8580951) using `fasterq-dump` and compress with `pigz`.
2. Execute quality control and adapter trimming using `fastp`.
3. Perform host depletion against GRCh38 using `bowtie2`.
4. Run taxonomic classification via `kraken2` / `bracken`.
