# Livestock Health Monitoring and Farm Operations Platform

## 1. Project Overview

The **Livestock Health Monitoring and Farm Operations Platform** is a software application designed to simplify livestock health monitoring and farm management activities.

Managing livestock information manually can be difficult and time-consuming. Farmers may face challenges in maintaining health records, tracking vaccination schedules, monitoring breeding activities, and managing daily farm operations.

This platform aims to provide a centralized digital solution to organize livestock information and support efficient farm management.

## 2. Project Objectives

- Maintain livestock health records digitally.
- Manage vaccination schedules and records.
- Monitor breeding activities.
- Organize daily farm operations.
- Identify pending and overdue activities.
- Improve access to livestock information.
- Support better farm management and decision-making.

## 3. Key Features

- **Health Records:** Maintain and manage livestock health information.
- **Vaccination Management:** Organize vaccination schedules and records.
- **Breeding Management:** Maintain breeding-related information.
- **Farm Operations:** Manage regular farm activities.
- **Alerts and Notifications:** Help identify pending or overdue activities, where implemented.
- **Performance Monitoring:** Monitor livestock and farm-related information.
- **Reports:** Organize and view farm management information, where available.

## 4. Repository Structure

The project repository is organized into separate frontend and backend folders.

```text
livestock-health-monitoring/
│
├── backend/
│   └── Backend source code
│
├── frontend/
│   └── Frontend source code
│
├── docker-compose.yml
│
├── HOTFIX.md
│
├── RELEASE_NOTES.md
│
└── README.md
```

*Note: The frontend and backend folders may contain additional files and subfolders.*

## 5. Technologies and Tools

| Component | Technology |
|---|---|
| Frontend | As implemented in the frontend folder |
| Backend | As implemented in the backend folder |
| Database | As configured in the project |
| Version Control | Git and GitHub |
| Containerization | Docker and Docker Compose |

## 6. Getting Started

### Prerequisites

Install the software required by the project:

- Git
- Docker Desktop and Docker Compose, if using containers
- Required frontend and backend runtimes
- Database software, if required

### Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/amruthakola/livestock-health-monitoring.git
```

### Step 2: Navigate to the Project Folder

```bash
cd livestock-health-monitoring
```

### Step 3: Configure the Project

- Open the `frontend` folder and check its dependency files.
- Open the `backend` folder and check its dependency files.
- Configure the required environment variables.
- Configure the database connection, if required.
- Install the dependencies according to the project instructions.

### Step 4: Run the Application

If Docker Compose is properly configured, use:

```bash
docker compose up --build
```

To stop the application:

```bash
docker compose down
```

If running without Docker, follow the setup and execution instructions provided in the frontend and backend folders.

## 7. Application Usage

After starting the application:

1. Open the application using its configured local address.
2. Access the available application features.
3. Manage livestock information.
4. View available health records.
5. Manage vaccination and breeding information, where implemented.
6. Monitor farm activities.
7. View available alerts and reports.

The available functionality depends on the current project implementation.

## 8. Version Control

Git and GitHub are used to manage the source code and track project changes.

The repository contains branches such as:

- `main`
- `develop`
- `feature/health-monitoring`
- `feature/vaccination-management`

Branches help organize development work. Commits record changes, and pull requests allow changes to be reviewed before merging.

## 9. Testing

The application can be evaluated using the following testing areas:

- Application startup and accessibility.
- Input validation.
- Livestock information management.
- Health record management.
- Vaccination schedule management.
- Frontend and backend communication.
- Error handling.

Actual testing results should be recorded after executing the application.

## 10. Future Enhancements

Possible future improvements include:

- Automated vaccination reminders.
- Mobile-friendly application design.
- Advanced livestock health reports.
- Role-based user access.
- Improved search and filtering.
- Secure data backup and recovery.
- Additional farm performance analytics.

## 11. Project Documentation

The repository includes supporting documentation:

- `HOTFIX.md` – Information about documented urgent fixes.
- `RELEASE_NOTES.md` – Information about documented project releases and updates.
- `README.md` – Main project description and setup documentation.

## 12. Conclusion

The Livestock Health Monitoring and Farm Operations Platform aims to improve livestock health monitoring and farm management through a centralized digital system.

The project uses an organized repository structure, GitHub version control, and Docker Compose configuration to support software development and application management.

## 13. Repository Information

**Project Name:** Livestock Health Monitoring and Farm Operations Platform

**GitHub Repository:**  
https://github.com/amruthakola/livestock-health-monitoring

**Version Control:** Git and GitHub

**Institution:** SIMATS Engineering – Saveetha School of Engineering

**Course:** Software Engineering
