import oracledb
import bcrypt

# Conexión segura a Oracle
connection = oracledb.connect(
    user="mediuser",
    password="medi123",
    dsn="localhost/XEPDB1"
)
cursor = connection.cursor()


class Usuario:
    def __init__(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo):
        self.__id = id
        self.__nombre_usuario = nombre_usuario
        self.__clave = clave
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__telefono = telefono
        self.__email = email
        self.__tipo = tipo

    # CRUD 
    def crear(self, cursor):
        sql = """INSERT INTO usuario 
                 (nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)
                 VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"""
        hashed_pw = bcrypt.hashpw(self.__clave.encode(), bcrypt.gensalt()).decode()
        cursor.execute(sql, (
            self.__nombre_usuario,
            hashed_pw,
            self.__nombre,
            self.__apellido,
            self.__fecha_nacimiento,
            self.__telefono,
            self.__email,
            self.__tipo
        ))
        print("Usuario creado en BD")

    @staticmethod
    def listar(cursor):
        cursor.execute("SELECT id, nombre_usuario, nombre, apellido, email, tipo FROM usuario")
        for row in cursor:
            print(row)

    def actualizar_email(self, cursor, nuevo_email):
        sql = "UPDATE usuario SET email = :1 WHERE id = :2"
        cursor.execute(sql, (nuevo_email, self.__id))
        print("Email actualizado")

    def eliminar(self, cursor):
        sql = "DELETE FROM usuario WHERE id = :1"
        cursor.execute(sql, (self.__id,))
        print("Usuario eliminado")


class Paciente(Usuario):
    def __init__(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)
        self.__comuna = comuna
        self.__fecha_primera_visita = fecha_primera_visita

    def agendarConsulta(self):
        print("Consulta agendada")


class Medico(Usuario):
    def __init__(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, horario_atencion, fecha_ingreso):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)
        self.__especialidad = especialidad
        self.__horario_atencion = horario_atencion
        self.__fecha_ingreso = fecha_ingreso

    def atenderPaciente(self):
        print("Atendiendo paciente")


class Consulta:
    def __init__(self, id, id_paciente, id_medico, id_receta, fecha, comentarios):
        self.__id = id
        self.__id_paciente = id_paciente
        self.__id_medico = id_medico
        self.__id_receta = id_receta
        self.__fecha = fecha
        self.__comentarios = comentarios

    def crearConsulta(self):
        print("Consulta creada en BD")


class Receta:
    def __init__(self, id, id_paciente, id_medico, descripcion):
        self.__id = id
        self.__id_paciente = id_paciente
        self.__id_medico = id_medico
        self.__descripcion = descripcion

    def crearReceta(self):
        print("Receta creada")


class Agenda:
    def __init__(self, id, id_paciente, id_medico, fecha_consulta, estado):
        self.__id = id
        self.__id_paciente = id_paciente
        self.__id_medico = id_medico
        self.__fecha_consulta = fecha_consulta
        self.__estado = estado

    def crearAgenda(self):
        print("Agenda creada")


class Insumos:
    def __init__(self, id, nombre, tipo, stock):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__stock = stock

    def agregarInsumo(self):
        print("Insumo agregado")
