import sqlite3
import threading

DB_PATH = "config.db"
db_lock = threading.Lock()

def init_db():
    with db_lock:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS captcha_config (
                id INTEGER PRIMARY KEY,
                captcha_length INTEGER,
                retry_attempts INTEGER,
                prompt_wav_path TEXT
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM captcha_config")
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO captcha_config (id, captcha_length, retry_attempts, prompt_wav_path)
                VALUES (1, 5, 3, '/usr/share/asterisk/sounds/en/hello-world.wav')
            """)
            print("Default config inserted.")

        conn.commit()
        conn.close()
        print("DB initialization complete.")

