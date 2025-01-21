# Fitness API Documentation

Welcome to the Fitness API! This API enables you to manage users and track their workouts efficiently. Below is a detailed overview of the available endpoints and how to interact with them.

---

## **Base URL**
The API is hosted at:
```
https://bai756.pythonanywhere.com/
```

---

## **Endpoints Overview**

### **Challenges**

**GET** `/challenges`
- **Description:** Fetches all a challenge.
- **Response:**
  ```json
  { 
    "id": 1, "challenge": "50 pushups"
  }
  ```

#### **Create a Daily Challenge**
**POST** `/challenges`
- **Description:** Creates a new daily challenge.
- **Request Body:**
  ```json
  {
    "title": "10,000 Steps",
    "description": "Walk 10,000 steps in a day",
    "reward_points": 50
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "10,000 Steps",
    "description": "Walk 10,000 steps in a day",
    "reward_points": 50
  }
  ```

#### **Retrieve a Daily Challenge**
**GET** `/challenges/:id`
- **Description:** Fetches details of a specific daily challenge.
- **Response:**
  ```json
  {
    "id": 1,
    "title": "10,000 Steps",
    "description": "Walk 10,000 steps in a day",
    "reward_points": 50
  }
  ```

#### **Update a Daily Challenge**
**PATCH** `/challenges/:id`
- **Description:** Updates details of a specific daily challenge.
- **Request Body:**
  ```json
  {
    "title": "15,000 Steps",
    "description": "Walk 15,000 steps in a day",
    "reward_points": 75
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "15,000 Steps",
    "description": "Walk 15,000 steps in a day",
    "reward_points": 75
  }
  ```

#### **Delete a Daily Challenge**
**DELETE** `/challenges/:id`
- **Description:** Deletes a daily challenge by its ID.
- **Response:**
  ```json
  {
    "message": "Challenge deleted"
  }
  ```
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


