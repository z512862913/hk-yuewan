import re
from date.models import User

class LoginBackend(object):
	def authenticate(self, username = None, password = None):
		if (username):
			if (re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", username) != None):
				try:
					user = User.objects.get(email = username)
					if (user.check_pasword(password)):
						return user
					else:
						return None
				except User.DoesNotExist:
					return None
			elif ((len(username) == 11) and (re.match("^(1[3458]\d{9})$", username) != None)):
				try:
					user = User.objects.get(mobile = username)
					if (user.check_pasword(password)):
						return user
					else:
						return None
				except User.DoesNotExist:
					return None
			else:
				try:
					user = User.objects.get(username = username)
					if (user.check_pasword(password)):
						return user
					else:
						return None
				except User.DoesNotExist:
					return None
		else:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk = user_id)
		except User.DoesNotExist:
			return None