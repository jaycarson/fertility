AGE=20
END=25
echo "Starting"
echo "Normal"
python3 Simulation.py --year=$AGE --end=$END > $AGE.stop_$END.normal
echo "Tall"
python3 Simulation.py --year=$AGE --end=$END --tall > $AGE.stop_$END.tall
echo "Healthy"
python3 Simulation.py --year=$AGE --end=$END --healthy > $AGE.stop_$END.healthy
echo "IVF"
python3 Simulation.py --year=$AGE --end=$END --ivf > $AGE.stop_$END.ivf
echo "Smoker"
python3 Simulation.py --year=$AGE --end=$END --regular > $AGE.stop_$END.smoker
echo "Morbid"
python3 Simulation.py --year=$AGE --end=$END --morbid > $AGE.stop_$END.morbid
echo "Completed"
