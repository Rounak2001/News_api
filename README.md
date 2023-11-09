# Django News & Blogs Web Application Documentation

## Overview

This documentation provides an overview of the "News & Blogs" web application developed using Django. The application allows users to register, login, view news articles fetched from a news API, create and delete their own blogs, and log out. The styling is enhanced with Bootstrap.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Features](#features)
   - [User Authentication](#user-authentication)
   - [API Calls and JSON Handling](#api-calls-and-json-handling)
   - [Dashboard](#dashboard)
   - [CRUD Operations](#crud-operations)
   - [Bootstrap Styling](#bootstrap-styling)
3. [Implementation Details](#implementation-details)
   - [User Authentication](#user-authentication-implementation)
   - [API Calls and JSON Handling](#api-calls-and-json-handling-implementation)
   - [Dashboard and CRUD Operations](#dashboard-and-crud-operations-implementation)
   - [Bootstrap Styling](#bootstrap-styling-implementation)

## Project Structure

The project follows a Django web application structure. Key components include:

- `accounts`: Handles user authentication and blog models.
- `newsapi.org`: Fetches news articles from the [newsapi.org](https://newsapi.org/) API.

## Features

### User Authentication

1. **User Registration:**
   - Collects full name, username, email, password, and confirms the password during registration.
   - Applies standard password validation.

2. **User Login and Logout:**
   - Provides a login form for users.
   - Allows users to log out from the application.

3. **Forgot Password Validation:**
   - Feature not implemented in this documentation but can be added using Django's built-in `django.contrib.auth.views.PasswordResetView`.

### API Calls and JSON Handling

1. **Fetch and Display News:**
   - Retrieves news articles from the [newsapi.org](https://newsapi.org/) API.
   - Displays news images and titles on the home page after login.

2. **Redirect to Detailed Article:**
   - Allows users to click on a news clip to view the detailed article on a separate page.

### Dashboard

1. **User Blogs:**
   - Allows logged-in users to create and delete their own blogs.
   - Displays user-created blogs on the dashboard.

### CRUD Operations

1. **Site Administrator API Endpoints:**
   - Provides API endpoints for site administrators to view existing blogs in JSON format.
   - Allows site administrators to delete, update, and create blogs using API endpoints.

### Bootstrap Styling

1. **Styling Elements:**
   - Utilizes Bootstrap for enhanced styling.
   - Implements form controls for blog creation.
   - Incorporates Font Awesome icons for delete operations in the dashboard.

## Implementation Details

### User Authentication Implementation

The `accounts` app implements user registration, login, and logout functionality using Django's built-in authentication views.

### API Calls and JSON Handling Implementation

The `api` app manages API calls and JSON handling. It fetches news articles from the [newsapi.org](https://newsapi.org/) API and displays them on the home page.

### Dashboard and CRUD Operations Implementation

The `accounts` app handles user-created blogs on the dashboard. It provides API endpoints for site administrators to perform CRUD operations on blogs.


For detailed code implementation, refer to the project source code.

---
