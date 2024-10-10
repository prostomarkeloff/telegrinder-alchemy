---

# 🐉📜 **Telegrinder-Alchemy: The Tome of Botmastery** 📜🐉

_Welcome, fearless coders and digital sorcerers, to **Telegrinder-Alchemy**, the repository that empowers you to create mighty **Telegram bots**! With the combined strength of Telegrinder and SQLAlchemy, this guide will help you craft bots that harness the full potential of PostgreSQL and Docker._

---

## 🧙 **The Tools of Creation**

Prepare yourself for a journey through the realms of bot development with these powerful tools at your command:

- **Telegrinder Framework: The Swift Blade** ⚡️
  An intuitive framework that makes Telegram bot development fast and seamless. Wield it like a master, simplifying your bot-building journey.

- **SQLAlchemy: The Architect of Data** 🏺
  Manage your bot's data effortlessly with SQLAlchemy, a robust ORM that bridges your bot and its database with precision.

- **Migrations: The Scroll of Evolution** 📜
  Pre-configured migrations ensure that your database evolves with your bot without risking the integrity of your data structures.

- **PostgreSQL: The Database Colossus** 🏛️
  A powerful and scalable database that allows your bot to manage vast amounts of data with ease. PostgreSQL is fully integrated to ensure smooth operation.

- **Docker: The Eternal Vessel** 🐳
  Docker containers make deployment across environments easy, providing your bot with a portable and consistent runtime, no matter the server or platform.

---

## ⚔️ **How to Summon Your Bot**

Follow these steps carefully to bring your bot to life:

### 1. **Clone the Repository**
   Begin by cloning the repository to your local machine:
   ```bash
   git clone https://github.com/prostomarkeloff/telegrinder-alchemy
   cd telegrinder-alchemy
   ```

### 2. **Create a Virtual Environment**
   Protect your project from dependency conflicts by creating a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\\Scripts\\activate
   ```

### 3. **Install Poetry for Dependency Management**
   Use Poetry to handle dependencies efficiently:
   ```bash
   pip install poetry
   ```

### 4. **Install Project Dependencies**
   Install all the required dependencies with:
   ```bash
   poetry install
   ```

### 5. **Configure Your Environment**
   Set up the necessary environment variables in a `.bot-env-dev` and `.bot-env-prod` files. Here’s an example:
   ```
   BOT_TOKEN=token
   DB_URL=postgresql+asyncpg://admin:admin@localhost:5432/bot
   POSTGRES_DATA_PATH=./postgres-data
   POSTGRES_USER=admin
   POSTGRES_PASSWORD=admin
   POSTGRES_DB=bot
   ```

### 6. **Run you bot**

  Telegrinder-alchemy lets you use already prewritten scripts, to run your bot locally and get into production.
  All of them do use docker and compose, so have it in mind getting errors.
  Let's run our bot!
  ```sh
  bash scripts/dev-run.sh
  ```

_Your bot is now alive and ready to serve!_

---

## 🌌 **The Path Ahead**

While your bot is now functional, the road to mastery continues. Consider expanding your bot’s capabilities by exploring advanced features of Telegrinder and fine-tuning your PostgreSQL database for optimal performance. Docker will allow you to scale and deploy your bot seamlessly.

---

## 🏰 **Join the Community**

Want to contribute to **Telegrinder-Alchemy**? Fork the repository, submit issues, or create pull requests. Together, we can build something extraordinary!

---

## 🧙‍♀️ **Final Words**

Armed with the knowledge of **Telegrinder-Alchemy**, go forth and build bots of incredible power. Whether your creation is simple or complex, this guide will serve you well.

**Happy coding, and may your bots be ever powerful!**

---

### ✍️ *By*:
- **Author**: prostomarkeloff
- **License**: MIT

🐉 **THE END. BUT ALSO, THE BEGINNING...** 🐉
