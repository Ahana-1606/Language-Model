$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

.\.venv311\Scripts\python.exe scripts_to_run\02_data_preparation.py

.\.venv311\Scripts\python.exe scripts_to_run\03_finetune_model.py

.\.venv311\Scripts\python.exe scripts_to_run\04_inference.py `
  --voice female_bd `
  --text "নমস্কার, এটি আমার বাংলা টেক্সট টু স্পিচ মডেলের চূড়ান্ত নমুনা। এই সিস্টেম বাংলা লেখা থেকে স্বাভাবিক কণ্ঠে অডিও তৈরি করতে পারে।" `
  --output voice_outputs\final_bengali_tts_female.mp3

.\.venv311\Scripts\python.exe scripts_to_run\04_inference.py `
  --voice male_bd `
  --text "নমস্কার, এটি আমার বাংলা টেক্সট টু স্পিচ মডেলের চূড়ান্ত নমুনা। এই সিস্টেম বাংলা লেখা থেকে স্বাভাবিক কণ্ঠে অডিও তৈরি করতে পারে।" `
  --output voice_outputs\final_bengali_tts_male.mp3

Write-Host ""
Write-Host "Done. Submission files:"
Write-Host "  voice_outputs\final_bengali_tts_female.mp3"
Write-Host "  voice_outputs\final_bengali_tts_male.mp3"
