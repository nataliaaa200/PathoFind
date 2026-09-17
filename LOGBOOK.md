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
