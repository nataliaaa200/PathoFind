# PathoFind Project Logbook

## Date: 17.09.2026
**Author:** Natalia (`nati22`)
**Cluster:** PCSS Eagle (`eagle`)
**Environment:** `pathofind` (/mnt/storage_6/project_data/pl1038-01/nati22/miniconda3/envs/pathofind)

---

### Accomplishments Today:
- **Storage Optimization:** Solved disk quota issues by creating a clean symlink architecture between scratch working space (`/scratch/PathoFind`) and persistent high-capacity storage (`/project_data/PathoFind/`).
- **Symlink Map Verified:**
  - `data/raw/` -> `/project_data/.../data/raw`
  - `data/host_depleted/` -> `/project_data/.../data/host_depleted`
  - `data/metadata/` -> `/project_data/.../data/metadata`
  - `data/ref_genomes/` -> `/project_data/.../ref_genomes`
  - `results/` -> `/project_data/.../results` (includes `qc`, `kraken2`, `bracken`, `r_analysis`, `multiqc`)
  - `logs/` -> `/project_data/.../logs`
- **Reference Genomes:** Downloaded and extracted human reference index `GRCh38` for Bowtie2.
- **Environment:** Verified active `pathofind` conda environment.

---

### Plan for Next Session:
1. Activate environment: `conda activate pathofind`.
2. Download test fastq samples (1-2 runs from PRJNA516289) into `data/raw/` using `fasterq-dump`.
3. Fetch MiniKraken2 test database into `data/ref_genomes/`.
4. Run dry-run and test batch pipeline execution.

---

##Date: 18.09.2026  
**Author:** Natalia (nati22)  
**Cluster:** PCSS Eagle (eagle)  
**Environment:** pathofind (`/mnt/storage_6/project_data/pl1038-01/nati22/miniconda3/envs/pathofind`)

###Accomplishments Today:

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

## Date: September 19, 2026
**Author:** Natalia (`nati22`)
**Cluster:** PCSS Eagle (`eagle`)
**Environment:** `pathofind`

---

### Accomplishments Today:
- **Raw Data Verification:** Checked and confirmed input raw FASTQ files (`SRR8580951.fastq.gz`, `SRR8580952.fastq.gz`) in `data/raw/`.
- **Host Depletion (Bowtie2):** 
  - Successfully executed Bowtie2 against the human reference genome (`GRCh38`) for sample `SRR8580952`.
  - Generated cleaned, host-depleted paired-end reads:
    - `data/host_depleted/SRR8580952_clean_1.fastq.gz`
    - `data/host_depleted/SRR8580952_clean_2.fastq.gz`
- **Pipeline Milestone:** Completed quality control and host depletion phases. Data is fully prepped for taxonomic classification.

---

### Next Steps for Today:
1. Run **Kraken2** taxonomic classification on the cleaned reads (`SRR8580952`) using the reference database.
2. Estimate species-level abundance using **Bracken**.
3. Inspect and parse the generated Kraken2/Bracken reports.
