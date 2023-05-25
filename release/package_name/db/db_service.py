from typing import List

from release.package_name.db.sqlite import User, session


def create_user(name: str, email: str, registered: bool) -> User:
    user = User(name=name, email=email, registered=registered)
    session.add(user)
    session.commit()
    return user


def get_all_users() -> List[User]:
    users = session.query(User).all()
    return users


def get_user(user_id: int) -> User:
    user = session.query(User).get(user_id)
    return user


def update_user(user_id: int, name: str, email=None, registered=False) -> User | None:
    user = get_user(user_id)
    if user:
        user.name = name
        user.registered = registered
        if email:
            user.email = email
        session.commit()
        return user
    return None


def delete_user(user_id: int) -> bool:
    user = get_user(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False
