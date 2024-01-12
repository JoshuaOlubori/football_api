from logic import apply_filtering_logic
from api_fetch import fetch_data
from time import sleep
from greeting import get_greeting

def main():
    print("\n")
    get_greeting()
    print("\nWelcome to football_api_v2.\n")
    # Prompt user for input
    user_input = input(
        "This API calls for data for the football season beginning in 2023. Press any key to proceed or enter 's' to choose a different season: ")

    if user_input.lower() == 's':
        # Prompt user for season input
        chosen_season = input(
            "Enter the year starting the season you want (e.g., 2023): ")
    else:
        chosen_season = "2023"

    # Countdown
    for i in range(3, 0, -1):
        print(f"Calling API in {i} seconds...")
        sleep(1)

    print("Calling API now!")
    fetch_data(chosen_season)
    print("API calls completed")

    # Execute filtering logic
    try:
        apply_filtering_logic()

        print("Program completed successfully \n")
    except Exception as e:
        print(f"Error in running program {e}")


if __name__ == '__main__':
    main()