import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from themes.sidebar import apply_sidebar_theme, center_sidebar_title

st.set_page_config(
    page_title="Reservation",
    page_icon="🚀",  # Emoji for the tab icon
    layout="wide",
)

apply_sidebar_theme()

# Add a centered sidebar title
center_sidebar_title("Business Name")

# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

def send_confirmation_email(name, email, phone, room, pax, start_date, end_date, booking_datetime):
    sender_email = st.secrets['EMAIL']['username']
    password = st.secrets['EMAIL']['password']

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = 'Booking Confirmation and Receipt'

    # Include confirmation details as a receipt in the email body
    body = f"Dear {name},\n\nThank you for booking {room} for {pax} person(s) from {start_date} to {end_date} on {booking_datetime}. Your booking details are as follows:\n\n"\
           f"Name: {name}\n"\
           f'Email: {email}\n'\
           f'Phone: {phone}\n'\
           f'Room: {room}\n'\
           f'Number of Persons (PAX): {pax}\n'\
           f'Start Date: {start_date}\n'\
           f'End Date: {end_date}\n'\
           f'Booking Date and Time: {booking_datetime}\n\n'\
           f"Thank you for choosing our hotel. We look forward to your stay!\n\nBest regards,\nYour Hotel"

    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, [email], message.as_string())
        st.success(f'Booking confirmation email sent to {email}!')
    except Exception as e:
        st.error(f"Error: Failed to send email to guest. {e}")

def update_google_sheets(booking_data):
    existing_booking_data = conn.read(worksheet="Bookings", usecols=list(range(8)), ttl=5)
    existing_booking_data = existing_booking_data.dropna(how="all")
    updated_booking_data = pd.concat([existing_booking_data, booking_data], ignore_index=True)
    conn.update(worksheet="Bookings", data=updated_booking_data)

def send_emails_and_update_sheets(booking_info):
    name = booking_info['name']
    email = booking_info['email']
    phone = booking_info['phone']
    room = booking_info['room']
    pax = booking_info['pax']
    start_date = booking_info['start_date']
    end_date = booking_info['end_date']
    booking_datetime = booking_info['booking_datetime']

    booking_data = pd.DataFrame([{
        'Name': name,
        'Email': email,
        'Phone': phone,
        'Room': room,
        'PAX': pax,
        'Start Date': start_date,
        'End Date': end_date,
        'Booking DateTime': booking_datetime,
    }])

    with ThreadPoolExecutor() as executor:
        executor.submit(update_google_sheets, booking_data)
        executor.submit(send_confirmation_email, name, email, phone, room, pax, start_date, end_date, booking_datetime)

def main():
    if 'booking_info' not in st.session_state:
        st.session_state.booking_info = {}

    st.title('Hotel Booking Form')

    name = st.text_input('Full Name', key='name')
    email = st.text_input('Email', key='email')
    phone = st.text_input('Phone Number', key='phone')
    room = st.selectbox('Select Room', ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5', 'Room 6', 'Room 7'], key='room')  # Updated room options
    pax = st.number_input('Number of Persons (PAX)', min_value=1, value=1, key='pax')
    start_date = st.date_input('Start Date of Stay', key='start_date')
    end_date = st.date_input('End Date of Stay', key='end_date')
    booking_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if st.button('Book Now'):
        st.session_state.booking_info = {
            'name': name,
            'email': email,
            'phone': phone,
            'room': room,
            'pax': pax,
            'start_date': start_date,
            'end_date': end_date,
            'booking_datetime': booking_datetime,
        }

        send_emails_and_update_sheets(st.session_state.booking_info)

        st.subheader('Confirmation Details:')
        st.write(f'Name: {st.session_state.booking_info["name"]}')
        st.write(f'Email: {st.session_state.booking_info["email"]}')
        st.write(f'Phone: {st.session_state.booking_info["phone"]}')
        st.write(f'Room: {st.session_state.booking_info["room"]}')
        st.write(f'Number of Persons (PAX): {st.session_state.booking_info["pax"]}')
        st.write(f'Start Date: {st.session_state.booking_info["start_date"]}')
        st.write(f'End Date: {st.session_state.booking_info["end_date"]}')
        st.write(f'Booking Date and Time: {st.session_state.booking_info["booking_datetime"]}')

        st.session_state.booking_info = {}

if __name__ == '__main__':
    main()
