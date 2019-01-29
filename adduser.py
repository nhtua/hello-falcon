import bcrypt
import sys
import getopt

from model import User
from model.database import DBManager


def main(argv):
    _with_gift = None
    _with_notification = None
    try:
        opts, args = getopt.getopt(argv, "h", ["username=", "password="])
    except getopt.GetoptError:
        print("python3 adduser.py --username=User --password=Secret")
        exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("python3 adduser.py --username=User --password=Secret")
            exit()
        elif opt == "--username":
            _username = arg
        elif opt == "--password":
            _password = arg

    dbm = DBManager()
    dbm.setup()
    session = dbm.session

    user = session.query(User).filter(User.username == _username).first()
    password = bcrypt.hashpw(bytes(_password, encoding='UTF-8'), bcrypt.gensalt(10))
    print('PASSWORD:', password)
    if user is None:
        user = User(
            username=_username,
            password=password.decode('UTF-8')
        )
        session.add(user)
        print("CREATE USER")
    else:
        user.password = password.decode('UTF-8')
        print("UPDATE PASSWORD")

    session.commit()
    session.close()


if __name__ == "__main__":
    main(sys.argv[1:])
