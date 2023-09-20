from django.db import models

class Cidades(models.Model):
    Nome= models.CharField(max_length=50)
    UF= models.CharField(max_length=50)

def __str__(self):
    return f'{self.Nome} {self.UF}'

class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    data_nasc = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Cidades = models.ForeignKey(Cidades, on_delete=models.CASCADE)

def __str__(self):
    return f'{self.nome} {self.pai} {self.mae} {self.cpf} {self.data_nasc} {self.email} {self.cidade}'

class Ocupacao(models.Model):
    Professor = models.CharField(max_length=50)
    Estudante = models.CharField(max_length=50)
    Coordenador = models.CharField(max_length=50)
    Diretor = models.CharField(max_length=50)
    
def __str__(self):
    return f'{self.Professor} {self.Estudante} {self.Coordenador} {self.Diretor}'

class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)  

def __str__(self):
    return f'{self.nome} {self.site} {self.telefone}'

class Saber(models.Model):
    Nome = models.CharField(max_length=50)

def __str__(self):   
    return f'{self.nome}'

class Cursos(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria_total = models.CharField(max_length=50)
    duracao = models.CharField(max_length=50)
    saber = models.ForeignKey(Saber, on_delete=models.CASCADE) 
    Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
def __str__(self):
    return f'{self.nome} {self.carga_horaria_total} {self.duracao} {self.saber}'

class Periodos(models.Model):
    periodo= models.CharField(max_length=50)

def __str__(self):
    return f'{self.periodo}'

class Disciplinas(models.Model):
    nome = models.CharField(max_length=50)
    Saber = models.ForeignKey(Saber, on_delete=models.CASCADE)

def __str__(self):
    return f'{self.nome} {self.saber}'

class Matriculas(models.Model):
    Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    Pessoas = models.ForeignKey(Pessoas,on_delete=models.CASCADE)
    Data_inicio = models.CharField(max_length=50)
    Data_previsao_terminio = models.CharField(max_length=50)

def __str__(self):
    return f'{self.Instituicao} {self.Cursos} {self.Pessoas} {self.Data_inicio} {self.Data_previsao_termino}'

class Avaliacoes(models.Model):
    Descricao= models.CharField(max_length=50)
    Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    Diciplinas = models.ForeignKey(Disciplinas,on_delete=models.CASCADE)

def __str__(self):
    return f'{self.Descricao} {self.Cursos} {self.Diciplinas}'

class Frequencia(models.Model):
    Faltas= models.CharField(max_length=50)
    Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    Diciplinas = models.ForeignKey(Disciplinas,on_delete=models.CASCADE)


def __str__(self):
    return f'{self.Faltas}'

class Turmas(models.Model):
    Periodos= models.CharField(max_length=50)
    nome= models.CharField(max_length=50)

def __str__(self):
    return f'{self.Periodos} {self.nome}'



class Ocorrencias(models.Model):
    Descricao = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    Diciplinas = models.ForeignKey(Disciplinas,on_delete=models.CASCADE)
    Pessoas = models.ForeignKey(Pessoas,on_delete=models.CASCADE)

def __str__(self):
    return f'{self.Descricao} {self.data} {self.Cursos} {self.Disciplinas} {self.Pessoas}'

class Disciplinas_Curso(models.Model):
    Nome = models.CharField(max_length=50)
    Carga_Horaria = models.CharField(max_length=50)
    Cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    Periodos = models.ForeignKey(Periodos,on_delete=models.CASCADE)

def __str__(self):
    return f'{self.Nome} {self.Carga_Horaria} {self.Cursos} {self.Periodos}'

class Tipos_avaliacao(models.Model):
    Prova = models.CharField(max_length=50)
    Trabalho = models.CharField(max_length=50)
    projeto= models.CharField(max_length=50)
    lista = models.CharField(max_length=50)

def __str__(self):
    return f'{self.Prova} {self.Trabalho} {self.projeto} {self.lista}'
    
