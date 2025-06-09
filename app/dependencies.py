from app.core.database import SessionLocal

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # Ensure the session is closed after use