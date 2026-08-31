"""
TimeSeriesAnalyticsPlatform - Production-grade statistical time-series analytics

Core configuration module for application settings and environment management.
"""

from typing import Optional
from pathlib import Path
import os
from pydantic_settings import BaseSettings
from pydantic import Field


class AppSettings(BaseSettings):
    """Application configuration settings"""

    APP_NAME: str = "TimeSeriesAnalyticsPlatform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    LOG_LEVEL: str = Field(default="INFO")

    # Database configuration
    DATABASE_PATH: Path = Field(default=Path("analytics.db"))
    DATABASE_TIMEOUT: int = 30
    DATABASE_CHECK_SAME_THREAD: bool = False
    DATABASE_JOURNAL_MODE: str = "WAL"

    # Data configuration
    MAX_DATASET_SIZE: int = 500_000
    MIN_SAMPLE_SIZE: int = 2
    CHUNK_SIZE: int = 10_000

    # UI configuration
    WINDOW_WIDTH: int = 1280
    WINDOW_HEIGHT: int = 720
    THEME_PRIMARY_PALETTE: str = "Blue"

    # Statistics configuration
    CONFIDENCE_LEVEL: float = 0.95
    NORMALITY_TEST_SAMPLE_LIMIT: int = 5000
    DEFAULT_ROLLING_WINDOWS: tuple = (10, 25, 50, 100, 250, 500, 1000)
    DEFAULT_THRESHOLDS: tuple = (1.2, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 100.0)

    # Visualization configuration
    VISUALIZATION_DOWNSAMPLE_THRESHOLD: int = 10_000
    CHART_DPI: int = 100
    CHART_STYLE: str = "seaborn-v0_8-darkgrid"

    # File upload configuration
    MAX_IMPORT_FILE_SIZE: int = 100_000_000
    ALLOWED_IMPORT_EXTENSIONS: tuple = (".txt", ".csv", ".json", ".xlsx")

    # Cache configuration
    ENABLE_QUERY_CACHE: bool = True
    CACHE_TIMEOUT_SECONDS: int = 3600

    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def database_url(self) -> str:
        """Get database URL for SQLite"""
        return f"sqlite:///{self.DATABASE_PATH}"

    @property
    def app_data_dir(self) -> Path:
        """Get application data directory"""
        if os.name == "nt":
            app_data = Path(os.getenv("APPDATA", Path.home() / "AppData" / "Roaming"))
        else:
            app_data = Path.home() / ".local" / "share"

        app_dir = app_data / self.APP_NAME
        app_dir.mkdir(parents=True, exist_ok=True)
        return app_dir

    @property
    def logs_dir(self) -> Path:
        """Get logs directory"""
        logs = self.app_data_dir / "logs"
        logs.mkdir(parents=True, exist_ok=True)
        return logs

    @property
    def reports_dir(self) -> Path:
        """Get reports directory"""
        reports = self.app_data_dir / "reports"
        reports.mkdir(parents=True, exist_ok=True)
        return reports

    @property
    def temp_dir(self) -> Path:
        """Get temporary files directory"""
        temp = self.app_data_dir / "temp"
        temp.mkdir(parents=True, exist_ok=True)
        return temp


def get_settings() -> AppSettings:
    """Get application settings instance"""
    return AppSettings()
