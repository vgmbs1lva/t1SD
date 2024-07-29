# Trabalho 3, 4 e 5 de Compiladores 2024/1

**Atenção**: Importante ressaltar que o trabalho que será entregue no T3 é o mesmo do T5. Como adiantamos o T5, e os casos de teste funcionam no T3 e T4, utilizaremos o mesmo nesses trabalhos. Por conta disso, verá implementações referentes ao T4 e T5 nas linhas de código, como também nas classes e funções.

### Grupo:
- Matheus Rezende Milani Videira - 790809
- Mauricio Herrera Fontes - 790986
- Victor Germano Moreira Batista da Silva - 769775

### Requisitos:
Para realizar o trabalho foram utilizados os seguintes programas:

| Nome do programa | Versão | Link para download |
|------------------|--------|--------------------|
| NetBeans | 12.6 | [Windows](https://www.apache.org/dyn/closer.cgi/netbeans/netbeans-installers/12.6/Apache-NetBeans-12.6-bin-windows-x64.exe) \| [Linux](https://www.apache.org/dyn/closer.cgi/netbeans/netbeans-installers/12.6/Apache-NetBeans-12.6-bin-linux-x64.sh) \| [Mac](https://www.apache.org/dyn/closer.cgi/netbeans/netbeans-installers/12.6/Apache-NetBeans-12.6-bin-macosx.dmg) |
| Apache Maven | 3.8.4 | [https://maven.apache.org/](https://maven.apache.org/) |
| antlr4 | Usado para criação de dicionários | [https://www.antlr.org/](https://www.antlr.org/) |

### Para compilar o projeto:
Execute os comandos abaixo no terminal de comandos:

```sh
git clone https://github.com/MatheusRMVideira/compiladores-trabalho-2.git
cd compiladores-trabalho-2
mvn install
mvn compile assembly:single
```

Para executar o código


java -jar ./target/compiladorT5-1.0-SNAPSHOT-jar-with-dependencies.jar {ARQUIVO DE ENTRADA} {ARQUIVO DE SAÍDA}

SE ATENTE A USAR OS DIRETÓRIOS DE SUA PRÓPRIA MÁQUINA, E OS NOMES DOS ARQUIVOS DE ENTRADA E SAÍDA DESEJADOS.

VERIFIQUE O <maven.compiler.source> E </maven.compiler.target> NO ARQUIVO POM DE SEU PROGRAMA, O ARQUIVO BASE CONSTA COMO 1.8.

Para compilar o código em um arquivo à parte, abra o projeto na IDE NetBeans, utilize a função de "Clean and Build" localizada no canto superior esquerdo. Se o arquivo fonte for modificado, se atente a erros e warnings, pois eles podem comprometer o funcionamento da aplicação.

Bom Proveito!
