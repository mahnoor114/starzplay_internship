cd data_folder
#!/bin/bash
cd data_folder
head -n 1 file1.csv > combined.csv
tail -n +2 file1.csv >> combined.csv
tail -n +2 file2.csv >> combined.csv
echo "Merged successfully."

chmod +x merge_script.sh
./merge_script.sh

#!/bin/bash

# Create data folder
mkdir -p data_folder

# Create two sample CSV files
echo "Name,Score" > data_folder/file1.csv
echo "Alice,90" >> data_folder/file1.csv

echo "Name,Score" > data_folder/file2.csv
echo "Bob,85" >> data_folder/file2.csv

# Merge into combined.csv (with header only once)
head -n 1 data_folder/file1.csv > data_folder/combined.csv
tail -n +2 data_folder/file1.csv >> data_folder/combined.csv
tail -n +2 data_folder/file2.csv >> data_folder/combined.csv

Ctrl + O
Ctrl + X

