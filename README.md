# Website Hit Counter System

## Overview
This project implements a website hit counter system that tracks visits by different customers using multiple devices. The system ensures that each customer visit is counted only once, regardless of the device used.

## Features
- Track visits to a website by different customers.
- Each customer may use multiple devices (laptop, mobile, tablet).
- Ensure each customer visit is counted only once, regardless of the device used.

## API Endpoints
The following API endpoints are implemented:

1. `POST /visit`
   - Track a visit to a website by a specific customer using a specific device.
2. `GET /customer_visit_count`
   - Retrieve the number of visits a specific customer has made to a specific website.
3. `GET /overall_hit_count`
   - Retrieve the total number of visits to a specific website by all customers.
