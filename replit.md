# AI Dementia Risk Assessment Tool

## Overview

This is a Streamlit-based web application that provides AI-powered cognitive assessment and dementia risk evaluation. The application guides users through a comprehensive battery of cognitive tests including memory, attention, language, spatial awareness, and executive function assessments. It uses machine learning models to analyze test results and provide personalized risk assessments and educational resources about cognitive health.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit for web interface and user interaction
- **Multi-page Structure**: Main app with separate pages for Assessment, Results, Education, and Medical Services
- **Session Management**: Streamlit session state for maintaining user data across pages
- **Interactive Components**: Real-time cognitive tests with timers, form inputs, and progress tracking
- **Medical Integration**: Comprehensive medical services with appointment scheduling, report generation, and scan uploads

### Backend Architecture
- **Application Structure**: Single-file main app (`app.py`) with modular page components
- **Test Engine**: Comprehensive cognitive testing framework in `tests/cognitive_tests.py`
- **AI/ML Model**: Random Forest classifier for dementia risk assessment using synthetic training data
- **Data Processing**: Utility classes for session data management and cognitive profile calculation

### Data Storage Solutions
- **Session Storage**: In-memory storage using Streamlit session state
- **Test Data**: Static question banks and cognitive test materials stored in Python modules
- **Model Persistence**: Scikit-learn models with joblib serialization support
- **No Database**: Currently uses temporary session-based storage without persistent database

### Authentication and Authorization
- **User Identification**: UUID-based session identification without authentication
- **Session Tracking**: Automatic user ID generation for anonymous usage
- **No Login System**: Open access application without user accounts

### Medical Services Architecture
- **Appointment System**: Doctor appointment scheduling with smart defaults based on risk assessment scores
- **Document Generation**: Professional PDF report creation using reportlab with medical formatting and disclaimers
- **Medical File Management**: Upload system for CT, MRI, and PET scans with metadata storage and file organization
- **Workflow Integration**: Seamless connection between assessment results and medical services
- **Data Persistence**: JSON-based storage for appointments and scan metadata in medical_data/ directory

### External Dependencies
- **Core Framework**: Streamlit for web application framework
- **Data Science Stack**: 
  - pandas for data manipulation
  - numpy for numerical operations
  - scikit-learn for machine learning models
- **Visualization**: plotly for interactive charts and cognitive profile visualizations
- **Model Training**: RandomForestClassifier with StandardScaler for risk assessment
- **Document Generation**: reportlab for professional PDF report creation
- **Utilities**: datetime and uuid for session management and unique ID generation

### Key Design Patterns
- **Modular Test Architecture**: Separate cognitive test classes with standardized interfaces
- **State Management**: Centralized session state for test progress and results
- **Progressive Assessment**: Multi-stage testing with delayed recall components
- **Educational Integration**: Built-in educational content and resources
- **Medical Compliance**: Comprehensive medical disclaimers and professional consultation guidance

### Risk Assessment Model
- **Training Data**: Synthetic dataset generation for demonstration purposes
- **Feature Engineering**: 10-feature model including age, education, cognitive scores, and risk factors
- **Model Output**: Multi-class risk categorization (Low, Moderate, High, Very High)
- **Validation**: Note that production use would require validated clinical data

## External Dependencies

### Python Libraries
- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning models and preprocessing
- **plotly**: Interactive data visualization
- **joblib**: Model serialization and persistence

### Data Sources
- **Static Question Banks**: Pre-defined cognitive test materials
- **Synthetic Training Data**: Generated datasets for ML model training
- **Educational Content**: Embedded health information and resources

### Development Dependencies
- **Python 3.7+**: Runtime environment
- **pip**: Package management
- **Standard Library**: uuid, datetime, time, random, json, os

Note: The application is designed for demonstration and educational purposes. Production deployment would require integration with validated clinical datasets, secure user authentication, persistent database storage, and compliance with healthcare data regulations.