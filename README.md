# Trending Topics App

This project is a Flask-based web application that fetches and displays trending topics from a website. The app uses cookies to maintain the session for scraping the website, and proxies to ensure better anonymity while fetching the data. The trending topics are then saved into a database for further use.

Note----> Please First Login Manually with your account by pressing the login button 

![Screenshot 2024-12-27 220135](https://github.com/user-attachments/assets/a99aa325-8ee6-457f-8bbd-92083d70ebc3)

## Features

- **Login**: Saves cookies after a successful login to avoid repeated logins.
- **Fetch Trending Topics**: Scrapes the latest trending topics from a website and saves them into the database.
- **Database Integration**: Stores the fetched data in a MongoDB database.
- **Proxy Usage**: Uses proxy IP addresses to avoid rate-limiting or blocking while scraping.
- **Error Handling**: Displays relevant error messages if something goes wrong during the execution.


## Proxy Authentication
**Username**:golu2602
**password**:12345678vai
## Installation

1.**Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
```

2.**Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3.**Install Webdriver-Manager**:
  ```bash
  pip install webdriver-manager
  ```

## How to Run

**1.Navigate to the folder**
```bash
cd <project-folder>
```
**2.Run the Script**

```bash
python app.py
```

## Dependencies
```bash
selenium==4.10.0
webdriver-manager==4.8.0
pymongo==4.6.0
requests==2.31.0
flask==2.3.3
```
# API Reference

## Home Page

**GET** `/`

Fetches the home page.

| Parameter | Type     | Description          |
| :-------- | :------- | :------------------- |
| `none`    | `none`   | Renders the home page.|

## Login Page

**GET** `/login`

Initiates cookie saving and redirects to the script page.

| Parameter | Type     | Description                                  |
| :-------- | :------- | :------------------------------------------- |
| `none`    | `none`   | Saves cookies manually and redirects to the script page. |

---

## Run Script

**GET** `/run-script`

Runs the script to fetch trending topics and save them to the database.

| Parameter | Type     | Description                                 |
| :-------- | :------- | :------------------------------------------ |
| `none`    | `none`   | Fetches trending topics and saves them to the database. If no trending topics found, displays error data. |

---

## Error Handling

**GET** `/error`

Displays error message if an exception occurs during script execution or any error fetching data.

| Parameter | Type     | Description                                 |
| :-------- | :------- | :------------------------------------------ |
| `none`    | `none`   | Displays an error page with exception details. |

---

## Template Rendering

**GET** `/errors.html`

Displays an error page if there is an issue with cookies or during the script execution.

| Parameter | Type     |Description                                    |
| :-------- | :------- | :--------------------------------------------- |
| `data`    | `string` | Error message detailing the issue.            |

**GET** `/page.html`

Displays the page with the trending topics fetched by the script.

| Parameter | Type     | Description                                    |
| :-------- | :------- | :--------------------------------------------- |
| `data`    | `list`   | List of trending topics fetched from the script. |
