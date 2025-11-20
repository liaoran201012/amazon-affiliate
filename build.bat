@echo off
REM Build script for Amazon Affiliate Site (Windows)

echo ======================================
echo Amazon Affiliate Site Builder
echo ======================================
echo.

REM Step 1: Generate pages from CSV
echo Step 1: Generating pages from CSV...
python scripts/generate_pages.py

if errorlevel 1 (
    echo Error: Failed to generate pages
    pause
    exit /b 1
)

echo.

REM Step 2: Build with Hugo
echo Step 2: Building with Hugo...
hugo --minify

if errorlevel 1 (
    echo Error: Hugo build failed
    pause
    exit /b 1
)

echo.
echo ======================================
echo Build completed successfully!
echo ======================================
echo.
echo Next steps:
echo 1. To preview locally: hugo server --buildDrafts
echo 2. To deploy: git add . ^&^& git commit -m "Update products" ^&^& git push
echo.
pause
