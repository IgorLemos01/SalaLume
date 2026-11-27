# Sala Lume

Site institucional da Sala Lume, um ecossistema de sala de aula inteligente: tela interativa, dispositivos 1:1, agente de IA para cada aluno, correção de tarefas manuscritas e conteúdos educacionais abertos.

## Páginas

| Arquivo | Conteúdo |
|---|---|
| `index.html` | Início: apresentação, as quatro frentes e os públicos |
| `como-funciona.html` | Ambiente da sala, princípios pedagógicos e ciclo de aprendizagem |
| `agente-ia.html` | Agente de IA para aluno, professor e gestão; trilhas de talento e reforço |
| `escrita-a-mao.html` | Digitalização e diagnóstico de provas e tarefas manuscritas |
| `conteudos.html` | Curadoria por habilidade da BNCC e acervo do MEC e de recursos abertos |
| `na-escola.html` | Níveis de atuação, ciclos de revisão e formação docente |
| `contato.html` | Formulário para agendar apresentação |

## Estrutura

```
docs/            site pronto para publicar (gerado pelo build)
src/
  pages/         conteúdo de cada página
  styles.css     estilos compartilhados
  app.js         menu, abas e validação do formulário
  icons.svg.part ícones SVG
  build.py       monta as páginas com cabeçalho e rodapé comuns
assets/          logo em SVG e PNG (normal, branca e símbolo)
design-system/   design system gerado com a skill UI/UX Pro Max
```

## Gerar o site

Edite os arquivos em `src/` e rode:

```bash
python3 src/build.py
```

O resultado vai para `docs/`. Não edite `docs/` à mão, porque o build sobrescreve a pasta.

## Publicar no GitHub Pages

Em **Settings › Pages**, escolha a branch `main` e a pasta `/docs`.

## Identidade visual

- Azul institucional `#0258A3`: marca, navegação e destaques
- Branco `#FEFEFE`: fundos
- Amarelo `#FEAA03`: botões de ação e detalhes (texto escuro `#0A2342` sobre ele)
- Tipografia: Nunito (títulos), DM Sans (texto) e Caveat (só para simular escrita à mão)

## Pendências

- O formulário de contato valida os campos, mas ainda não envia os dados. É preciso conectá-lo a um e-mail, CRM ou serviço de formulários.
- Os números dos painéis de exemplo são ilustrativos.
