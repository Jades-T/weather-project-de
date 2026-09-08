# Weather Application - Data Engineering Learning Project

A complete weather application built through the full data engineering lifecycle, designed for deep learning and understanding of data engineering principles.

## Project Overview

This project implements a complete data engineering pipeline that:

- **Extracts** current weather data for multiple cities using weather APIs
- **Transforms** raw JSON data into clean, structured format with validation
- **Loads** processed data into SQLite database for persistent storage
- **Serves** data through an interactive terminal-based dashboard
- **Monitors** data quality and pipeline health

### Architecture

```
Weather API → Data Pipeline → SQLite Database → Dashboard
                ↓
            Validation & Error Handling
                ↓
            Logging & Monitoring
```

## Project Structure

```
weather-project-de/
├── data/
│   ├── weather.db (SQLite database)
│   └── raw/ (raw data backups)
├── src/
│   ├── __init__.py
│   ├── config.py (configuration management)
│   ├── api_client.py (weather API integration)
│   ├── database.py (SQLite operations)
│   ├── pipeline.py (data processing pipeline)
│   └── dashboard.py (user interface)
├── tests/
│   ├── __init__.py
│   ├── test_api_client.py
│   ├── test_database.py
│   └── test_pipeline.py
├── scripts/
│   ├── setup.sh (environment setup)
│   └── run_pipeline.sh (pipeline execution)
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── pytest.ini
├── .env
└── README.md
```

## Prerequisites

- Python 3.11 or higher
- Weather API key (OpenWeatherMap or similar)
- Git (for version control)

## Setup Instructions

### 1. Clone and Navigate

```bash
cd weather-project-de
```

### 2. Run Setup Script

```bash
make setup
```

Or manually:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment

Edit the `.env` file and add your API key:

```bash
WEATHER_API_KEY=your_actual_api_key_here
```

### 4. Initialize Database

```bash
make init-db
```

## Usage

### Running the Application

#### Interactive Dashboard
```bash
make dashboard
```

#### Data Collection Pipeline
```bash
make run
```

#### Collect for Specific Locations
```bash
make run-locations LOCATIONS="London,Paris,Berlin"
```

### Available Make Commands

- `make setup` - Set up development environment
- `make install` - Install dependencies
- `make test` - Run tests
- `make run` - Run weather data collection pipeline
- `make dashboard` - Run interactive dashboard
- `make clean` - Clean generated files
- `make docker-build` - Build Docker container
- `make docker-run` - Run Docker container

## Testing

### Run All Tests
```bash
make test
```

### Run with Coverage
```bash
make test-coverage
```

### Run Specific Test File
```bash
pytest tests/test_api_client.py -v
```

## Docker Deployment

### Build and Run
```bash
make docker-build
make docker-run
```

### View Logs
```bash
make docker-logs
```

### Stop Container
```bash
make docker-stop
```

## Data Engineering Lifecycle

This project follows the complete data engineering lifecycle:

### 1. Requirements Gathering
- Define weather data requirements
- Identify data sources
- Specify update frequency

### 2. System Design
- Architecture planning
- Data model design
- API integration strategy

### 3. Data Ingestion
- API integration with error handling
- Data validation and cleaning
- Rate limiting and retry logic

### 4. Data Storage
- SQLite database schema design
- Efficient data insertion
- Index optimization

### 5. Data Processing
- Data transformation
- Quality checks
- Historical analysis

### 6. Data Serving
- Query optimization
- Dashboard interface
- Real-time updates

### 7. Monitoring & Maintenance
- Logging setup
- Health checks
- Backup strategies

## Key Features

- **Robust Error Handling**: Retry logic, rate limiting, comprehensive error logging
- **Data Validation**: Multi-level validation ensuring data quality
- **Scalable Architecture**: Modular design for easy extension
- **Comprehensive Testing**: Unit tests for all components
- **Containerization**: Docker support for easy deployment
- **Interactive Dashboard**: Terminal-based user interface
- **Scheduled Collection**: Automated weather data collection

## Learning Objectives

- Understanding data flow from source to consumption
- Database design and optimization
- API integration patterns
- Error handling in data pipelines
- Containerization of data applications
- Testing data engineering components
- Build automation and deployment

## Configuration

Key environment variables in `.env`:

- `WEATHER_API_KEY` - Your weather API key
- `WEATHER_API_URL` - API endpoint URL
- `DATABASE_PATH` - SQLite database file path
- `UPDATE_INTERVAL_MINUTES` - Data collection interval
- `MAX_RETRIES` - API retry attempts
- `LOG_LEVEL` - Logging verbosity

## Troubleshooting

### API Key Issues
- Ensure your API key is valid and active
- Check API rate limits
- Verify network connectivity

### Database Issues
- Ensure data directory exists
- Check file permissions
- Run `make init-db` to reinitialize

### Import Errors
- Ensure virtual environment is activated
- Verify all dependencies are installed
- Check Python version compatibility

## Contributing

This is a learning project focused on understanding data engineering principles. Contributions should focus on:

- Improving code clarity and documentation
- Adding educational comments
- Enhancing test coverage
- Implementing additional features with clear explanations

## License

This project is for educational purposes.
