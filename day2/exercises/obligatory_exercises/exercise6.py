import datetime

def minutes_lived_since_birth(birthdate):
    # Assuming birthdate is provided in the format 'YYYY-MM-DD'
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    current_date = datetime.datetime.now()

    # Calculate the difference in time
    time_difference = current_date - birthdate

    # Convert the difference into minutes
    minutes_lived = time_difference.total_seconds() / 60

    print("You have lived approximately {:.2f} minutes in your life.".format(minutes_lived))

# Example usage:
birthdate = '1989-06-23'
minutes_lived_since_birth(birthdate)
