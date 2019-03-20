from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Modelo Snippet
class Snippet(models.Model):
    creado = models.DateTimeField(auto_now_add = True)
    titulo = models.CharField(max_length=100, blank=True, default='')
    codigo = models.TextField()
    linenos = models.BooleanField(default=False)
    lenguaje = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    estilo = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    autor = models.ForeignKey('auth.User', related_name ='snippets', on_delete=models.CASCADE)
    remarcado = models.TextField()

    def save(self, *args, **kwargs):
        """
        Usando la librería `pygments` para crear una representacion marcada 
        en HTML del snippet de código.
        """
        lexer=get_lexer_by_name(self.lenguaje)
        linenos = 'Tabla' if self.linenos else False
        options = {'Titulo': self.titulo} if self.titulo else {}
        formatter = HtmlFormatter(style = self.estilo, linenos=linenos, full=True, **options)
        self.remarcado = highlight(self.codigo, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ('creado',)
