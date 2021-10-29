from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.animation import Animation

arq = open('relatorios.txt','a')

class Gerenciador(ScreenManager):
	pass


class Menu(Screen):
	def on_pre_enter(self,*args):
		Window.bind(on_request_close=self.confirma)

	def confirma(self,*args,**kwargs):
		box = BoxLayout(orientation='vertical',spacing=20,padding=10)
		botao = BoxLayout()
		pop = Popup(title='Tem certeza?', content=box, size_hint=(None,None), size=(300,200))
		img = Image(source="noite.jpg")
		bt1 = Button(text='sair',on_release=App.get_running_app().stop)
		bt2 = Button(text='voltar',on_release=pop.dismiss)
		box.add_widget(img)
		botao.add_widget(bt1)
		botao.add_widget(bt2)
		box.add_widget(botao)
		anim = Animation(size=(500,400),duration=0.3, t='out_back')
		animtext = Animation(color=(1,0.3,0,1)) + Animation(color=(1,1,1,1))
		animtext.start(bt1)
		animtext.repeat = True
		anim.start(pop)
		pop.open()
		return True

class Botao(ButtonBehavior,Label):
	cor = ListProperty([0.1,0.5,0.7,1])
	cor2 = ListProperty([0.2,0.2,0.2,1])
	def __init__(self,**kwargs):
		super(Botao,self).__init__(**kwargs)
		self.atualizar()

	def on_pos(self,*args):
		self.atualizar()

	def on_size(self,*args):
		self.atualizar()

	def on_press(self,*args):
		self.cor, self.cor2 = self.cor2, self.cor

	def on_cor(self,*args):
		self.atualizar()

	def on_release(self,*args):
		self.cor2, self.cor = self.cor, self.cor2

	def atualizar(self,*args):

		self.canvas.before.clear()

		with self.canvas.before:
			Color(rgba=self.cor)
			#Ellipse(size=(self.height,self.height), pos=self.pos)
			#Ellipse(size=(self.height,self.height), pos=(self.x+self.width-self.height,self.y))
			Rectangle(size=(self.width-self.height,self.height),pos=(self.x+self.height/2.0,self.y))


class Assistencia(Screen):
	def __init__(self,tarefas=[],**kwargs):
		super().__init__(**kwargs)

	def enviaTexto(self):
		pass
		"""
		arq = open('relatorios.txt','a')
		texto = f'\n{self.ids.tinput.text}'
		arq.write(texto)
		arq.close()
		self.ids.tinput.text = ''
		"""

	def on_pre_enter(self):
			Window.bind(on_keyboard=self.voltar)

	def voltar(self,window,key,*args):
		if key == 27:
			App.get_running_app().root.current ='menu'
			return True
		if key == 13:
			self.addWidget()

	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.voltar)


class Tarefas(Screen):
	def __init__(self,tarefas=[],**kwargs):
		super().__init__(**kwargs)
		arq = open('relatorios.txt','r')
		for tarefa in tarefas:
			self.ids.box.add_widget(Tarefa(text=tarefa+arq.read))
			arq.write(tarefa)

	def on_pre_enter(self):
			Window.bind(on_keyboard=self.voltar)

	def voltar(self,window,key,*args):
		if key == 27:
			App.get_running_app().root.current ='menu'
			return True
		if key == 13:
			self.addWidget()

	def on_pre_leave(self):
		Window.unbind(on_keyboard=self.voltar)

	def addWidget(self):
		arq = open('relatorios.txt','a')
		texto = self.ids.texto.text
		arq.write(texto)
		self.ids.box.add_widget(Tarefa(text=texto))
		self.ids.texto.text = ''
		arq.close()


class Tarefa(BoxLayout):

	def __init__(self,text,**kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = text


class Tela(App):

	def build(self):

		return Gerenciador()


Tela().run()
