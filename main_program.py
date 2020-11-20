import file_handling
import music_reports
import display


"""
The main program should use functions from music_reports and display modules
"""


def get_albums():
    user_input = input("Please provide text file name to import data from it: ")
    if not user_input:
        albums = file_handling.import_data()
    else:
        albums = file_handling.import_data(user_input)
    return albums


def get_genre(albums):
    options = list(set([album[3] for album in albums]))
    genre = None
    while genre not in options:
        genre = input("Please enter genre: ").lower()
    return genre


def load_action(action, albums):
    if action == 1:
        genre = get_genre(albums)
        genre_albums = music_reports.get_albums_by_genre(albums, genre)
        display.print_albums_list(genre_albums)
    elif action == 2:
        longest_album = music_reports.get_longest_album(albums)
        display.print_album_info(longest_album)
    elif action == 3:
        total_length = str(music_reports.get_total_albums_length(albums))
        display.print_command_result(total_length)
    elif action == 0:
        return 0
    else:
        raise KeyError("Wrong input!")


def menu_options():
    # options = ["Exit", "Delete album", "Get Albums by genre", "Display oldest album", "Show genre stats"]
    options = ["Exit", "Get Albums by genre", "Get longest album", "Show total albums length"]
    display.print_program_menu(options)


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    albums = get_albums()
    action = None
    while action != "0":
        menu_options()
        try:
            action = input("Select action: ")
            load_action(int(action), albums)
        except KeyError:
            display.print_command_result("No such action!")
        except ValueError:
            display.print_command_result("Please enter a number!")
    display.print_command_result("Goodbye!")


if __name__ == '__main__':
    main()
