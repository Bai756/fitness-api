# Fitness API Documentation

Welcome to the Fitness API! This API enables you to manage users and track their workouts efficiently. Below is a detailed overview of the available endpoints and how to interact with them.

---

## **Base URL**
The API is hosted at:
```
http://<your-domain>
```

---

## **Endpoints Overview**

### **Users**
Endpoints for managing users:

#### **Create a User**
**POST** `/users`
- **Description:** Creates a new user.
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

#### **Retrieve a User**
**GET** `/users/:id`
- **Description:** Fetches details of a specific user.
- **Response:**
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

#### **Update a User**
**PATCH** `/users/:id`
- **Description:** Updates the details of an existing user.
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

#### **Delete a User**
**DELETE** `/users/:id`
- **Description:** Deletes a user by their ID.
- **Response:**
  ```json
  {
    "message": "User deleted successfully"
  }
  ```

---

### **Workouts**
Endpoints for managing workouts:

#### **Retrieve All Workouts for a User**
**GET** `/users/:user_id/workouts`
- **Description:** Fetches all workouts for a specific user.
- **Response:**
  ```json
  [
    {
      "id": 1,
      "user_id": 1,
      "type": "Running",
      "duration": 30,
      "calories": 300
    },
    {
      "id": 2,
      "user_id": 1,
      "type": "Cycling",
      "duration": 45,
      "calories": 450
    }
  ]
  ```

#### **Create a Workout**
**POST** `/workouts`
- **Description:** Creates a new workout.
- **Request Body:**
  ```json
  {
    "user_id": 1,
    "type": "Running",
    "duration": 30,
    "calories": 300
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "user_id": 1,
    "type": "Running",
    "duration": 30,
    "calories": 300
  }
  ```

#### **Retrieve a Workout**
**GET** `/workouts/:id`
- **Description:** Fetches details of a specific workout.
- **Response:**
  ```json
  {
    "id": 1,
    "user_id": 1,
    "type": "Running",
    "duration": 30,
    "calories": 300
  }
  ```

#### **Update a Workout**
**PATCH** `/workouts/:id`
- **Description:** Updates details of a specific workout.
- **Request Body:**
  ```json
  {
    "user_id": 1,
    "type": "Cycling",
    "duration": 45,
    "calories": 450
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "user_id": 1,
    "type": "Cycling",
    "duration": 45,
    "calories": 450
  }
  ```

#### **Delete a Workout**
**DELETE** `/workouts/:id`
- **Description:** Deletes a workout by its ID.
- **Response:**
  ```json
  {
    "message": "Workout deleted"
  }
  ```

---

## **Error Handling**

### Common Error Responses
- **400 Bad Request:**
  - Missing or invalid parameters.
  ```json
  {
    "message": "A user with this email already exists."
  }
  ```

- **404 Not Found:**
  - Resource not found.
  ```json
  {
    "message": "User not found"
  }
  ```

---

## **Data**

### **User**
| Field  | Type     | Description            |
|--------|----------|------------------------|
| `id`   | Integer  | Unique user ID         |
| `name` | String   | Name of the user       |
| `email`| String   | Email address of user  |

### **Workout**
| Field      | Type     | Description                 |
|------------|----------|-----------------------------|
| `id`       | Integer  | Unique workout ID           |
| `user_id`  | Integer  | ID of the associated user   |
| `type`     | String   | Type of workout (e.g., Running) |
| `duration` | Integer  | Duration of workout in minutes |
| `calories` | Integer  | Calories burned during workout |

---


