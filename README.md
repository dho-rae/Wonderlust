# WonderLust - Travel Recommendation Program

## Overview
WonderLust is a practical, Python-based, travel inspiration tool that suggests travel destinations based on user preferences. By considering Vacation Type, Budget Constraints, and Travel Season, it filters through a curated list of cities to recommend the best match.

## How It Works
- The user selects two out of three criteria: Vacation Type, Budget, or Season.
- The program filters destinations accordingly.
- Results are refined using set operations and dictionary lookups to ensure tailored recommendations.

## Key Features
- **Personalised Matching**: Cities are selected based on user preferences.
- **Efficient Data Handling**: Uses dictionaries for structured storage and retrieval.
- **Error Handling**: `try/except` blocks prevent unexpected crashes.
- **Set Operations**: Avoids duplicate recommendations.

## Running the Program
To run WonderLust, execute:
```sh
python3 dream_vacation_planner.py
```
Follow the prompts to enter your travel preferences and receive destination recommendations.

## Example Output
```
Let’s find your dream vacation spot together!
Are you tied to travelling in a particular month? (Yes / No): No
What is of utmost importance to you? (1. Vacation Type / 2. Low-Budget / 3. Season): 1
Select two vacation types in order of preference:
a) Luxury Escape, b) Wellness, c) Urban Nightscape, d) Gastronomy, e) Cultural Immersion, f) Adventure Tourism, g) Nature Retreat
First choice: d
Second choice: e
Voila! Your dream vacation lies in one of the following cities: ['Lisbon', 'Rome', 'Seville', 'Ho Chi Minh']
```
