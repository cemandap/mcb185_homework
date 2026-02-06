gunzip -c ~/Code/MCB185/data/dictionary.gz \
| grep -E '^.{4,}$' \
| grep r \
| grep -E '^[oznicar]+$'
