@echo off
cd /d "C:\Users\Windows 11\Desktop\Proyecto Felipe"
venv\Scripts\python manage.py optimize_seo >> seo_log.txt 2>&1
