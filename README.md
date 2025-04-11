# WebTools 🛠️

![Python](https://img.shields.io/badge/Python-3.9-blue) ![Flask](https://img.shields.io/badge/Flask-2.0.1-green) ![Docker](https://img.shields.io/badge/Docker-ready-blue) ![License](https://img.shields.io/badge/license-MIT-brightgreen)

**WebTools** is a minimalist web service built with Flask. The project provides handy tools for daily use, such as generating QR codes and shortening links. It is also containerized with Docker for quick deployment.

## 🚀 Features

- **QR Code Generator**: Generate QR codes for any data (links, text, etc.).
- **Link Shortener**: Convert long URLs into short, user-friendly links.
- **Docker Support**: Easily deploy the project using Docker and Docker Compose.

## 📋 Requirements

To run the project without Docker, you will need:

- Python 3.9+
- Flask 2.0.1
- Redis (for storing shortened link data)

If using Docker, you only need:

- Docker

## 🛠️ Installation and Setup

### Option 1: Local Setup (Without Docker)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/webtools.git
   cd webtools
   docker-compose up --build
