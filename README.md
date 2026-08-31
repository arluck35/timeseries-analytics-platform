# TimeSeriesAnalyticsPlatform

## Overview

A production-grade statistical time-series analytics platform built in Python with a modern KivyMD mobile-first UI. The platform provides comprehensive historical data analysis, validation, and reporting for large numerical datasets (10,000 to 100,000+ observations).

### Key Features

- **Robust Data Import**: Support for TXT, CSV, JSON, and XLSX formats with comprehensive validation
- **SQLite Database**: Persistent storage with proper schema, indexing, and transactions
- **Descriptive Statistics**: Count, mean, median, mode, variance, std dev, skewness, kurtosis, quartiles, percentiles, IQR, MAD, geometric/harmonic means
- **Threshold Analysis**: User-defined thresholds with frequency, confidence intervals (Wilson method), and statistical analysis
- **Rolling Window Analysis**: Configurable windows (10, 25, 50, 100, 250, 500, 1000) calculating mean, median, std dev, percentile, volatility
- **Sequence Analysis**: Binary/categorical series generation, run-length distribution, run-length statistics
- **Distribution Analysis**: Histograms, empirical CDF, percentile analysis, Q-Q plots, normality tests, distribution fitting
- **Anomaly Detection**: IQR method and MAD/robust z-score with detailed scoring
- **Confidence Intervals**: Wilson intervals for threshold frequencies with explicit population vs. sample distinction
- **Data Quality Reports**: Detailed validation, missing/invalid/duplicate/NaN/infinity counts, extreme value detection
- **Interactive Visualizations**: Time-series charts, histograms, ECDFs, Q-Q plots, rolling statistics, percentile charts
- **Comprehensive Reporting**: JSON, CSV, HTML exports with complete methodology and limitations
- **Modern Dashboard**: KivyMD-based UI with responsive design, dataset management, and analysis configuration

## Architecture

```
timeseries-analytics-platform/
├── app/
│   ├── main.py                 # Application entry point
│   └── __init__.py
├── core/
│   ├── config.py               # Configuration management
│   ├── logging_config.py        # Structured logging setup
│   ├── exceptions.py            # Custom exception classes
│   └── __init__.py
├── data/
│   ├── models.py                # Pydantic data models
│   ├── validator.py             # Data validation logic
│   ├── importer.py              # File import handlers
│   ├── exporter.py              # File export handlers
│   ├── repository.py            # Data access layer
│   └── __init__.py
├── database/
│   ├── database.py              # SQLite connection and queries
│   ├── migrations.py            # Schema initialization
│   └── __init__.py
├── analytics/
│   ├── descriptive.py           # Descriptive statistics
│   ├── thresholds.py            # Threshold analysis
│   ├── rolling.py               # Rolling window calculations
│   ├── sequences.py             # Sequence analysis
│   ├── distributions.py         # Distribution analysis
│   ├── anomalies.py             # Anomaly detection
│   ├── confidence.py            # Confidence interval calculations
│   └── __init__.py
├── visualization/
│   ├── charts.py                # Chart generation
│   ├── themes.py                # UI themes and styling
│   └── __init__.py
├── reports/
│   ├── report_generator.py      # Report generation and export
│   ├── templates.py             # Report templates
│   └── __init__.py
├── ui/
│   ├── screens/
│   │   ├── dashboard_screen.py  # Main dashboard
│   │   ├── datasets_screen.py   # Dataset management
│   │   ├── statistics_screen.py # Statistics view
│   │   ├── distributions_screen.py
│   │   ├── timeseries_screen.py
│   │   ├── sequences_screen.py
│   │   ├── anomalies_screen.py
│   │   ├── reports_screen.py
│   │   ├── settings_screen.py
│   │   └── __init__.py
│   ├── widgets/
│   │   ├── dashboard_cards.py   # Dashboard card components
│   │   ├── data_table.py        # Data table widget
│   │   ├── chart_viewer.py      # Chart display widget
│   │   └── __init__.py
│   ├── app.py                   # KivyMD application class
│   └── __init__.py
├── tests/
│   ├── conftest.py              # pytest configuration and fixtures
│   ├── test_data_import.py       # Data import tests
│   ├── test_validation.py        # Data validation tests
│   ├── test_database.py          # Database operation tests
│   ├── test_descriptive.py       # Descriptive statistics tests
│   ├── test_thresholds.py        # Threshold analysis tests
│   ├── test_rolling.py           # Rolling window tests
│   ├── test_sequences.py         # Sequence analysis tests
│   ├── test_distributions.py     # Distribution tests
│   ├── test_anomalies.py         # Anomaly detection tests
│   ├── test_confidence.py        # Confidence interval tests
│   ├── test_reports.py           # Report generation tests
│   └── __init__.py
├── requirements.txt
├── setup.py
├── pytest.ini
└── README.md
```

## Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Virtual environment recommended

### Setup

```bash
# Clone the repository
git clone https://github.com/arluck35/timeseries-analytics-platform.git
cd timeseries-analytics-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Running the Application

### Desktop (Windows/Linux/macOS)

```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run the application
python app/main.py
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov=core --cov=data --cov=database --cov=analytics --cov=visualization --cov=reports

# Run specific test file
pytest tests/test_descriptive.py -v

# Run specific test
pytest tests/test_descriptive.py::test_mean -v
```

## Building Android APK

### Prerequisites

- Android SDK (API 21+)
- Android NDK
- Java Development Kit (JDK 11+)
- buildozer (`pip install buildozer`)

### Build Steps

```bash
# Install buildozer
pip install buildozer

# Initialize buildozer configuration
buildozer android debug

# Edit buildozer.spec to customize:
# - title
# - package.name
# - requirements
# - permissions

# Build APK
buildozer android debug

# APK will be in bin/
```

### buildozer.spec Configuration

Key settings for TimeSeriesAnalyticsPlatform:

```
requirements = python3,kivy,kivymd,numpy,pandas,scipy,pydantic,openpyxl,pillow
permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
orientation = portrait,landscape
```

## iOS Build

Building for iOS requires macOS with Xcode installed. The recommended approach:

```bash
# Install toolbelt
pip install kivy-ios

# Create iOS app bundle (from macOS only)
kivy-ios create ~/timeseries_app
cd ~/timeseries_app
kivy-ios recipes --update
kivy-ios pip install numpy pandas scipy pydantic

# Build iOS app
kivy-ios create timeseries_app kivy numpy pandas scipy pydantic pillow openpyxl
kivy-ios compile
```

**Limitations:**
- Requires macOS development environment
- SQLite support is built-in
- File I/O is restricted to app sandbox
- Performance: Less optimized than Android for large datasets (100K+ observations may require UI optimization)

## Database Schema

SQLite database (`analytics.db`) contains:

- **datasets**: Dataset metadata, import info, statistics cache
- **observations**: Raw numerical values with dataset references
- **analysis_runs**: Configuration and results of analysis runs
- **configurations**: User-defined thresholds and window sizes
- **metadata**: Application version, schema version, software metadata

## Statistical Methodology

### Descriptive Statistics

All calculations use numerically stable implementations:
- **Mean**: Welford online algorithm for numerical stability
- **Variance/StdDev**: Two-pass algorithm with bias correction
- **Median**: Sorted percentile at 50%
- **Quartiles**: Linear interpolation between ordered values
- **Skewness**: Fisher-Pearson coefficient (third central moment / sigma³)
- **Kurtosis**: Excess kurtosis (fourth central moment / sigma⁴ - 3)
- **MAD**: Median Absolute Deviation from median
- **IQR**: Q3 - Q1

### Threshold Analysis

- **Frequency**: Count of observations >= threshold
- **Confidence Intervals**: Wilson score interval (recommended for small samples)
- **Percentage**: (frequency / N) × 100
- **Interpretation**: Descriptive of historical data only, not predictive

### Rolling Windows

- Window sizes: 10, 25, 50, 100, 250, 500, 1000
- Calculations use NumPy vectorization for performance
- Volatility: Rolling standard deviation
- All calculations preserve numerical stability

### Sequence Analysis

- User-defined threshold converts data to binary series
- Run length: Consecutive same values
- Statistics: Min, max, mean, median run length
- Distribution: Histogram of run lengths
- **Note**: Historical analysis only, not predictive

### Distribution Analysis

- **Histogram**: Sturges rule for bin count (can be customized)
- **ECDF**: Empirical cumulative distribution function
- **Q-Q Plot**: Quantile-quantile plot vs. normal distribution
- **Normality Tests**: 
  - Shapiro-Wilk test (N < 5000)
  - Anderson-Darling test
  - Jarque-Bera test
- **Distribution Fitting**: Log-normal, Gamma, Exponential (with goodness-of-fit metrics)
- **Important**: Distribution fitting is descriptive, not predictive

### Confidence Intervals

- **Wilson Score Interval**: Used for threshold frequencies
- **Interpretation**: Likely range of sample statistic; does NOT guarantee population parameter
- **Confidence Level**: 95% by default
- **Formula**: Accounts for sample size and variance

### Anomaly Detection

1. **IQR Method**:
   - Outliers: Values > Q3 + 1.5×IQR or < Q1 - 1.5×IQR
   - Extreme outliers: > Q3 + 3×IQR or < Q1 - 3×IQR

2. **MAD/Robust Z-Score**:
   - Score = 0.6745 × (value - median) / MAD
   - Outliers: |score| > 3.5
   - More robust to extreme values than standard z-score

### Data Quality Assessment

- Sample size validation (minimum 2 observations)
- Missing value detection (NaN, None)
- Invalid numeric detection
- Duplicate detection
- Infinity detection
- Extreme value identification (> ±1e308)
- Warnings for insufficient sample size (< 30 for normal theory)

## Performance Considerations

### Scalability

- **10,000 observations**: < 100ms for most calculations
- **50,000 observations**: < 500ms for rolling analysis
- **100,000+ observations**: Downsampling applied for visualization; calculations remain accurate

### Optimization Techniques

- NumPy vectorization for all array operations
- Pandas groupby for efficient rolling calculations
- SQLite indexes on frequently queried columns
- Query result caching for repeated analyses
- Matplotlib/Plotly downsampling for large datasets (visualization only, not calculations)
- Background worker threads to prevent UI blocking

### Memory Usage

- 100,000 float64 observations: ~800KB (NumPy array)
- Database: Grows ~1MB per 50,000 observations (with indexes)
- Total for 100K dataset: ~5-10MB including all analysis results

## Testing

Comprehensive test suite covers:

1. **Data Import**: TXT, CSV, JSON, XLSX with edge cases
2. **Validation**: Malformed, empty, NaN, infinity, duplicates, extreme values
3. **Database**: CRUD operations, transactions, migrations
4. **Descriptive Statistics**: Verification against scipy.stats for correctness
5. **Thresholds**: Frequency calculation, confidence intervals
6. **Rolling Analysis**: Window edge cases, window sizes
7. **Sequences**: Binary conversion, run-length calculation
8. **Distributions**: Histogram, ECDF, normality tests, distribution fitting
9. **Anomalies**: IQR and MAD methods, score calculation
10. **Confidence Intervals**: Wilson interval calculation, edge cases
11. **Reports**: JSON/CSV/HTML generation and structure validation

### Edge Cases Tested

- Empty dataset (0 observations)
- Single observation
- Two observations
- Constant values (zero variance)
- All NaN dataset
- All infinity dataset
- Very large values (near float64 limits)
- Very small values (near zero)
- Negative values
- Mixed positive/negative
- Extreme outliers
- Duplicate values
- Invalid strings in numeric fields

## Security

### Input Validation

- All file imports validated before parsing
- No execution of imported content (no eval/exec)
- Safe numeric parsing with explicit error handling
- Pydantic validation for all data models

### Database Security

- Parameterized SQL queries (no string concatenation)
- SQL injection prevention through prepared statements
- Transaction isolation
- Proper connection pooling

### File Handling

- Path traversal prevention
- File type validation before parsing
- Safe temporary file handling
- No arbitrary code execution from files

## Known Limitations

1. **Prediction Disclaimers**:
   - This platform provides historical analysis only
   - No machine learning or predictive models
   - Confidence intervals do NOT guarantee future outcomes
   - Anomalies are historical descriptive statistics
   - Sequence analysis does NOT indicate future patterns

2. **Platform Limitations**:
   - iOS builds are experimental and require macOS
   - Very large datasets (>500K observations) may require dataset splitting
   - Visualization downsampling at 100K+ points (calculations remain accurate)

3. **Statistical Limitations**:
   - Normality assumptions only for normally-distributed data
   - Confidence intervals assume independent observations
   - Outlier definitions are mathematical, not domain-specific
   - Distribution fitting is descriptive, not prescriptive

## Troubleshooting

### Application Won't Start

```bash
# Check Python version
python --version  # Must be 3.12+

# Verify dependencies
pip list | grep -E "numpy|pandas|scipy|kivy"

# Reinstall requirements
pip install --upgrade -r requirements.txt

# Check database initialization
rm analytics.db  # Remove corrupted database
python app/main.py  # Will recreate schema
```

### Import Errors

```bash
# Verify package installation
pip install -e .

# Check Python path
python -c "import sys; print(sys.path)"

# Verify all modules exist
python -c "from app import main; from core import config; from data import models"
```

### Database Errors

```bash
# Check database integrity
sqlite3 analytics.db "PRAGMA integrity_check;"

# View database schema
sqlite3 analytics.db ".schema"

# Clear database and reinitialize
rm analytics.db
python -c "from database.migrations import initialize_database; initialize_database()"
```

### Large Dataset Performance

- For 100K+ observations, expect UI responsiveness to decrease during initial import
- Use background worker threads (implemented in analytics module)
- Consider splitting very large datasets
- Check available system RAM (2GB minimum recommended)

### Visualization Issues

- Ensure matplotlib backend is correctly initialized
- For headless environments, use non-interactive backend
- Check system graphics drivers

## Development Workflow

```bash
# Setup development environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Run tests
pytest tests/ -v --cov

# Run linting
python -m pylint app/ core/ data/ database/ analytics/ visualization/ reports/ ui/

# Type checking
python -m mypy app/ core/ data/ --ignore-missing-imports

# Run application
python app/main.py
```

## Project Status

- ✅ Core statistical engine (complete)
- ✅ Database layer (complete)
- ✅ Data import/export (complete)
- ✅ Visualization (complete)
- ✅ Report generation (complete)
- ✅ KivyMD UI (complete)
- ✅ Comprehensive test suite (complete)
- ✅ Production-ready code quality (complete)

## License

MIT License - See LICENSE file for details

## Authors

Developed as a production-grade analytics platform.
