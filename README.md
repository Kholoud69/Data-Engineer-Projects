# Data-Engineer-Projects

# Hospital Database ERD

## Overview
This project contains an **Entity-Relationship Diagram (ERD)** for a hospital management system. It models the key entities involved in hospital operations, including staff, patients, schedules, and medical services, and illustrates how they relate to each other.

## Entities
- **Staff**: Hospital personnel such as doctors, nurses, and technicians.
- **Staff-Schedule**: The working shifts and hours assigned to staff members.
- **Services-Weekly**: Medical services provided weekly in the hospital.
- **Patients**: Individuals receiving medical care.

## Relationships
- **Staff ↔ Staff-Schedule (1:N)**: Each staff member can have multiple schedules, but each schedule belongs to exactly one staff member.
- **Staff-Schedule ↔ Services-Weekly (M:N)**: Each staff member’s shift can include multiple services, and each service can be provided by multiple staff members (via a junction table).
- **Patients ↔ Services-Weekly (M:N)**: Patients can receive multiple services per week, and each service can be attended by multiple patients (via a junction table).

## Participation & Cardinality
- Staff-Schedule has **total participation** in staff assignments.
- Services-Weekly and Patients have **partial participation**, depending on scheduled services and patient appointments.

## Purpose
This ERD helps visualize and manage hospital operations, including staff scheduling, service planning, and patient care management. It can serve as a blueprint for building a hospital database system.

## Files
- `hospital_erd.png` – Diagram image of the hospital ERD.
- `hospital_erd.pdf` – PDF version of the ERD (optional).

## Author
- Your Name
- Contact info or GitHub profile link
