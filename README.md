# Restaurant Review System

This project implements a simple Restaurant Review System using SQLAlchemy for database management and Faker for generating sample data. The system includes three main entities: Restaurants, Customers, and Reviews.

## Getting Started

These instructions will help you set up the project and run the scripts to populate the database with sample data.

### Prerequisites

- Python 3.x
- SQLAlchemy
- Faker

Install the required dependencies using:

```bash
pip install sqlalchemy faker
Database Setup
Make sure to have SQLite installed. The default database file is restaurants.db.

Populating the Database
Run the seed.py script to create the database schema and populate it with sample data.

bash
Copy code
python seed.py
Running the Main Script
Run the main script (main.py or your preferred script) to interact with the database and perform various operations.

bash
Copy code
python main.py
Project Structure
models.py: Defines SQLAlchemy models for Restaurant, Customer, and Review entities.
seed.py: Populates the database with sample data using Faker.
main.py: Interacts with the database using SQLAlchemy models.
Author
[moahmed hussein]

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

css
Copy code

Make sure to replace `[Your Name]` in the Author section with your actual name. Additionally, if you have a specific license file, mention it in the License section and include the corresponding `LICENSE.md` file.
