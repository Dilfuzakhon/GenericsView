# GenericsView Django Project

## Description

This is a Django-based project called **GenericsView**. It consists of several applications such as `dashboard` and `config`, each serving different parts of the project. The project uses a Generics View architecture and includes basic models like `Faculty`, `Department`, `Group`, `Subject`, `Teacher`, and `Student`. Each model is structured using a `BaseModel` for created and updated timestamps, and relationships are established with proper `related_name` attributes for ease of querying.

## Features

- Faculty and Department relationship management.
- Group and Department-based student management.
- Subject assignment to teachers.
- REST framework integration for building APIs.

## Installation

To set up this project locally, follow these steps:

 **Clone the repository:**

   ```bash
   git clone https://github.com/Dilfuzakhon/GenericsView.git

   pip install django
   pip install djangorestframework
   ```

### Usage

```bash
python manage.py runserver
```
