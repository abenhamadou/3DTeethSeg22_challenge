
call .\build.bat

docker volume create 3DTeethSeg-output

docker run --rm^
 --memory=4g^
 -v %~dp0\test\:/input/^
 -v 3DTeethSeg-output:/output/^
 noduledetection

docker run --rm^
 -v 3DTeethSeg-output:/output/^
 python:3.7-slim cat /output/results.json | python -m json.tool

docker run --rm^
 -v noduledetection-output:/output/^
 -v %~dp0\test\:/input/^
 python:3.7-slim python -c "import json, sys; f1 = json.load(open('/output/results.json')); f2 = json.load(open('/input/expected_output.json')); sys.exit(f1 != f2);"

if %ERRORLEVEL% == 0 (
	echo "Tests successfully passed..."
)
else
(
	echo "Expected output was not found..."
)

docker volume rm 3DTeethSeg-output