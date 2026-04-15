from config import FREE_LIMIT

def check_access(plan, usage):
    if plan == "free" and usage >= FREE_LIMIT:
        return False
    return True