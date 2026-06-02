# ?? Rasoi Guru - Recipe Finder & Meal Planner

A full-stack web application for discovering recipes, planning meals, and managing ingredients. Built with Streamlit (frontend), Python (backend), and MongoDB (database).

## ?? Features

### Authentication System
- **Signup/Login**: User registration with email and password
- **Password Security**: Passwords hashed using bcrypt
- **Session Management**: Streamlit session_state for user sessions
- **User Database**: All users stored in MongoDB

### Core Features

#### ?? What's in My Fridge
- Browse and select from 30+ common ingredients
- Search ingredients by name
- Get recipe recommendations based on selected ingredients
- Intelligent ingredient matching

#### ?? Recipe Catalog
- Browse all available recipes
- View recipes in attractive card format with images
- Search recipes by name or ingredients
- Filter by category (Veg, Non-Veg, Quick Meals, Desserts, Beverages)
- Quick access to recipe details

#### ?? Recipe Details
- Full recipe information including ingredients and steps
- Cooking time and calorie information
- Difficulty level indicator
- Add to favorites or meal plan directly

#### ? Add Recipe
- User-friendly form to add new recipes
- Upload recipe with name, ingredients, steps, image URL
- Categorize and set cooking time
- Specify difficulty level and calories

#### ?? Weekly Meal Planner
- Visual 7-day meal planning interface
- Assign recipes to each day of the week
- Save meal plans persistently
- Update plans anytime

#### ?? Favorites
- Save favorite recipes for quick access
- View all saved recipes with images
- Remove recipes from favorites
- Quick links to view full recipe details

## ??? Project Structure

```
rasoi_guru/
+-- app.py                    # Main Streamlit application
+-- requirements.txt          # Python dependencies
+-- .env                      # Environment variables
+-- README.md                 # This file
¦
+-- database/
¦   +-- __init__.py
¦   +-- connection.py         # MongoDB connection (lazy-loaded)
¦
+-- models/
¦   +-- __init__.py
¦   +-- user.py              # User model & authentication
¦   +-- recipe.py            # Recipe model & queries
¦   +-- meal_plan.py         # Meal planning model
¦
+-- utils/
    +-- __init__.py
    +-- auth.py              # Password hashing & verification
```

## ??? Tech Stack

- **Frontend**: Streamlit 1.57.0
- **Backend**: Python 3.12
- **Database**: MongoDB Atlas (PyMongo 4.17.0)
- **Authentication**: Bcrypt 5.0.0
- **Environment**: python-dotenv 1.2.2

## ?? Installation

### Prerequisites
- Python 3.12+
- pip package manager
- MongoDB Atlas account (or local MongoDB)

### Setup

1. Clone or download the project:
```bash
cd rasoi_guru
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`:
```env
MONGO_URI=your_mongodb_connection_string
DB_NAME=rasoi_guru_db
SECRET_KEY=your_secret_key
```

4. Run the application:
```bash
streamlit run app.py
```

5. Open browser to `http://localhost:8501`

## ?? UI/UX Design

### Color Scheme
- **Primary**: #FF6B6B (Food red/pink)
- **Secondary**: #FFF5F5 (Light background)
- **Accent**: #FFA07A (Salmon)

### Design Features
- Modern rounded card layouts
- Responsive mobile-friendly design
- Clean spacing and typography
- Intuitive navigation with emojis
- Soft shadow effects

## ?? Database Schema

### Users Collection
```json
{
  "_id": ObjectId,
  "email": String (unique),
  "password": String (hashed),
  "name": String
}
```

### Recipes Collection
```json
{
  "_id": ObjectId,
  "name": String,
  "ingredients": Array<String>,
  "steps": String,
  "image_url": String,
  "category": String,
  "cooking_time": String,
  "calories": Number,
  "difficulty": String,
  "user_id": String,
  "rating": Number,
  "numRatings": Number
}
```

### Meal Plans Collection
```json
{
  "_id": ObjectId,
  "user_id": String,
  "meal_plan": Object {
    "Monday": String,
    "Tuesday": String,
    ...
  }
}
```

### Favorites Collection
```json
{
  "_id": ObjectId,
  "user_id": String,
  "recipe_id": String
}
```

## ?? How to Use

### 1. Create Account
- Click "Sign Up" on the login page
- Enter name, email, and password (min 6 characters)
- Account is created and ready to use

### 2. Browse Recipes
- Navigate to "Recipe Catalog"
- Browse all available recipes
- Use search or filter by category
- Click "View Details" for full recipe information

### 3. Find Recipes by Ingredients
- Go to "What's in My Fridge"
- Select ingredients you have available
- Click "Find Recipes" to see matches
- View and save favorite recipes

### 4. Add Your Own Recipe
- Click "Add Recipe" in the menu
- Fill in recipe details
- Upload image URL and set cooking time
- Recipe is saved and available to all users

### 5. Plan Your Week
- Navigate to "Meal Planner"
- Select recipes for each day (Monday-Sunday)
- Click "Save Meal Plan"
- Plan persists in your account

### 6. Manage Favorites
- Save recipes to favorites using the ?? button
- Visit "Favorites" to see all saved recipes
- Remove recipes anytime

## ?? Security Features

- Passwords hashed with bcrypt (salt rounds: 12)
- Email-based unique user identification
- Session-based authentication
- No password stored in plain text
- Environment variable protection for secrets

## ?? Advanced Features

- Lazy MongoDB connection (works even if DB temporarily unavailable)
- Ingredient search and filtering
- Multi-category recipe organization
- Meal plan persistence
- Recipe recommendation based on available ingredients
- Error handling and fallback UI

## ?? Troubleshooting

### MongoDB Connection Issues
- Verify MONGO_URI in .env file
- Check MongoDB Atlas network access
- Ensure IP is whitelisted
- App works with mock data if connection fails

### Streamlit Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

### Clear Streamlit Cache
```bash
streamlit cache clear
```

## ?? Sample Recipes

The application comes with 5 sample recipes pre-loaded:
1. Classic Masala Dosa (Veg)
2. Chicken Butter Masala (Non-Veg)
3. Palak Paneer (Veg)
4. Vegetable Fried Rice (Quick Meal)
5. Biryani (Non-Veg)

## ?? Future Enhancements

- [ ] User ratings and reviews
- [ ] Nutritional information database
- [ ] Recipe difficulty ratings
- [ ] Social sharing features
- [ ] Dark mode toggle
- [ ] Recipe export to PDF
- [ ] Shopping list generation
- [ ] Voice-based ingredient search

## ?? License

This project is open source and available for educational and personal use.

## ????? Developer

Built with ?? using Streamlit and MongoDB

---

**Status**: ? Fully Functional

**Last Updated**: June 1, 2026

**Version**: 1.0.0
