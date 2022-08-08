from mental_health import db
from mental_health.models.user import User
from mental_health.models.entry import Entry

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()