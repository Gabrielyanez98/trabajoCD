from idioma import Idioma
from adminIdioma import AdminEntidades


miIdioma = Idioma("Catalán")

Admin = AdminEntidades()

Admin.insert(miIdioma.getIdioma())