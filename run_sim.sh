AGE=30
echo "Starting"
echo "Normal"
python3 Simulation.py --year=$AGE > $AGE.normal
echo "Tall"
python3 Simulation.py --year=$AGE --tall > $AGE.tall
echo "Healthy"
python3 Simulation.py --year=$AGE --healthy > $AGE.healthy
echo "IVF"
python3 Simulation.py --year=$AGE --ivf > $AGE.ivf
echo "Smoker"
python3 Simulation.py --year=$AGE --regular > $AGE.smoker
echo "Morbid"
python3 Simulation.py --year=$AGE --morbid > $AGE.morbid
echo "Completed"
