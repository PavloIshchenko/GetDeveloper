from google.oauth2 import service_account
from googleapiclient.discovery import build
import csv

# Путь к вашему JSON-ключу
credentials_file = 'C:\\Users\\trigu\\Desktop\\GooglePlayScraping\\trigubs-project-52aba150035b.json'
# Путь к файлу со списком названий игр
input_file = 'games_list.txt'
# Путь к файлу для записи информации
output_file = 'app_info.csv'

# Создаем объект учетных данных из файла JSON
credentials = service_account.Credentials.from_service_account_file(
    credentials_file,
    scopes=['https://www.googleapis.com/auth/androidpublisher']
)

# Создаем клиент API
service = build('androidpublisher', 'v3', credentials=credentials)

# Функция для поиска пакетного имени по названию игры
def get_package_name(game_name):
    try:
        response = service.packages().list(
            q=game_name
        ).execute()

        if 'packages' in response and response['packages']:
            return response['packages'][0]['name']
        else:
            print(f"No package name found for {game_name}")
            return None
    except Exception as e:
        print(f"Error retrieving package name for {game_name}: {e}")
        return None

# Функция для получения информации о приложении и разработчике
def get_app_info(package_name):
    try:
        response = service.edits().get(
            packageName=package_name,
            editId='-',  # Use '-' to refer to the active edit
        ).execute()

        app_details = response['details']

        # Информация о приложении
        app_title = app_details['title']
        app_description = app_details['description']
        app_installs = app_details['installs']
        app_categories = app_details['appCategory']
        app_price = app_details['price']

        # Информация о разработчике
        developer_info = response['developer']
        developer_name = developer_info['name']
        developer_email = developer_info['email']
        developer_website = developer_info['website']

        return {
            'Package Name': package_name,
            'App Title': app_title,
            'Description': app_description,
            'Installs': app_installs,
            'Categories': app_categories,
            'Price': app_price,
            'Developer Name': developer_name,
            'Developer Email': developer_email,
            'Developer Website': developer_website
        }
    except Exception as e:
        print(f"Error retrieving information for {package_name}: {e}")
        return None

if __name__ == "__main__":
    # Открываем файл для записи информации
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Package Name', 'App Title', 'Description', 'Installs', 'Categories', 'Price', 'Developer Name', 'Developer Email', 'Developer Website'])
        writer.writeheader()

        # Читаем список игр из файла
        with open(input_file, 'r') as f:
            for line in f:
                game_name = line.strip()
                package_name = get_package_name(game_name)
                if package_name:
                    app_info = get_app_info(package_name)
                    if app_info:
                        writer.writerow(app_info)

    print(f'Информация о приложениях была записана в файл: {output_file}')

