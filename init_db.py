from mental_health import db
from mental_health.models.user import User

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()