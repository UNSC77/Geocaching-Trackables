# Geocaching Trackable System

## Overview
A geocaching trackable code generation and tracking system that allows users to create, monitor, and visualize the journey of trackable items across different locations.

## Key Features
- Interactive location tracking
- Timeline-based history visualization
- Trackable code generation
- Geospatial movement tracking

## Project Architecture
- **Backend**: Flask with SQLAlchemy ORM
- **Database**: PostgreSQL (migrated from SQLite)
- **Frontend**: HTML templates with Bootstrap styling
- **Geocoding**: Geopy with Nominatim service

## Database Models
- `Trackable`: Stores trackable codes and creation timestamps
- `Location`: Stores location history for each trackable with coordinates

## Recent Changes
- July 29, 2025: Added PostgreSQL database support with Neon
- Migrated from SQLite to PostgreSQL for better scalability
- Updated database configuration to use environment variables

## Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `SESSION_SECRET`: Flask session secret key
- `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`: PostgreSQL connection details

## User Preferences
(To be updated as user expresses preferences)
