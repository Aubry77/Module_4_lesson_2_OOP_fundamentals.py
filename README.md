# City Infrastructure Management System

## Objective
The aim of this project is to apply Object-Oriented Programming (OOP) concepts in Python to build a simulated City Infrastructure Management System. This system manages different aspects of a city, such as buildings, traffic, and events.

## Task 1: Vehicle Registration System
- **Description:** Manages vehicle registrations in the city.
- **Class:** `Vehicle`
  - **Attributes:** `registration_number`, `type`, `owner`
  - **Methods:** `update_owner(new_owner)`
- **Demonstration:** Create instances of `Vehicle` and update their owners.

## Task 2: Event Management System Enhancement
- **Description:** Extends the `Event` class to track the number of participants.
- **Class:** `Event`
  - **Attributes:** `name`, `date`, `participant_count`
  - **Methods:** `add_participant()`, `get_participant_count()`
- **Demonstration:** Create instances of `Event`, add participants, and retrieve participant counts.

## How to Run
1. Ensure you have Python installed.
2. Run the script using `python <script_name>.py`.

## Example Usage
```python
# Vehicle Registration System
vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle1.update_owner("Alice Johnson")

# Event Management System
event1 = Event("Music Festival", "2025-06-15")
event1.add_participant()
