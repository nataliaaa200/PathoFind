# Project Execution Logbook — PathoFind

## Project Overview
- **Objective:** Benchmarking Clinical mNGS Pathogen Detection in Cerebrospinal Fluid (Reproducing Miller et al., 2019)
- **Dataset:** BioProject PRJNA516289 (NCBI SRA)
- **Reference Paper:** Miller et al. (2019), *Genome Research* (PMID: 30992304)

---

## Benchmark Log

### Entry 001 — Environment & Repository Setup
- **Date:** 2026-09-16
- **Status:** Completed
- **Actions:**
  - Repository structure initialized (`data/`, `results/`, `scripts/`, `logs/`).
  - Conda environment file `environment.yml` created with explicit dependencies.
  - Remote integration with PCSS cluster established.

### Entry 002 — Reference Human Genome (GRCh38) & Test Download
- **Date:** 2026-09-16
- **Status:** In Progress
- **Actions:**
  - Downloading human reference index for Bowtie2 (`GRCh38_noalt_as`).
  - Fetching initial test dataset (`SRR8484832`) via `fasterq-dump`.
