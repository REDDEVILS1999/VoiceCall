import sqlite3
from db_init import DB_PATH, db_lock

def get_config():
    with db_lock:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT captcha_length, retry_attempts, prompt_wav_path FROM captcha_config WHERE id = 1")
        row = cursor.fetchone()
        conn.close()
        return {
            "captcha_length": row[0],
            "retry_attempts": row[1],
            "prompt_wav_path": row[2]
        }

def update_config(captcha_length, retry_attempts, prompt_wav_path):
    with db_lock:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE captcha_config
            SET captcha_length = ?, retry_attempts = ?, prompt_wav_path = ?
            WHERE id = 1
        """, (captcha_length, retry_attempts, prompt_wav_path))
        conn.commit()
        conn.close()

