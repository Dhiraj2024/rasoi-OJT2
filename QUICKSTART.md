# ?? Quick Start Guide - Rasoi Guru

## Installation & Setup (5 minutes)

### Step 1: Install Dependencies
```bash
cd d:\Allvsfiles\Arecipi\python\rasoi_guru
pip install -r requirements.txt
```

### Step 2: Configure Database
Edit `.env` file with your MongoDB connection:
```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/?appName=YourApp
DB_NAME=rasoi_guru_db
SECRET_KEY=your_secret_key_here
```

### Step 3: Run the App
```bash
streamlit run app.py
```

App opens at: `http://localhost:8501`

---

## User Journey

### First Time Users
1. **Sign Up** ? Create account with email & password
2. **Explore** ? Browse Recipe Catalog
3. **Discover** ? Use "What's in My Fridge" feature
4. **Save** ? Add recipes to favorites

### Weekly Planning
1. Go to **Meal Planner**
2. Select recipes for each day
3. Click **Save Meal Plan**
4. Your plan is saved for next week

### Add Your Recipe
1. Click **Add Recipe**
2. Fill in:
   - Recipe name
   - Ingredients (comma-separated)
   - Step-by-step instructions
   - Image URL
   - Category & cooking time
3. Submit to share with others

---

## Features at a Glance

| Feature | Location | What It Does |
|---------|----------|-------------|
| ?? What's in My Fridge | Sidebar Menu | Find recipes with your ingredients |
| ?? Recipe Catalog | Sidebar Menu | Browse all recipes |
| ? Add Recipe | Sidebar Menu | Create new recipe |
| ?? Meal Planner | Sidebar Menu | Plan your week |
| ?? Favorites | Sidebar Menu | Save favorite recipes |

---

## Default Ingredients Available
Potato, Tomato, Onion, Garlic, Ginger, Paneer, Chicken, Rice, Wheat, Flour, Eggs, Milk, Olive Oil, Butter, Cumin, Turmeric, Chilli, Salt, Pepper, Coriander, Carrot, Capsicum, Mushroom, Spinach, Lettuce, Cucumber, Yogurt, Cream, Cheese, Bread, Pasta, Sugar

---

## Keyboard Shortcuts

- `Ctrl+C` - Stop the app (in terminal)
- `R` - Rerun Streamlit script
- `C` - Clear cache

---

## Troubleshooting

### "Cannot connect to MongoDB"
**Solution**: App will work with sample data. Add your MongoDB connection to `.env`

### "Port 8501 already in use"
**Solution**: 
```bash
streamlit run app.py --server.port 8502
```

### "Password too short"
**Solution**: Use password with minimum 6 characters

---

## Support

For issues, check:
1. MongoDB connection string in `.env`
2. Internet connection for external images
3. Python version 3.12+
4. All dependencies installed

---

**Happy Cooking! ??**
