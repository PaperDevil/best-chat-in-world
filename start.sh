. ./assets/locals/local.env

echo "=== INSTALL DEPS ==="
pip install -r ./requirements.txt

start=$(date +"%T")
clear
echo "=== STARTING WORK AT $start ==="
uvicorn main:app --reload

end=$(date +"%T")
echo "=== ENDING WORK AT $end ==="