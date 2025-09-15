import database
from admin_app import AdminApp

def main():
    database.initialize_db()
    app = AdminApp()
    app.mainloop()

if __name__ == "__main__":
    main()

