import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///trackables.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
db.init_app(app)

from models import Trackable, Location

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_trackable():
    unique_code = str(uuid.uuid4())[:8].upper()
    trackable = Trackable(code=unique_code)
    db.session.add(trackable)
    db.session.commit()
    flash(f'New trackable generated: {unique_code}', 'success')
    return redirect(url_for('index'))

@app.route('/track', methods=['GET', 'POST'])
def track():
    if request.method == 'POST':
        code = request.form.get('code')
        location_name = request.form.get('location')

        trackable = Trackable.query.filter_by(code=code).first()
        if not trackable:
            flash('Invalid trackable code!', 'danger')
            return redirect(url_for('track'))

        try:
            geolocator = Nominatim(user_agent="geocaching_tracker")
            location_data = geolocator.geocode(location_name)

            if location_data:
                location = Location(
                    trackable_id=trackable.id,
                    name=location_name,
                    latitude=location_data.latitude,
                    longitude=location_data.longitude,
                    timestamp=datetime.utcnow()
                )
                db.session.add(location)
                db.session.commit()
                flash('Location updated successfully!', 'success')
                # Redirect to history page after successful update
                return redirect(url_for('history', code=code))
            else:
                flash('Location not found!', 'danger')
        except GeocoderTimedOut:
            flash('Location service timeout. Please try again.', 'danger')

        return redirect(url_for('track'))

    return render_template('track.html')

@app.route('/history/<code>')
def history(code):
    trackable = Trackable.query.filter_by(code=code).first_or_404()
    return render_template('history.html', trackable=trackable)

with app.app_context():
    db.create_all()
