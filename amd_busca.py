from turtle import back
import PySimpleGUI as sg
from numpy import size
import os
import sys
import pywin32_system32
import keyboard
import io

#
# Nome_do _programa: AMD_BUSCA
#
# site: https://github.com/FabianoLandimDev/AMD_BUSCA_2024
#
# Autor: Fabiano Landim <landimfabiano01@gmail.com>
#
# Manutenção: Fabiano Landim <landimfabiano01@gmail.com>
#
# ESCOPO:
# O Programa consiste em uma Interface Gráfica, desenvolvida com a Biblioteca do Python (PysimpleGUI),
# o intuito do mesmo é auxiliar os operadores lotados no Balcão de Informações do TRJFA (AMD-SERVICES), que necessitam de dados sobre as Empresas no TRJFA-MG.
#
# Histórico:
#
# v1.0.0 2022-08-14, Fabiano Landim:
# - Versão Inicial do Programa.
#
# v1.0.1 2023-05-10, Fabiano Landim:
# - Versão Inicial do Programa, com alguns ajustes ortográficos para facilitar a digitação nas pesquisas pelos colaboradores (usuário final) além do recurso de confirmar a pesquisa com a tecla enter do teclado da Máquina (PC/NOTEBOOK).
#
# - Versão Inicial do Programa, com alguns ajustes ortográficos. Atualização de busca sobre o estabelecimento Farmácia FARMACIAKI, que se desligara do TRJDF em outubro de 2023
#
# v1.0.2_2024-01-22, Fabiano Landim:
# - Mudanças em algumas linhas do código, referente algumas lojas que foram desligadas do TRJFA, inclusão de algumas novas informações sobre guichês no interior do terminal.
#
# Licença: MIT.
#
#Criando a função pertinente à janela principal...
#
#
def janela_inicial():
	sg.theme('Dark Grey 15')
	layout = [
		[sg.Text(' -=-=-= AMD BUSCA -=-=-=', justification='center', text_color='blue', background_color='grey', pad=(0, 10), size=(50, 1), font=('arial 18 bold'))],
		[sg.Text('PESQUISAR POR: ', size=(15, 1), font=('arial 15 bold')), sg.Input(key='-NOME-', size=(25, 1), font=('arial 15'))],
  		[sg.Text('PARA MAIS OPÇÕES COLOQUE UM  " * "  OU  " ** "  ANTES DO NOME DA REFERIDA PESQUISA', justification='center', text_color='yellow', size=(75, 1), font=('arial 10 bold'))],
		[sg.Button('Pesquisar', bind_return_key=True), sg.Button('Sair'), sg.Button('Limpar'), sg.Text('	NOVA PESQUISA / CLIQUE LIMPAR!', size=(38, 1), text_color='red', font=('arial 15 bold'))],
		[sg.Output(size=(65, 16), key='-OUTPUT-', background_color=("Black"))],
		[sg.Text('Desenvolvedor: fabiano.landim@amdservices.com.br', size=(40, 1), font=('arial 10 bold')), sg.Text('/', size=(1, 1), font=('arial 10 bold')), sg.Text('Versão: v1.0.2_2024-01-18, Fabiano Landim', size=(35, 1), font=('arial 10 bold'))]
	]
	return sg.Window('AMD-SERVICES * GUICHÊS EMPRESAS RODOVIÁRIAS * ORGÃOS PÚBLICOS * LOJAS NO TRJDF', layout, font=("Helvetica", 15), finalize=True)

#lendo os eventos...
#
janela = janela_inicial()
#
#criando as listas de cidades separadamente pelas respectivas Empresas...
#
#VIAÇÃO PROGRESSO:
#
cidade_4 = ['afonso arinos', 'além paraíba', 'alem paraiba', 'além paraiba', 'alem paraíba', 'barra mansa', 'barra do piraí', ' bdp', 'barra do pirai', 'levy gasparian', 'matias barbosa', 'paraíba do sul', 'paraiba do sul', 'pds', 'pirapitinga', 'serraria', 'três rios', 'tres rios', '3 rios', 'vassouras', 'volta redonda']
#
#VIAÇÃO SARITUR / COORDENADAS:
#
cidade_1 = ['bh', 'belo horizonte', 'betim', 'carandaí', 'carandai', 'congonhas', 'conselheiro lafayete', 'barbacena', 'congonhas', 'contagem', 'itaúna', 'itauna', 'mariana', 'natal', 'ouro preto', 'pará de minas', 'para de minas', 'pdm', 'raposo', 'ressaquinha',]
#
#VIAÇÃO UTIL/ BRISA/ SAMPAIO:
#
cidade_2 = ['angra dos reis', 'adr', 'brasília', 'brasilia', 'caxias', 'conservatória', 'conservatoria', 'gurupi', 'gurupí', 'imperatriz', 'macaé', 'macae', 'madureira', 'rdj', 'rio de janeiro', 'rio', 'rj', 'valença', 'valenca', 'manoel duarte', 'mogi das cruzes', 'mdc', 'niterói', 'niteroi', 'ouro branco', 'parati', 'rio das flores', 'rdf', 'rio das ostras', 'rdo', 'são bernardo do campo', 'sao bernardo do campo', 'sbdc', 'são josé dos campos', 'sao jose dos campos', 'sjdc', 'taubaté', 'taubate', 'valença', 'valenca']
#
#VIAÇÃO UNIDA:
#
cidade_5 = ['caranguejo', 'coimbra', 'coronel fabriciano', 'ervália', 'ervalia', 'ipatinga', 'itabira', 'joão molevade', 'joao molevade', 'molevade',  'mercês', 'merces', 'nova era', 'ponte nova', 'porto firme', 'rio casca', 'rio pomba', 'são domingos do prata', 'sao domingos do prata', 'sddp', 'são geraldo', 'sao geraldo', 'senador firmino', 'tabuleiro', 'teixeiras', 'timóteo', 'timoteo', 'tocantins', 'ubá', 'uba', 'viçosa', 'vicosa', 'visconde do rio branco', 'vdrb']
#
#VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001:
#
cidade_3 = ['alfenas', 'águas de lindóia', 'aguas de lindoia', 'adl', 'americana', 'aparecida do norte', 'ap do norte', 'adn', 'bragança paulista', 'braganca paulista', 'campinas', 'campo mourão', 'campo mourao', 'sp', 'são paulo', 'sao paulo', 'araraquara', '*catanduvas', 'curitiba', 'extrema', 'florianópolis',  'florianopolis', 'floripa', 'jacareí', 'jacarei', 'joinvile', 'jundiaí', 'jundiai', 'londrina', 'medianeira', 'mogi mirim', 'mogi guaçu', 'mogi guaçú', 'mogi guacu', 'ourinhos', '*piracicaba', 'pirassununga', 'porto alegre', 'resende', '*ribeirão preto', '*ribeirao preto', 'santo andré', 'santo andre', 'santos', 'são caetano', 'sao caetano', 'são carlos', 'sao carlos', 'são gonçalo do sapucaia', 'sao gonçalo do sapucaia', 'sgds', 'são joão do rio preto', 'sao joao do rio preto', 'sjdrp', 'sorocaba']
#
#VIAÇÃO TRANSUR:
#
cidade_6 = ['bananal', 'barbacena', 'barroso', 'caieiro', 'correia de almeida', 'cda', 'dores de campos', 'ddc', 'ewbank da câmara', 'ewbank da camara', 'edc', 'faixa azul', 'helvas', 'ibertioga', 'itutinga', 'lavras', 'madre de deus', 'mdd',  'peróbas', 'perobas', 'prados', 'santos dumont', 'são joão da serra', 'sjds', 'sao joao da serra', 'são joão del rei', 'sao joao del rei', 'sjdr', 'são sebastião da vitória', 'sao sebastiao da vitoria', 'ssdv', 'tiradentes']
#
#VIAÇÃO BASSAMAR:
#
cidade_7 = ['aeroporto', 'acampamento de campelina', 'adc', 'andrelândia', 'andrelandia', 'arantina', 'argirita', 'bela vista de minas', 'bvdm', 'bias fortes', 'bicas', 'boa vista', 'bom jardim de minas', 'bjdm', 'cachoeira', 'chiador', 'conceição', 'conceiçao', 'conceicao', 'conceição do rio verde', 'conceicao do rio verde', 'conceiçao do rio verde', 'cdrv', '*conceição do monte alegre', '*conceicao do monte alegre', '*conceiçao do monte alegre', '*cdma', 'descoberto', 'ferreira lage', 'guarará', 'guarara', '*leopoldina', '*liberdade', 'lima duarte', 'mar de espanha', 'mde', 'maripá de minas', 'maripa de minas', 'mdm', 'monte verde', 'olaria', 'orvalho', 'palmital', 'pedro teixeira', 'pequeri', 'ponte preta', 'recreio', 'rio preto', 'rochedo de minas', 'rdm', 'santa bárbara', 'snt bárbara', 'santa barbara', 'santa helena de minas', 'shdm', 'santa rita do jacutinga',  'snt rita do jacutinga', 'srdj', 'santana do deserto', 'sdd', 'santo antônio aventureiro', 'santo antonio aventureiro', 'saa', 'são joão nepomuceno', 'sao joao nepomuceno', 'sjn', 'são roque de minas', 'sao roque de minas', 'srdm', 'são vicente de minas', 'sao vicente de minas', 'svdm', 'senador cortês', 'senador cortes', '*serra bocaina', 'sossego', 'sôssego', 'tebas', 'torres', 'três ilhas', 'tres ilhas', '3 ilhas', 'valadares', 'vale sobrado']
#
#VIAÇÃO RIO DOCE:
#
cidade_8 = ['águas pretas', 'aguas pretas', 'almenara', 'araçuaí', 'araçuai', 'aracuai', '**bicas', 'bicuíba', 'bicuiba', 'bjdi', 'bom jesus do itabapoana', 'cachoeiro do itapemirim', 'cdi', 'camacam', 'campanário', 'campanario', 'campos dos goytacazes', 'cdg', 'campos', 'caratinga', 'carlos chagas', 'dom cavate', 'engenheiro caldas', 'eng caldas', 'eunápolis', 'eunapolis', 'felisburgo', 'frei inocêncio', 'frei inocencio', 'governador valadares', 'guarapari', 'guaraparí', 'ilhéus', 'ilheus', 'inhapim', 'itabacuri', 'itabuna', 'itagimirim', 'itamaraju', 'itambé', 'itambe', 'itaobim', 'itaoca', 'itaperuna',  'jequitinhonha', '**leopoldina', '*manhuaçu', '*manhuacu', 'marataizes', 'marataízes', 'monte pascoal', 'nanuque', 'novo cruzeiro', 'orizânia', 'orizania', 'pedra azul', 'piúma', 'piuma', 'posto da mata', 'pdm', 'realeza', 'rio do prado', 'rdp', 'santa bárbara do leste', 'santa barbara do leste', 'snt barbara do leste', 'sbdl', 'santa clara', 'snt clara', 'teófilo otoni', 'teofilo otoni',  'vargem grande', 'vila velha', 'virgem da lapa', 'vdl', 'vitória', 'vitoria', 'vitória da conquista', 'vitoria da conquista', 'vdc']
#
#VIAÇÃO SANTA CRUZ:
#
cidade_9 = ['aiuruoca', '*alfenas', '*americana', 'andradas', '*araraquara', 'baependi', '*bom jardim de minas', '*bjdm', '*bragança paulista', 'cambuquira', '*campinas', 'carvalhos', 'catanduvas', 'caxambu', 'cruzilia', 'cruzília', 'guaxupé', 'guaxupe', 'lambari', 'passa quatro', 'piracicaba', '*pirassununga', 'poços de caldas', 'pocos de caldas', 'pouso alegre', 'ribeirão preto', 'ribeirao preto',  '*são carlos', '*sao carlos', 'são josé do rio preto', 'sao jose do rio preto', 'sjrp', '*são joão do rio preto', 'sao joao do rio preto', '*sjdrp', 'são lourenço', 'sao lourenço', 'sao lourenco', 'são tomé das letras', 'sao tome das letras', 'stdl', 'seritinga', 'três corações', 'tres coraçoes', 'tres coracoes', 'varginha', ]
#
#VIAÇÃO GONTIJO:
#
cidade_10 = ['alto araguaia', 'alto garças', 'alto garcas', 'anápolis', 'anapolis' 'aracajú', 'aracaju', 'araxá', 'araxa', 'arcos', 'bambuí', 'bambui', 'bom despacho', 'campo belo', 'campos altos', 'cana verde', 'candeias', 'catalao', 'catalão', 'cristais', 'cuiabá', 'cuiaba', 'divinópolis', 'divinopolis', 'estalagem', 'feira de santana', 'fds', 'formiga', 'iguatama', 'itumbiara', 'jaciara', 'jataí', 'jatai', 'jequié', 'jequie', 'joão pessoa', 'joao pessoa', 'mineiros', 'nova ponte', 'nova serrana', 'oliveira', 'perdões', 'perdoes', 'rio verde', 'rondonópolis', 'rondonopolis', 'santa juliana', 'snt juliana', 'uberaba', 'uberlândia', 'uberlandia']
#
#VIAÇÃO PARAIBUNA:
#
cidade_11 = ['alto jequitibá', 'alto jequitiba', 'alvorada de minas', '*argirita', 'bom jesus da cachoeira', 'bjdc', 'caparaó divino', 'caparao divino', 'carangola', 'cataguases', 'conceição do monte alegre', 'conceicao do monte alegre', 'conceiçao do monte alegre', 'cdma', 'espera feliz', 'fervedouro', 'fortaleza de minas', 'fdm', '*guarará', 'guarara', 'laranjal', 'leopoldina', 'liberdade', 'manhuaçu', 'manhuacu', 'manhumirim', '*maripá de minas', '*mdm', '*matias barbosa', 'minduri', 'mindurí', 'miradouro', 'miraí',  'mirai', '*monte verde', 'muriaé', 'muriae', 'parque nacional caparaó', 'parque nacional do caparao', 'pndc', 'passo da pátria', 'passo da patria', 'pdp', '*ponte preta', '*santa helena de minas', '*shdm', '*snt helena de minas', 'serra bocaina', 'simão pereira', 'simao pereira', '*sossego', '*tebas']
#
#VIAÇÃO UNIÃO:
#
cidade_12 = ['alto paraíso de goiás', 'alto paraiso de goias', 'apdg', 'araguari', 'arraias', 'belém', 'belem', 'bocaiúva', 'bocaiuva', 'buenópolis', 'buenopolis',  'caldas novas', 'campos belos', 'conceição do tocantins', 'conceicao do tocantins', 'corinto', 'curvelo', 'goiânia', 'goiania', 'janaúba', 'janauba', 'jaraguá', 'jaragua', 'lages', 'mafra', 'maringá', 'maringa', 'medina', 'monte alegre de goiás', 'monte alegre de goias', 'madg', 'monte carmelo', 'montes claros', 'natividade', 'palmas', 'paracatu','paracatú', 'patos de minas', 'pdm', 'patrocínio', 'patrocinio', 'piracanjuba', 'pirapora', 'planaltina', 'porangatu', 'porto nacional', 'rialma', 'santa rosa do tocantins', 'srdt', 'santo ângelo', 'snt angelo', 'santo angelo', 'são gabriel', 'sao gabriel', 'são joão daliança', 'são joão da aliança', 'sjda', 'sao joao da aliança', 'sao joao da alinca', 'são luiz gonzaga', 'sao luiz gonzaga', 'slg', 'sete lagoas', 'silvanópolis', 'silvanopolis', 'três marias', '3 marias', 'tres marias',  'unaí', 'unai',  'uruaçu', 'uruaçú', 'uruacu']
#
#VIAÇÃO UNICA:
#
cidade_13 = ['areal', 'cabo frio', 'itaipava', 'nova friburgo', 'nova iguaçú', 'nova iguaçu', 'nova iguacu', 'petrópolis', 'petropolis', 'rio bonito', 'são pedro da aldeia', 'spda', 'sao pedro da aldeia']
#
#VIAÇÃO JOSÉ MARIA RODRIGUES:
#
cidade_14 = ['*aeroporto', 'astolfo dutra', '*bicas', 'campestre', 'coronel pacheco', 'dona euzébia', 'dona euzebia', 'goianá', 'goiana', 'guarani', 'guaraní', 'joão ferreira', 'joao ferreira', 'piau', 'piraúba', 'pirauba', 'rio novo', 'sobral pinto', 'toledos', 'triqueda']
#
#VIAÇÃO ÀGUIA BRANCA:
#
cidade_15 = ['foz do iguaçú', 'foz do iguaçu', 'foz do iguacu', 'são josé dos campos', 'sao jose dos campos', 'sjdc', '*taubaté', '*taubate']
#
#VIAÇÃO ITAPEMIRIM:
#
cidade_16 = ['*aracaju', 'aracaju', '*aracajú', '*aracaju', '*belo horizonte', '*bh', 'campina grande', '*curitiba', '*feira de santana', '*fds', '*guarapari', '*guaraparí', '*ipatinga', '*nanuque', '*rio de janeiro', '*rdj', '*rj', 'salvador', '*são paulo', '*sao paulo', '*sp', '*vitória da conquista', '*vitoria da conquista', '*vdc']
#Lista de Tarifas...
#
#Referente ao valor da tarifa de R$0,85
#
tarifa_1 = ['aeroporto', '*aeroporto', 'goianá', 'goiana', 'conceição do rio verde', 'conceicao do rio verde', 'conceiçao do rio verde', 'cdrv', 'coronel pacheco', 'ewbank da câmara', 'ewbank da camara', 'ewbank', 'eubank da camara', 'ferreira lage', 'joão ferreira', 'joao ferreira', 'matias barbosa', '*matias barbosa', 'monte verde', '*monte verde', 'passo da pátria', 'passo da patria', 'santa bárbara', 'snt bárbara', 'santa barbara', 'são roque de minas', 'sao roque de minas', 'srdm', 'senador cortês', 'senador cortes', 'triqueda', 'valadares'] 
#
#Referente ao valor da tarifa de R$1,45
#
tarifa_2 = ['afonso arinos', 'bela vista de minas', 'bvdm', 'bias fortes', 'bicas', '*bicas', '**bicas', 'boa vista', 'bom jardim de minas', 'bjdm', '*bom jardim de minas', '*bjdm', 'cachoeira', 'caranguejo', 'chiador', 'conceiçao', 'conceicao', 'conceição', 'correia de almeida', 'cda', 'faixa azul', 'guarani', 'guaraní', 'guarará', 'guarara', '*guarará', '*guarara', 'lima duarte', 'mar de espanha', 'maripá de minas', 'maripa de minas', '*maripá de minas', '*maripa de minas', 'mdm', '*mdm', 'olaria', 'orvalho', 'palmital','paraíba do sul', 'paraiba do sul', 'pds', 'pedro teixeira', 'pequeri', 'pequerí', 'peróbas', 'perobas', 'piau', 'ponte preta', '*ponte preta', 'rio novo', 'rio pomba', 'rochedo de minas', 'rdm', 'santa helena de minas', 'shdm', '*santa helena de minas', '*shdm', 'snt helena de minas',  'santo antônio aventureiro', 'santo antonio aventureiro', 'snt antonio aventureiro', 'snt aventureiro', 'saa', 'santos dumont', 'são joão da serra', 'sao joao da serra', 'sjds', 'são joão nepomuceno', 'sao joao nepomuceno', 'sjn', 'simão pereira', 'simao pereira', 'sossego', 'sôssego', '*sôssego', '*sossego', 'tabuleiro']
#
#Referente ao valor da tarifa de R$2,55
#
tarifa_3 = ['além paraíba', 'alem paraiba', 'além paraiba', 'alem paraíba', 'acampamento de campelina', 'adc', 'alto jequitibá', 'alto jequitiba', 'alvorada de minas', 'argirita', '*argirita', 'astolfo dutra', 'barbacena', 'barroso', 'bom jesus da cachoeira', 'bjdc', 'caieiro', 'campestre', 'carandaí', 'carandai', 'coimbra', 'ubá', 'uba', 'visconde do rio branco', 'vdrb', 'cataguases', 'conceição do monte alegre', 'conceicao do monte alegre', 'cdma', '*conceição do monte alegre', '*conceicao do monte alegre', '*cdma', 'conservatória', 'conservatoria', 'descoberto', 'dona euzébia', 'dona euzebia', 'dores de campos', 'ervália', 'ervalia', 'fortaleza de minas', 'fdm', 'helvas', 'ibertioga', 'itaipava', 'laranjal', 'leopoldina', '*leopoldina', 'levy gasparian', 'madre de deus', 'mdd', 'manoel duarte', 'mercês', 'merces', 'minduri', 'mindurí', 'nova friburgo', 'nova iguaçú', 'nova iguaçu', 'paraíba do sul', 'paraiba do sul', 'pds', 'petrópolis', 'petropolis', 'pirapitinga', 'piraúba', 'pirauba', 'prados', 'ressaquinha', 'rio das flores', 'rdf', 'rio preto', 'santana do deserto', 'sdd', 'são pedro da aldeia', 'sao pedro da aldeia', 'spda', 'são sebastião da vitória', 'sao sebastiao da vitoria', 'ssdv', 'senador firmino', 'serra bocaina', '*serra bocaina', 'sobral pinto', 'tebas', '*tebas', 'tiradentes', 'tocantins', 'toledos', 'três ilhas', 'tres ilhas', '3 ilhas', 'três rios',  'tres rios', '3 rios', 'vale sobrado', 'valença', 'vassouras', 'visconde do rio branco', 'vdrb',] 
#
#Referente ao valor da tarifa de R$5,25
#
tarifa_4 = ['alegrete', 'aiuruoca', 'almenara', 'alfenas', '*alfenas', 'alto araguaia', 'alto garças', 'alto garcas', 'águas pretas', 'aguas pretas', 'águas de lindóia', 'aguas de lindoia', 'alto paraíso de goiás', 'alto paraiso de goias', 'apdg', 'americana', '*americana', 'anápolis', 'anapolis', 'andradas', 'andrelândia', 'andrelandia', 'angra dos reis', 'adr', 'aparecida do norte', 'ap do norte', 'adn', 'aracajú', 'aracaju', '*aracajú', '*aracaju', 'araçuaí', 'araçuai', 'aracuai', 'araguari', 'arantina', 'araraquara', '*araraquara', 'araxá', 'araxa', 'arcos', 'areal', 'arraias', 'baependi', 'bambuí', 'bambui', 'bananal', 'barra do piraí', 'barra do pirai', 'barra mansa', 'belém', 'belem', 'belo horizonte','*belo horizonte', '*bh', 'bh', 'betim', 'bicuíba', 'bicuiba', 'bocaiúva', 'bocaiuva', 'bom despacho', 'bom jesus do itabapoana', 'bjdi', 'bragança paulista', 'braganca paulista', '*bragança paulista', '*braganca paulista', 'brasilia', 'brasília', 'buenópolis', 'buenopolis', 'cabo frio', 'cachoeiro do itapemirim', 'cdi', 'caldas novas', 'camacam', 'cambuquira', 'campanario', 'campanário', 'campinas', '*campinas', 'campina grande', 'campo belo', 'campos dos goytacazes', 'cdg', 'campos goytacazes', 'campos altos', 'campos belos', 'campo mourão', 'campo mourao', 'cana verde', 'candeias', 'caparaó divino', 'caparao divino', 'carangola', 'caratinga', 'carlos chagas', 'carvalhos', 'catalao', 'catalão', 'catanduvas', '*catanduvas', 'caxambu', 'caxambú', 'caxias', 'conceição do tocantins', 'conceicao do tocantins','cdt', 'congonhas', 'conselheiro lafayete', 'contagem', 'corinto', 'coronel fabriciano', 'cruzilia', 'cruzília',  'cuiabá', 'cuiaba', 'curitiba', '*curitiba', 'curvelo', 'divinópolis', 'divinopolis', 'dom cavate', 'engenheiro caldas', 'eng caldas', 'espera feliz', 'estalagem', 'eunápolis', 'eunapolis', 'extrema', 'cristais', 'feira de santana', 'fds', '*feira de santana', '*fds', 'felisburgo', 'fervedouro', 'florianópolis', 'florianopolis', 'formiga', 'foz do iguaçu', 'foz do iguaçú', 'foz do iguacu', 'frei inocêncio', 'frei inocencio', 'goiania', 'goiânia', 'governador valadares', 'guarapari', 'guaraparí', '*guaraparí', '*guarapari', 'guaxupé', 'guaxupe',  'gurupi', 'guarupí', 'iguatama', 'ilhéus', 'ilheus', 'ipatinga', '*ipatinga', 'imperatriz', 'inhapim', 'itabacuri', 'itabacurí', 'itabira', 'itabuna', 'itagimirim', 'itamaraju', 'itambé', 'itaobim', 'itaoca', 'itaperuna', 'itaúna', 'itauna', 'itumbiara', 'itutinga', 'jacareí', 'jacarei', 'jaciara', 'janúba', 'januda', 'jaraguá', 'jaragua', 'jataí', 'jatai', 'jequié', 'jequie', 'jequitinhonha', 'joão molevade', 'joao molevade', 'joão pessoa', 'joao pessoa', 'joinvile', 'jundiaí', 'jundiai', 'lages', 'lambari', 'lambarí', 'lavras','**leopoldina', 'liberdade', '*liberdade', 'londrina', 'macaé', 'macae', 'madureira', 'mafra', 'manhuaçu', '*manhuaçu', 'manhuacu', '*mnhuacu', 'manhumirim', 'marataizes', 'mariana', 'maringá', 'medianeira', 'medina', 'mineiros', 'miradouro', 'miraí', 'mirai', 'mogi mirim', 'mogi das cruzes', 'mogi guaçu', 'mogi guaçú', 'monte alegre de goiás', 'monte alegre de goias', 'madg', 'monte carmelo', 'monte pascoal', 'montes claros', 'muriaé', 'muriae', 'nanuque', '*nanuque', 'natal', 'natividade', 'niterói', 'niteroi', 'nova era', 'nova ponte', 'nova serrana', 'novo cruzeiro', 'oliveira', 'ourinhos', 'ouro branco', 'ouro preto', 'orizânia', 'orizania', 'palmas', 'paracatu' 'paracatú', 'pará de minas', 'pará de minas', 'parati', 'parque nacional caparaó', 'pnc', 'parque nacional caparao', 'passa quatro', ' passa 4', 'patos de minas', 'pdm', 'patrocínio', 'patrocinio', 'pedra azul', 'perdões', 'perdoes', 'piracanjuba', 'piracicaba', '*piracicaba', 'pirapora', 'pirassununga', '*pirassununga', 'piúma', 'piuma', 'planaltina', 'poços de caldas', 'ponte nova', 'porangatu', 'porangatú', 'porto alegre',  'porto firme', 'porto nacional', 'posto da mata', 'pouso alegre', 'raposo', 'realeza', 'recreio', 'resende', 'rialma', 'ribeirão preto', '*ribeirão preto','ribeirao preto', '*ribeirao preto', 'rio bonito', 'rio casca', 'rio das ostras', 'rdo', 'rio de janeiro', '*rio de janeiro', 'rdj', '*rdj', 'rj', '*rj', 'rio do prado', 'rdp', 'rio verde', 'rondonópolis', 'rondonopolis', 'santa bárbara do leste', 'sbdl', 'santa clara', 'snt clara', 'santa juliana', 'snt juliana', 'santa rita de jacutinga', 'srdj', 'snt rita de jacutinga', 'santa rosa do tocantins', 'srdt', 'santo andré', 'santo andre', 'santo ângelo', 'santo angelo', 'santos', 'são bernardo do campo', 'sao bernanrdo do campo', 'sbdc', 'são caetano', 'sao caetano' 'são carlos', '*são carlos', 'são domingos do prata', 'são gabriel', 'são geraldo', 'são gonçalo do sapucaia', 'são joão daliança', 'sjd', 'são joão del rei', 'sjdr', 'são josé do rio preto', 'sjrp', 'são joão do rio preto', '*sjrp', 'são josé dos campos', 'são lourenço', 'são luiz gonzaga', 'slg', 'sp', 'são paulo', 'sao paulo', '*são paulo', '*sao paulo', '*sp', 'são tomé das letras', 'sao tome das letras', 'stdl', 'são vicente de minas', 'sao vicente de minas', 'svdm', 'seritinga', 'serraria', 'sete lagoas', 'silvanópolis', 'silvanopolis', 'sorocaba', 'taubaté', 'taubate', '*taubaté', '*taubate' 'teixeiras', 'teófilo otoni', 'teofilo otoni', 'timóteo', 'timoteo', 'torres', 'três corações', 'tres coraçoes', 'tres coracoes', '3 coraçoes', '3 coracoes', 'três marias', 'tres marias', '3 marias', 'uberaba', 'uberlândia', 'uberlandia', 'unaí', 'unai', 'uruaçu', 'uruaçú', 'vargem grande', 'varginha', 'viçosa', 'vila velha', 'virgem da lapa', 'vitória', 'vitória da conquista', 'vitoria da conquista', 'vdc', '*vitória da conquista', '*vitoria da conquista', '*vdc' 'volta redonda']
#
#Invocando as condições...
#

while True:
	eventos, valores = janela.read()
	if eventos == 'Sair' or sg.WINDOW_CLOSED: #caso o usuário feche a janela o loop para.
		break
	if eventos == 'Limpar':
		janela.close()
		janela = janela_inicial()
	if eventos == 'Pesquisar':
		#
		#VIAÇÃO COORDENADAS
		#
		if valores['-NOME-'].lower() in cidade_1 and valores['-NOME-'].lower() in tarifa_3:
			print('EMPRESA: VIAÇÃO COORDENADAS  -  ATUAL\n\nCONTATO: (32) 3112-0423 - GUICHÊS: 04 e 05\n\nSITE: https://www.saritur.com.br/\n\nFUNCIONAMENTO: dom a sex das 06h30 - 00h\nsab de 06h30 - 19h\n\nPLATAFORMA: 22')
			print('\nTARIFA DE EMBARQUE R$2,55')
		#
		elif valores['-NOME-'].lower() in cidade_1 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO COORDENADAS  -  ATUAL\n\nCONTATO: (32) 3112-0423 - GUICHÊS: 04 e 05\n\nSITE: https://www.saritur.com.br/\n\nFUNCIONAMENTO: dom a sex das 06h30 - 00H\nsab de 06h30 ás 19hn\n\nPLATAFORMA: 22')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO UTIL/BRISA/SAMPAIO
		#
		elif valores['-NOME-'].lower() in cidade_2 and valores['-NOME-'].lower() in tarifa_3:
			print('EMPRESA: VIAÇÃO UTIL / BRISA / SAMPAIO / GYPSYY / GUANABARA\n\nGUICHÊS: 20 à 24 - CONTATOS: 0800 883 8830\n\nSITE:\n\n	UTIL: https://www.util.com.br/\n	GUANABARA: https://www.viajeguanabara.com.br/\n	SAMPAIO: https://viacaosampaio.com.br/\n\nPLATAFORMAS: 13, 14, e 15')
			print('\nTARIFA DE EMBARQUE R$2,55')
		#
		elif valores['-NOME-'].lower() in cidade_2 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO UTIL / BRISA / SAMPAIO / GYPSYY / GUANABARA\n\nGUICHÊS: 20 à 24 - CONTATOS: 0800 883 8830\n\nSITE:\n\n	UTIL: https://www.util.com.br/\n	GUANABARA: https://www.viajeguanabara.com.br/\n	SAMPAIO: https://viacaosampaio.com.br/\n\nPLATAFORMAS: 13, 14, e 15')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001:
		#
		elif valores['-NOME-'].lower() in cidade_3 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001\n\nGUICHÊS 15 e 16 - CONTATO: 4004-9600 e 0800 942 0030\n\nSITE:\n	COMETA: https://www.cometa.com.br\n	CATARINENSE: https://www.catarinense.com.br\n	EXPRESSO DO SUL: https://www.expressodosul.com.br\n	1001: https://www.autoviacao1001.com.br\n\nFUNCIONAMENTO: DIARIAMENTE 07h30 - 23h30\n\nPLATAFORMAS: 10, 11 e 12')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO PROGRESSO:
		#
		elif valores['-NOME-'].lower() in cidade_4 and valores['-NOME-'].lower() in tarifa_1:
			print('EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30\n\nCONTATOS:\n	GUICHÊ:(32) 3215-5020\n	PANTUR:(32) 3216-2975\n	LOJA DO ZÉ KODAK: (32) 3025-3936\n\nSITE: https://www.viacaoprogresso.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 25 e 26')
			print('\nTARIFA DE EMBARQUE R$0,85')
		#
		elif valores['-NOME-'].lower() in cidade_4 and valores['-NOME-'].lower() in tarifa_2:
			print('EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30\n\nCONTATOS:\n	GUICHÊ:(32) 3215-5020\n	PANTUR:(32) 3216-2975\n	LOJA DO ZÉ KODAK: (32) 3025-3936\n\nSITE: https://www.viacaoprogresso.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 25 e 26')
			print('\nTARIFA DE EMBARQUE R$1,45')
		#
		elif valores['-NOME-'].lower() in cidade_4 and valores['-NOME-'].lower() in tarifa_3:
			print('EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30\n\nCONTATOS:\n	GUICHÊ:(32) 3215-5020\n	PANTUR:(32) 3216-2975\n	LOJA DO ZÉ KODAK: (32) 3025-3936\n\nSITE: https://www.viacaoprogresso.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 25 e 26')
			print('\nTARIFA DE EMBARQUE R$2,55')
		elif valores['-NOME-'].lower() in cidade_4:
			print('EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30\n\nCONTATOS:\n	GUICHÊ:(32) 3215-5020\n	PANTUR:(32) 3216-2975\n	LOJA DO ZÉ KODAK: (32) 3025-3936\n\nSITE: https://www.viacaoprogresso.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 25 e 26')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO UNIDA:
		#
		elif valores['-NOME-'].lower() in cidade_5 and valores['-NOME-'].lower() in tarifa_1:
			print('EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n\nCONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n\nFUNCIONAMENTO:\n	seg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n	dom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n\nPLATAFORMA: 23')
			print('\nTARIFA DE EMBARQUE R$0,85')
		#
		elif valores['-NOME-'].lower() in cidade_5 and valores['-NOME-'].lower() in tarifa_2:
			print('EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n\nCONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n\nFUNCIONAMENTO:\n	seg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n	dom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n\nPLATAFORMA: 23')
			print('\nTARIFA DE EMBARQUE R$1,45')
		#
		elif valores['-NOME-'].lower() in cidade_5 and valores['-NOME-'].lower() in tarifa_3:
			print('EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n\nCONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n\nFUNCIONAMENTO:\n	seg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n	dom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n\nPLATAFORMA: 23')
			print('\nTARIFA DE EMBARQUE R$2,55')
		#
		elif valores['-NOME-'].lower() in cidade_5 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n\nCONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n\nFUNCIONAMENTO:\n	seg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n	dom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n\nPLATAFORMA: 23')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO TRANSUR:
		#
		elif valores['-NOME-'].lower() in cidade_6 and valores['-NOME-'].lower() in tarifa_2:
			print('EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10\n\nCONTATO: (32) 3218-6313\n\nSITE: https://https://www.transur.com.br/horarios_preco\n\nFUNCIONAMENTO: DIARIAMENTE 06h30 - 19h\n\nPLATAFORMA: 17')
			print('\nTARIFA DE EMBARQUE R$1,45')
		#
		elif valores['-NOME-'].lower() in cidade_6 and valores['-NOME-'].lower() in tarifa_3:
			print('EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10\n\nCONTATO: (32) 3218-6313\n\nSITE: https://https://www.transur.com.br/horarios_preco\n\nFUNCIONAMENTO: DIARIAMENTE 06h30 - 19h\n\nPLATAFORMA: 17')
			print('\nTARIFA DE EMBARQUE R$2,55')
		#
		elif valores['-NOME-'].lower() in cidade_6 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10\n\nCONTATO: (32) 3218-6313\n\nSITE: https://https://www.transur.com.br/horarios_preco\n\nFUNCIONAMENTO: DIARIAMENTE 06h30 - 19h\n\nPLATAFORMA: 17')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO BASSAMAR:
		#
		elif valores['-NOME-'].lower() in cidade_7 and valores['-NOME-'].lower() in tarifa_1:
			print('EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31\n\nCONTATO: (32) 3215-5020\n\nSITE: https://www.viacaobassamar.queropassagem.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 19, 20, e 21')
			print('\nTARIFA DE EMBARQUE R$0,85')
		#
		elif valores['-NOME-'].lower() in cidade_7 and valores['-NOME-'].lower() in tarifa_2:
			print('EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31\n\nCONTATO: (32) 3215-5020\n\nSITE: https://www.viacaobassamar.queropassagem.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 19, 20, e 21')
			print('\nTARIFA DE EMBARQUE R$1,45')
		#
		elif valores['-NOME-'].lower() in cidade_7 and valores['-NOME-'].lower() in tarifa_3:
			print('EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31\n\nCONTATO: (32) 3215-5020\n\nSITE: https://www.viacaobassamar.queropassagem.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 19, 20, e 21')
			print('\nTARIFA DE EMBARQUE R$2,55')
			print('EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31\n\nCONTATO: (32) 3215-5020\n\nSITE: https://www.viacaobassamar.queropassagem.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 19, 20, e 21')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO RIO DOCE:
		#
		elif valores['-NOME-'].lower() in cidade_8 and valores['-NOME-'].lower() in tarifa_2:
			print('EMPRESA: VIAÇÃO RIO DOCE - GUICHÊ: 32\n\nCONTATO: (32)3215-8828\n\nSITE: http://www.viacaoriodoce.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 07h - 21h30\n\nPLATAFORMA: 24')
			print('\nTARIFA DE EMBARQUE R$1,45')
		#
		elif valores['-NOME-'].lower() in cidade_8 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO RIO DOCE - GUICHÊ: 32\n\nCONTATO: (32)3215-8828\n\nSITE: http://www.viacaoriodoce.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 07h - 21h30\n\nPLATAFORMA: 24')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO SANTA CRUZ / SUL MINAS:
		#
		elif valores['-NOME-'].lower() in cidade_9 and valores['-NOME-'].lower() in tarifa_2:
			print('EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3215-5020  -  GUICHÊ: 29\n\nSITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPlataforma: 16')
			print('\nTARIFA DE EMBARQUE R$1,45')
		#
		elif valores['-NOME-'].lower() in cidade_9 and valores['-NOME-'].lower() in tarifa_3:
			print('EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3215-5020  -  GUICHÊ: 29\n\nSITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPlataforma: 16')
			print('\nTARIFA DE EMBARQUE R$2,55')
		#
		elif valores['-NOME-'].lower() in cidade_9 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3215-5020  -  GUICHÊ: 29\n\nSITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPlataforma: 16')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO GONTIJO:
		#
		elif valores['-NOME-'].lower() in cidade_10 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO GONTIJO - GUICHÊ: 27\n\nCONTATO: (32) 3215-9458\n\nSITE: https://www.gontijo.com.br/\n\nFUNCIONAMENTO: seg- sab 08h - 20h20 / dom - feriados 08h - 12h / 14h - 17h20\n\nPLATAFORMA: 27')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO PARAIBUNA:
		#
		elif valores['-NOME-'].lower() in cidade_11 and valores['-NOME-'].lower() in tarifa_1:
			print('	EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n\nSITE: https://www.paraibunatransportes.com.br/\n\nFUNCIONAMENTO:\n\n	seg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\n	sab e dom: 05h15 - 10h30 - 11h30- 18h\n\nPLATAFORMA: 18')
			print('\nTARIFA DE EMBARQUE R$0,85')
		#
		elif valores['-NOME-'].lower() in cidade_11 and valores['-NOME-'].lower() in tarifa_2:
			print('	EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n\nSITE: https://www.paraibunatransportes.com.br/\n\nFUNCIONAMENTO:\n\n	seg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\n	sab e dom: 05h15 - 10h30 - 11h30- 18h\n\nPLATAFORMA: 18')
			print('\nTARIFA DE EMBARQUE R$1,45')
		#
		elif valores['-NOME-'].lower() in cidade_11 and valores['-NOME-'].lower() in tarifa_3:
			print('	EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n\nSITE: https://www.paraibunatransportes.com.br/\n\nFUNCIONAMENTO:\n\n	seg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\n	sab e dom: 05h15 - 10h30 - 11h30- 18h\n\nPLATAFORMA: 18')
		#
		elif valores['-NOME-'].lower() in cidade_11 and valores['-NOME-'].lower() in tarifa_4:
			print('	EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n\nSITE: https://www.paraibunatransportes.com.br/\n\nFUNCIONAMENTO:\n\n	seg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\n	sab e dom: 05h15 - 10h30 - 11h30- 18h\n\nPLATAFORMA: 18')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÂO EXPRESSO UNIÂO PLUMA:
		#
		elif valores['-NOME-'].lower() in cidade_12 and valores['-NOME-'].lower() in tarifa_4:
			print('EMPRESA: VIAÇÃO EXPRESSO UNIÃO / PLUMA - GUICHÊ: 25\n\nCONTATO: (32) 98710-6414\n\nSITE: https://www.expressouniao.com.br\n\nFUNCIONAMENTO:\n\n	seg - sex 09h - 18h\n	sab dom feriados 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 29')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO UNICA:
		#
		elif valores['-NOME-'].lower() in cidade_13 and valores['-NOME-'].lower() in tarifa_3:
			print('	EMPRESA: VIAÇÃO UNICA FACIL - GUICHÊ: 14\n\nCONTATOS:\n\n	Central: (24) 2244-1642(32)\n	PANTUR: 3216-2975\n\nSITE: http://www.unica-facil.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 06h30 - 12h / 14h - 18h30\n\nPLATAFORMA: 19')
			print('\nTARIFA DE EMBARQUE R$2,55')
		#
		elif valores['-NOME-'].lower() in cidade_13 and valores['-NOME-'].lower() in tarifa_4:
			print('	EMPRESA: VIAÇÃO UNICA FACIL - GUICHÊ: 14\n\nCONTATOS:\n\n	Central: (24) 2244-1642(32)\n	PANTUR: 3216-2975\n\nSITE: http://www.unica-facil.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 06h30 - 12h / 14h - 18h30\n\nPLATAFORMA: 19')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO JOSÉ MARIA RODRIGUES:
		#
		elif valores['-NOME-'].lower() in cidade_14 and valores['-NOME-'].lower() in tarifa_1:
			print('EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n\nSITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n\nPLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO")')
			print('\nTARIFA DE EMBARQUE R$0,85')
		#
		elif valores['-NOME-'].lower() in cidade_14 and valores['-NOME-'].lower() in tarifa_2:
			print('EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n\nSITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n\nPLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO")')
			print('\nTARIFA DE EMBARQUE R$1,45')
		#
		elif valores['-NOME-'].lower() in cidade_14 and valores['-NOME-'].lower() in tarifa_3:
			print('EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n\nSITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n\nPLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO")')
			print('\nTARIFA DE EMBARQUE R$2,55')
		#
		#VIAÇÃO ÁGUIA BRANCA:
		#
		elif valores['-NOME-'].lower() in cidade_15 and valores['-NOME-'].lower() in tarifa_4:
			print('	EMPRESA: VIAÇÃO ÀGUIA BRANCA - GUICHÊ 26\n\nCONTATO:(32) 98710-6414\n\nSITE: https://www.aguiabranca.com.br\n\nFUNCIONAMENTO:\n\n	seg - sex 09h - 18h\n	sab 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 12')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		#VIAÇÃO ITAPEMIRIM / KAISSARA:
		#
		elif valores['-NOME-'].lower() in cidade_16:
			print('	EMPRESA: VIAÇÃO ITAPEMIRIM / KAISSARA - GUICHÊ: 29\n\nCONTATOS: (32)3215-5020 \n\nFUNCIONAMENTO:\n\n	seg - sab 06h - 19h\n	dom 07h - 22h\n\nPLATAFORMA: 28')
			print('\nTARIFA DE EMBARQUE R$5,25')
		#
		# LISTA DE ORGÃOS PÚBLICOS,LOJAS, E GUICHÊS NO INTERIOR DO TRJFA:
		#
		elif valores['-NOME-'].lower() == 'inss' or valores['-NOME-'].lower() == 'previdencia' or valores['-NOME-'].lower() == 'previdência' or valores['-NOME-'].lower() == 'previdência social':
			print('	AGÊNCIA INSS TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO: seg à sex de 07h àS 13h\n\nAGENDAMENTO: gov.br/meuinss  ou 135')
		#
		elif valores['-NOME-'].lower() == 'conselho tutelar' or valores['-NOME-'].lower() == 'juizado de menores' or valores['-NOME-'].lower() == 'juizado menores':
			print('AGÊNCIA DO CONSELHO TUTELAR NO TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO:  seg à sex de 08h ás 12h e de 14h às 18h\n\nCONTATO: (32)3690-7398\n\nATENDIMENTO DE PLANTÃO: (32)98429-4740')
		#
		elif valores['-NOME-'].lower() == 'smu':
			print('AGÊNCIA SMU TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO: seg à sex de 08h às 11h e de 14h às 17h\n\nCONTATO: (32)3690-2806')
		#
		elif valores['-NOME-'].lower() == 'antt':
			print('AGÊNCIA ANTT TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO: "PROVISORIAMENTE SUSPENSO!!!"\n\nCONTATO: 166 (OUVIDORIA)')
		#
		elif valores['-NOME-'].lower() == 'guarda municipal' or valores['-NOME-'].lower() == 'gm':
			print('GUARDA MUNICIPAL DE JUIZ DE FORA\n\n\nCONTATO: 153 ou (32)3690-7137')
		#
		elif valores['-NOME-'].lower() == 'cargas util' or valores['-NOME-'].lower() == 'util cargas':
			print('\n\n\n	CARGAS UTIL TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\n	ATENDIMENTO: seg à sex de 08h às 18h - sáb 08h à 12h\n\n	Responsável: WAGNER ou VIVIAN\n\n	CONTATOS: (32)99828-0380')
		#
		elif valores['-NOME-'].lower() == 'encomendas ceu' or valores['-NOME-'].lower() == 'ceu encomendas' or valores['-NOME-'].lower() == 'ceu' or valores['-NOME-'].lower() == 'andré' or valores['-NOME-'].lower() == 'andre' or valores['-NOME-'].lower() == 'André' or valores['-NOME-'].lower() == 'Andre':
			print('CEU ENCOMENDAS TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO: seg à sex de 08h:30 às 17h (ANDRÉ)\n\nCONTATO-WHATSAPP (32)98831-3602')
		#
		elif valores['-NOME-'].lower() == 'cargas resendense' or valores['-NOME-'].lower() == 'resendense cargas' or valores['-NOME-'].lower() == 'resendense':
			print('CARGAS RESENDENSE TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO: seg à sex de 08h:30 às 12h (RESENDE)\n\nCONTATOS: (32)3084-4346 - https://resendensecargas.spaceblog.com.br')
		#
		elif valores['-NOME-'].lower() == 'edimar despachante' or valores['-NOME-'].lower() == 'edimar' or valores['-NOME-'].lower() == 'despachante':
			print('EDIMAR DESPACHANTE TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO: seg à sex de 07h às 18h (EDIMAR)\n\nCONTATOS: (32)99175-3064')
		#
		elif valores['-NOME-'].lower() == 'migração' or valores['-NOME-'].lower() == 'centro pop' or valores['-NOME-'].lower() == 'migracao' or valores['-NOME-'].lower() == 'migraçao':
			print('MIGRAÇÃO TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO: seg à qui de 09h às 15h - sex de 13h às 15h\n\nCONTATOS: (32)3690-7102\n\nCENTRO POP - RUA SETE DE SETEMBRO 1341 (CENTRO)\n\nFUNCIONAMENTO: 06h:30 Às 18h')
		#
		elif valores['-NOME-'].lower() == 'balcão' or valores['-NOME-'].lower() == 'balcao' or valores['-NOME-'].lower() == 'amd' or valores['-NOME-'].lower() == 'amd balcão' or valores['-NOME-'].lower() == 'amd balcao' or valores['-NOME-'].lower() == 'rodoviaria' or valores['-NOME-'].lower() == 'balcao rodoviaria' or valores['-NOME-'].lower() == 'amd services':
			print('AMD SERVICES BALCÃO DE INFORMAÇÕES TERMINAL RODOVIÁRIO MIGUEL MANSUR\n\nATENDIMENTO: seg à seg 24h\n\n\nCONTATOS: (32) 3217-2828\n\n\nAv Brasil nº 9501 Bairro São Dimas Cep: 36080-060')
		#
		elif valores['-NOME-'].lower() == 'adm' or valores['-NOME-'].lower() == 'secretaria' or valores['-NOME-'].lower() == 'administração' or valores['-NOME-'].lower() == 'administraçao' or valores['-NOME-'].lower() == 'administracao' or valores['-NOME-'].lower() == 'adm amd' or valores['-NOME-'].lower() == 'secretaria' or valores['-NOME-'].lower() == 'diretoria':
			print(' * ADMINISTRATIVO TERMINAL RODOVIÁRIO MIGUEL MANSUR * \n\nATENDIMENTO: seg à sex 9h às 18h\n\nEndereço: Av Brasil nº 9501, Bairro São Dimas Cep: 36080-060\n\n(OBS: FAVOR ANOTAR RECADO, CASO SEJA FINAL DE SEMANA OU FERIADO)')
		#
		elif valores['-NOME-'].lower() == 'mensalista' or valores['-NOME-'].lower() == 'estacionamento' or valores['-NOME-'].lower() == 'mensalidade estacionamento' or valores['-NOME-'].lower() == 'estacionamento pago' or valores['-NOME-'].lower() == 'estacionamento mensalista':
			print('	=-=-=- MENSALISTA ESTACIONAMENTO =-=-=-\n\nDocumentos Necessários:\n\n	> CNH\n	> Documento do veículo\n	> Comprovante de residência\n	> Contatos (telefone e e-mail)\n\nValor da mensalidade: R$ 145,00\n\nPermanência: Mínimo de 03 meses\n\nProcurar o setor ADMINISTRATIVO da AMD ASERVICES seg a sex de 9h às 18h')
		#
		elif valores['-NOME-'].lower() == 'rei do mate' or valores['-NOME-'].lower() == 'rdm' or valores['-NOME-'].lower() == 'rm':
			print('		-=-=-= LANCHONETE REI DO MATE -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: 24h (exceto nas madrugadas de sab para dom)\n\nContato: (32) 99958-2881\n\nResponsável: Fabiano')
		#
		elif valores['-NOME-'].lower() == 'cacau show' or valores['-NOME-'].lower() == 'cacau' or valores['-NOME-'].lower() == 'chocolateria':
			print('		-=-=-= CACAU SHOW -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: seg à seg 06h às 23h\n\nContato: (32) 99822-6153\n\nResponsável: Fabiano')
		#
		elif valores['-NOME-'].lower() == 'livraria nobel' or valores['-NOME-'].lower() == 'livraria' or valores['-NOME-'].lower() == 'nobel' or valores['-NOME-'].lower() == 'nobel livraria':
			print('		-=-=-= LIVRARIA NOBEL -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: seg à seg 06h às 23h\n\nContato: (32) 99828-7634\n\nResponsável: Fabiano')
		#
		elif valores['-NOME-'].lower() == 'empório rural' or valores['-NOME-'].lower() == 'empório' or valores['-NOME-'].lower() == 'emporio rural' or valores['-NOME-'].lower() == 'emporio' or valores['-NOME-'].lower() == 'rural':
			print('		-=-=-= EMPÓRIO RURAL -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: 08h às 19h\n\nContato: "NÃO INFORMADO!"\n\nResponsável: Neiva')
		#
		elif valores['-NOME-'].lower() == 'bomboniere' or valores['-NOME-'].lower() == 'bomboniere vitória' or valores['-NOME-'].lower() == 'bomboniere vitoria' or valores['-NOME-'].lower() == 'vitória' or valores['-NOME-'].lower() == 'vitoria':
			print('		-=-=-= BOMBONIERE VITÓRIA -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: dom à dom 05h e 30 às 22h\n\nContato: "NÃO INFORMADO!"\n\nResponsável: Côrrea')
		#
		elif valores['-NOME-'].lower() == 'pastelaria' or valores['-NOME-'].lower() == 'princesa dos pasteis' or valores['-NOME-'].lower() == 'princesa dos pastéis' or valores['-NOME-'].lower() == 'pastelaria correa' or valores['-NOME-'].lower() == 'pastelaria côrrea' or valores['-NOME-'].lower() == 'pastelariacorrea':
			print('		-=-=-= PASTELARIA PRINCESA DOS PASTÉIS -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: 24h por dia 7 dias da semana\n\nContato: "NÃO INFORMADO!"\n\nResponsável: Côrrea')
		#
		elif valores['-NOME-'].lower() == 'lanchonete' or valores['-NOME-'].lower() == 'santa lúcia' or valores['-NOME-'].lower() == 'lsl' or valores['-NOME-'].lower() == 'santa lucia' or valores['-NOME-'].lower() == 'lanchonete santa lucia' or valores['-NOME-'].lower() == 'snt lúcia' or valores['-NOME-'].lower() == 'snt lucia' or valores['-NOME-'].lower() == 'mercantil oliveira e côrrea' or valores['-NOME-'].lower() == 'mercantil oliveira e correa' or valores['-NOME-'].lower() == 'santalucia':
			print('		-=-=-= LANCHONETE SANTA LÚCIA -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: dom à dom 05h e 30 às 22h\n\nContato: "NÃO INFORMADO!"\n\nResponsável: Côrrea')
		#
		elif valores['-NOME-'].lower() == 'farmácia' or valores['-NOME-'].lower() == 'farmacia' or valores['-NOME-'].lower() == 'farmaciaki' or valores['-NOME-'].lower() == 'farmacia farmaciaki' or valores['-NOME-'].lower() == 'farmaciaki farmacia':
			print('			-=-=-= FARMÁCIA =-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nTEMPORARIAMENTE NÃO HÁ FARMÁCIA NO TERMINAL RODOVIÁRIO')
		#
		elif valores['-NOME-'].lower() == 'poderosa' or valores['-NOME-'].lower() == 'loja poderosa' or valores['-NOME-'].lower() == 'poderosa loja' or valores['-NOME-'].lower() == 'poderosa presentes' or valores['-NOME-'].lower() == 'loja poderosa presentes' or valores['-NOME-'].lower() == 'lpp' or valores['-NOME-'].lower() == 'poderosapresentes':
			print('		-=-=-= PODEROSA PRESENTES -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: seg à seg 7h às 20h\n\nContato: (32) 3214-1310 (WHATS APP)\n\nResponsável: "NÃO INFORMADO"')
		#
		elif valores['-NOME-'].lower() == 'belinha' or valores['-NOME-'].lower() == 'belinha eletrônicos' or valores['-NOME-'].lower() == 'belinha eletronicos' or valores['-NOME-'].lower() == 'belinhaeletrônicos' or valores['-NOME-'].lower() == 'belinhaeletronicos' or valores['-NOME-'].lower() == 'eletronicos' or valores['-NOME-'].lower() == 'eletrônicos':
			print('		-=-=-= BELINHA ELETRÔNICOS -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: seg à seg 7h às 20h\n\nContato: (32) 3212-8042\n\nResponsável: Mauro')
		#
		elif valores['-NOME-'].lower() == 'padaria' or valores['-NOME-'].lower() == 'estacao mineira' or valores['-NOME-'].lower() == 'estação mineira' or valores['-NOME-'].lower() == 'estaçao mineira':
			print('		-=-=-= PADARIA ESTAÇÃO MINEIRA -=-=-=\n\nLocal: Terminal Rodoviário Miguel Mansur\n\nFuncionamento: 24h (exceto nas madrugadas de sab para dom)\n\nContato: (**) *****-****\n\nResponsável: Wagner / Adriana')
		#
		#GLOSSÁRIO TERMINAL RODOVIÁRIO...
		#
		elif valores['-NOME-'].lower() == 'p1' or valores['-NOME-'].lower() == 'p 1' or valores['-NOME-'].lower() == 'p01' or valores['-NOME-'].lower() == 'p 01':
			print('>>> P1:\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE À ENTRADA PRINCIPAL DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\nESSA ÁREA ABRANGE DESDE O TERMINAL DO PONTO DE ÔNIBUS URBANO À CAPELA, PASSANDO TAMBÉM PELAS LOJAS DA ENTRADA DO TERMINAL RODOVIÁRIO.')
		#
		elif valores['-NOME-'].lower() == 'p2' or valores['-NOME-'].lower() == 'p 2' or valores['-NOME-'].lower() == 'p02' or valores['-NOME-'].lower() == 'p 02':
			print('>>> P2:\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE À SAÍDA PRINCIPAL DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\nESSA ÁREA ABRANGE DESDE A CORRENTE DE ENTRADA DO CARGA E DESCARGA, AO CORREDOR DOS FUNDOS PRÓXIMO A SUBSTAÇÃO DE ENERGIA')
		#
		elif valores['-NOME-'].lower() == 'p3' or valores['-NOME-'].lower() == 'p 3' or valores['-NOME-'].lower() == 'p03' or valores['-NOME-'].lower() == 'p 03':
			print('>>> P3:\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE AO DESEMBARQUE DE PASSAGEIROS NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\nESSA ÁREA ABRANGE DESDE AS PLAFORMAS DE 1 À 8, ATÉ PRÓXIMO À LOJA DO REI DO MATE')
		#
		elif valores['-NOME-'].lower() == 'p4' or valores['-NOME-'].lower() == 'p 4' or valores['-NOME-'].lower() == 'p04' or valores['-NOME-'].lower() == 'p 04':
			print('>>> P4:\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE AO EMBARQUE DE PASSAGEIROS NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\nESSA ÁREA ABRANGE DESDE AS PLATAFORMAAS DE 9 À 31, ATÉ AS ROLETAS OU CATRACAS DE EMBARQUE')
		#
		elif valores['-NOME-'].lower() == 'p5' or valores['-NOME-'].lower() == 'p 5' or valores['-NOME-'].lower() == 'p05' or valores['-NOME-'].lower() == 'p 05':
			print('>>> P5:\n\nCÓDIGO REFERENTE AOS SETORES PERTINENTES AOS SANITÁRIOS (PAGOS E GRATUITOS) DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA')
		#
		elif valores['-NOME-'].lower() == 'p6' or valores['-NOME-'].lower() == 'p 6' or valores['-NOME-'].lower() == 'p06' or valores['-NOME-'].lower() == 'p 06':
			print('>>> P6:\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE À ADMINISTRAÇÃO DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\nNO P6 SE ENCONTRA OS SETORES DE ENGENHARIA, BRIGADA, SALA DOS SUPERVISORES, SECRETARIA E A DIRETORIA DA AMD')
		#
		elif valores['-NOME-'].lower() == 'p7' or valores['-NOME-'].lower() == 'p 7' or valores['-NOME-'].lower() == 'p07' or valores['-NOME-'].lower() == 'p 07':
			print('>>> P7:\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE AO ESTACIONAMENTO DO TERMINAL RODOVIÁRIO DE JUIZ DE FORA\n\nESTACIONAMENTO PAGO, EM CASO DE DÚVIDAS SOBRE ADESÃO DE NOVOS MENSALISTAS, PESQUISAR PELA PALAVRA CHAVE "MENSALISTA"')
		#
		elif valores['-NOME-'].lower() == 'p8' or valores['-NOME-'].lower() == 'p 8' or valores['-NOME-'].lower() == 'p08' or valores['-NOME-'].lower() == 'p 08':
			print('>>> P8:\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE AO REFEITÓRIO NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA')
		#
		elif valores['-NOME-'].lower() == 'p9' or valores['-NOME-'].lower() == 'p 9' or valores['-NOME-'].lower() == 'p09' or valores['-NOME-'].lower() == 'p 09':
			print('>>> P8:\n\nCÓDIGO REFERENTE AO SETOR PERTINENTE DO ALMOXARIFADO NO TERMINAL RODOVIÁRIO DE JUIZ DE FORA')
		#
		#RELAÇÃO DOS GUICHÊS E SEUS DADOS...
		#
		elif valores['-NOME-'].lower() == 'saritur' or valores['-NOME-'].lower() == 'Saritur' or valores['-NOME-'].lower() == 'Coordenadas' or valores['-NOME-'].lower() == 'coordenadas' or valores['-NOME-'].lower() == 'Atual' or valores['-NOME-'].lower() == 'atual':
			print('EMPRESA: VIAÇÃO COORDENADAS  -  ATUAL - SARITUR\n\nCONTATO: (32) 3112-0423 - GUICHÊS: 04 e 05\n\nSITE: https://www.saritur.com.br/\n\nFUNCIONAMENTO: dom a sex das 06h30 - 00h\nsab de 06h30 - 19h\n\nPLATAFORMA: 22')
		#
		elif valores['-NOME-'].lower() == 'util' or valores['-NOME-'].lower() == 'brisa' or valores['-NOME-'].lower() == 'guanabara' or valores['-NOME-'].lower() == 'sampaio' or valores['-NOME-'].lower() == 'gypsyy':
			print('EMPRESA: VIAÇÃO UTIL / BRISA / SAMPAIO / GYPSYY / GUANABARA\n\nGUICHÊS: 20 à 24 - CONTATOS: 0800 883 8830\n\nSITE:\n\n	UTIL: https://www.util.com.br/\n	GUANABARA: https://www.viajeguanabara.com.br/\n	SAMPAIO: https://viacaosampaio.com.br/\n\nPLATAFORMAS: 13, 14, e 15')
		#
		elif valores['-NOME-'].lower() == 'cometa' or valores['-NOME-'].lower() == 'catarinense' or valores['-NOME-'].lower() == 'expresso do sul' or valores['-NOME-'].lower() == '1001':
			print('EMPRESA: VIAÇÃO COMETA / CATARINENSE / EXPRESSO DO SUL / 1001\n\nGUICHÊS 15 e 16 - CONTATO: 4004-9600 e 0800 942 0030\n\nSITE:\n	COMETA: https://www.cometa.com.br\n	CATARINENSE: https://www.catarinense.com.br\n	EXPRESSO DO SUL: https://www.expressodosul.com.br\n	1001: https://www.autoviacao1001.com.br\n\nFUNCIONAMENTO: DIARIAMENTE 07h30 - 23h30\n\nPLATAFORMAS: 10, 11 e 12')
		#
		elif valores['-NOME-'].lower() == 'progresso' or valores['-NOME-'].lower() == 'viação progresso' or valores['-NOME-'].lower() == 'viaçao progresso' or valores['-NOME-'].lower() == 'viacao progresso':
			print('EMPRESA: VIAÇÃO PROGRESSO - GUICHÊ: 30\n\nCONTATOS:\n	GUICHÊ:(32) 3215-5020\n	PANTUR:(32) 3216-2975\n	LOJA DO ZÉ KODAK: (32) 3025-3936\n\nSITE: https://www.viacaoprogresso.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 25 e 26')
		#
		elif valores['-NOME-'].lower() == 'unida' or valores['-NOME-'].lower() == 'viação unida' or valores['-NOME-'].lower() == 'unida mansur' or valores['-NOME-'].lower() == 'unidamansur':
			print('EMPRESA: VIAÇÃO UNIDA - GUICHÊS: 17, 18 e 19\n\nCONTATO: (32) 3215-3427\n\nSITE: https://unidamansur.queropassagem.com.br\n\nFUNCIONAMENTO:\n	seg - sab 05h15 - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n	dom 07h - 11h30 / 12h30 - 21h30 / 22h30 - 23h\n\nPLATAFORMA: 23')
		#
		elif valores['-NOME-'].lower() == 'transur' or valores['-NOME-'].lower() == 'viação transur':
			print('EMPRESA: VIAÇÃO TRANSUR - GUICHÊS: 09 e 10\n\nCONTATO: (32) 3218-6313\n\nSITE: https://https://www.transur.com.br/horarios_preco\n\nFUNCIONAMENTO: DIARIAMENTE 06h30 - 19h\n\nPLATAFORMA: 17')
		#
		elif valores['-NOME-'].lower() == 'bassamar' or valores['-NOME-'].lower() == 'viação bassamar' or valores['-NOME-'].lower() == 'viacao bassamar':
			print('EMPRESA: VIAÇÃO BASSAMAR - GUICHÊ: 31\n\nCONTATO: (32) 3215-5020\n\nSITE: https://www.viacaobassamar.queropassagem.com.br\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPLATAFORMAS: 19, 20, e 21')
		#
		elif valores['-NOME-'].lower() == 'rio doce' or valores['-NOME-'].lower() == 'riodoce':
			print('EMPRESA: VIAÇÃO RIO DOCE - GUICHÊ: 32\n\nCONTATO: (32)3215-8828\n\nSITE: http://www.viacaoriodoce.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 07h - 21h30\n\nPLATAFORMA: 24')
		#
		elif valores['-NOME-'].lower() == 'santa cruz' or valores['-NOME-'].lower() == 'snta cruz'  or valores['-NOME-'].lower() == 'sntacruz'  or valores['-NOME-'].lower() == 'santacruz' or valores['-NOME-'].lower() == 'sul minas' or valores['-NOME-'].lower() == 'sulminas':
			print('EMPRESA: VIAÇÃO SANTA CRUZ  -  SUL MINAS\n\nCONTATO: (32) 3215-5020  -  GUICHÊ: 29\n\nSITE: https://viajesantacruz.com.br/\n\nFUNCIONAMENTO: seg - sab 06h - 19h / dom 07h - 22h\n\nPlataforma: 16')
		#
		elif valores['-NOME-'].lower() == 'gontijo':
			print('EMPRESA: VIAÇÃO GONTIJO - GUICHÊ: 27\n\nCONTATO: (32) 3215-9458\n\nSITE: https://www.gontijo.com.br/\n\nFUNCIONAMENTO:\n\n	seg- sab 08h - 20h20\n	dom - feriados 08h - 12h / 14h - 17h20\n\nPLATAFORMA: 27')
		#
		elif valores['-NOME-'].lower() == 'paraibuna':
			print('EMPRESA: VIAÇÃO PARAIBUNA - GUICHÊS: 12 e 13\n\nCONTATO: (32) 2101-3314 / (32) 3216-2975(PANTUR) / (32)2101-3333\n\nSITE: https://www.paraibunatransportes.com.br/\n\nFUNCIONAMENTO:\n\n	seg à qui: 05h45 - 10h30 - 11h30 às 18h\n	sex: 05h45 - 10h30 - 11h30 - 14h e 15h15 - 19h\n	sab e dom: 05h15 - 10h30 - 11h30- 18h\n\nPLATAFORMA: 18')
		#
		elif valores['-NOME-'].lower() == 'união' or valores['-NOME-'].lower() == 'uniao' or valores['-NOME-'].lower() == 'expresso união' or valores['-NOME-'].lower() == 'expresso uniao' or valores['-NOME-'].lower() == 'expressounião' or valores['-NOME-'].lower() == 'expressouniao' or valores['-NOME-'].lower() == 'pluma':
			print('EMPRESA: VIAÇÃO EXPRESSO UNIÃO / PLUMA - GUICHÊ: 25\n\nCONTATO: (32) 98710-6414\n\nSITE: https://www.expressouniao.com.br\n\nFUNCIONAMENTO:\n\n	seg - sex 09h - 18h\n	sab dom feriados 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 29')
		#
		elif valores['-NOME-'].lower() == 'unica':
			print('	EMPRESA: VIAÇÃO UNICA FACIL - GUICHÊ: 14\n\nCONTATOS:\n\n	Central: (24) 2244-1642(32)\n	PANTUR: 3216-2975\n\nSITE: http://www.unica-facil.com.br/\n\nFUNCIONAMENTO: DIARIAMENTE 06h30 - 12h / 14h - 18h30\n\nPLATAFORMA: 19')
		#
		elif valores['-NOME-'].lower() == 'josé maria rodrigues' or valores['-NOME-'].lower() == 'jose maria rodrigues' or valores['-NOME-'].lower() == 'josemariarodrigues' or valores['-NOME-'].lower() == 'jmr':
			print('EMPRESA: VIAÇÃO JOSÉ MARIA RODRIGUES - GUICHÊ 06 e 07\n\nCONTATO: (32)3215-4460 / (32) 3221-3232\n\nSITE: https://www.josemariarodrigues.com.br\n\nFUNCIONAMENTO: seg - qui 07h - 20h / sex, sáb e dom 07h - 21h30\n\nPLATAFORMAS: 9 e 20 (Plataforma 20 "CONEXÂO AEROPORTO")')
		#
		elif valores['-NOME-'].lower() == 'águia branca' or valores['-NOME-'].lower() == 'aguia branca' or valores['-NOME-'].lower() == 'aguiabranca':
			print('	EMPRESA: VIAÇÃO ÁGUIA BRANCA - GUICHÊ 26\n\nCONTATO:(32) 98710-6414\n\nSITE: https://www.aguiabranca.com.br\n\nFUNCIONAMENTO:\n\n	seg - sex 09h - 18h\n	sab 14h - 18h (Intervalo: 12h30 - 13h30)\n\nPLATAFORMA: 12')
		#
		elif valores['-NOME-'].lower() == 'itapemirim' or valores['-NOME-'].lower == 'kaissara':
			print('	EMPRESA: VIAÇÃO ITAPEMIRIM / KAISSARA - GUICHÊ: 29\n\nCONTATOS: (32)3215-5020 \n\nFUNCIONAMENTO:\n\n	seg - sab 06h - 19h\n	dom 07h - 22h\n\nPLATAFORMA: 28')
		#
		#EM CASO DE NÃO CONFORMIDADE...
		else: 
			print('\nCONFIRA O NOME DA PESQUISA, E TENTE NOVAMENTE!\n\nPOSSIBILIDADE DE NÃO HAVER EMBARQUE PARA ESSE DESTINO NO TRJDF!\n\nPOSSIBILIDADE DE NÃO CONSTAR NO BANCO DE DADOS DO PROGRAMA\n\nCLIQUE EM LIMPAR PARA NOVA PESQUISA!')
#
janela.Close()