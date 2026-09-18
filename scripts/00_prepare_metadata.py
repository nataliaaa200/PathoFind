import pandas as pd
import numpy as np

# 1. Wczytanie i przygotowanie pliku Excel (Ground Truth)
excel_path = 'data/metadata/supp_gr.238170.118_Supplemental_Table_S2.xlsx'
df_raw = pd.read_excel(excel_path, sheet_name='All Organisms', header=1)

# Czyszczenie nazw kolumn i wypełnianie scalonych komórek
df_raw.columns = [str(c).strip() for c in df_raw.columns]
df_raw['Sample ID'] = df_raw['Sample ID'].ffill()

# Filtrowanie tylko poprawnych próbek MNA_
df_clean = df_raw[df_raw['Sample ID'].str.startswith('MNA_', na=False)].copy()
df_clean['Sample ID'] = df_clean['Sample ID'].str.strip()

print(f"Rekordy w Excelu: {len(df_clean)}")
print(f"Unikalne próbki pacjentów w Excelu: {df_clean['Sample ID'].nunique()}")

# 2. Wczytanie SRA RunInfo i stworzenie bazowego ID do łączenia
sra_path = 'data/metadata/SRA_RunInfo.csv'
df_sra = pd.read_csv(sra_path)

# Usuwamy _DNA / _RNA z końca nazwy SampleName
df_sra['base_sample_id'] = df_sra['SampleName'].str.replace(r'_(DNA|RNA)$', '', regex=True).str.strip()

# 3. Połączenie tabel (Merge)
df_merged = pd.merge(
    df_sra, 
    df_clean, 
    left_on='base_sample_id', 
    right_on='Sample ID', 
    how='inner'
)

print(f"\nUdana integracja!")
print(f"Zmapowane pliki SRA (Run - SRR...): {df_merged['Run'].nunique()}")
print(f"Zmapowani pacjenci: {df_merged['base_sample_id'].nunique()}")

# 4. Zapis do pliku CSV
output_path = 'data/metadata/samples_ground_truth.csv'
df_merged.to_csv(output_path, index=False)
print(f"Plik wyjściowy zapisano w: {output_path}")



