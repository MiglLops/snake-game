"SNAKE GAME.PY" -- VERSAO FINAL (17/02/2025)
--SNAKE GAME--
*--resumo--*
- Snake Game, meu primeiro jogo em python.

--MAIN.PY-- 27/01/2025 (N/A)
- Versao 1.0 crua do jogo com varios pontos faltando mas com a ideia base sendo colocada na pratica da forma certa usando o tutorial do "Canal Hashtag" como guia.

--SNAKE GAME 1.1-- 27/01/2025 (20:57)
- Versao 1.1 do jogo com alteracoes no fundo e na fruta do jogo (agora no formato circular)
- Alterado a cor da pontuacao (Branco -> Preto);
- Formato da fruta circular e com a cor vermelhal;
- Fundo colorido;
- Cobra na cor azul;
- Input basico com a sinalizacao que voce perdeu;
- Alteracao no tamanho dos pixels para facilitar a vizualizacao (10 -> 20).

--SNAKE GAME 1.2-- 28/01/2025 (14:27)
- Versao 1.2 traz um menu simples antes do jogo comecar com duas alternativas de resolucao e uma tela de Game Over
- *Tela de resolucoes*
- Escolha entre duas resolucoes (600x400 - Recomendada e original // 1200x800 - Resolucao e dificuldade maior);
- Resolucao 1200x800 *nao* aumenta o mapa (mapa 2x maior).
- *Tela Game Over*
- Exibe a quantidade de pontos obtidos;
- Aperte "R" para Reiniciar o jogo do zero;
- Aperte "Q"para Sair do jogo.

--SNAKE GAME 1.3-- 30/01/2025 - 31/01/2025 (14:05)
- Versao 1.3 trouxe uma tela inicial e modificacoes na movimentacao da cobra
- *Tela Inicial*
- Opcao de "Start" que inicia o jogo;
- Opcao de "Quit/Sair" que fecha o jogo;
- Secret: Caso voce clique na comida da cobra ela trocara as cores (cobra azul -> vermelha e comida vermelha -> azul) e isso afetara no gameplay fazendo o player ser a comida e a comida ser  o player;
-*Alteracao na movimentacao*
- A velocidadade mudara de acordo que voce coma as frutas;
- Velocidade inicial = 5;
- De 5 de velocidade ate 10 cada fruta lhe da um aumento de 1 na velocidade;
- A partir de 11 de velocidade cada fruta lhe dara um aumento de 0.5 na velocidade.
- -**Removido a tela de troca de resolucoes,deixando apenas a resolucao 600x400 como padrao**-

--SNAKE GAME 1.4-- 15/02/2025 - 17/02/2025 (19:38)
-Versao 1.4 trouxe o retorno de uma tela de configuracoes que ja foi vista em veroes passadas com a modificacao na velocidade da cobra e tamanho do mapa.
- *Tela de Configuracao*
- Opcoes de niveis de velocidade:
- NV 1 - VEL = 1;
- NV 2 (padrao) - VEL = 5;
- NV 3 - VEL = 15.
- Opcoes de tamanho do mapa (quadrados):
- NV 1 - Escala grande (facil);
- NV 2 - Escala padrao (medio);
- NV 3 - Escala extra pequena (dificil).
- *Adicoes no Jogo*
- Caso o tamanho da mapa seja "NV 1" ou "NV 2" a cobra nao morre se bater na parede mas sim saira na outra extremidade;
- Se o jogador pressionar "ESC" durante o jogo, ele voltara para a tela inicial;
- Adicionado um texto que exibe a velocidade do jogador;
- Um pixel verde ao lado superior esquerdo da fruta.
- *Tela Game Over*
- Agora existe uma tela de Game Over melhor,adicionando a opcao de click "Resetar - Sair" ou apertar "R - Q";
