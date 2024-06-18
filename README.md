<div align=center>

<h1>Automacao-Scripts-Python</h1>
Desenvolver método de automação paralela por meio do código em Python.
</div>

<h2>📝Instructions</h2>

<!-- FIRST STEP IS HERE -->

<details>
<summary><strong>🔸First Step</strong></summary>

<p></p>
<p>Para começar, certifique-se de ter a biblioteca `schedule` instalada. Caso não tenha, você pode instalá-la usando o pip:</p>

```sh
pip install schedule
```

<p>Depois de instalar a biblioteca `schedule`, importe-a no seu script Python:</p>

```python
import schedule
import time
```

<p>Agora você pode começar a configurar a automação no seu script.</p>
</details>

<!-- SECOND STEP IS HERE -->

<details>
<summary><strong>🔹Second Step</strong></summary>

<p></p>
<p>Agora vamos criar uma função aleatória para demonstrar o uso do `schedule`.</p>

<p>Primeiro, defina uma função, por exemplo `run_task()`:</p>

```python
def run_task():
    print("Executando uma tarefa aleatória...")
```

<p>É importante estruturar seu script Python com uma função principal (`main`) para organizar e controlar a execução das tarefas. Aqui está como você pode criar a função `main`:</p>

```python
def main():
    # Configuração do agendamento com o schedule
    schedule.every().day.at("10:00").do(run_task)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
```

<p>Este exemplo define a função `run_task()` para ser executada todos os dias às 10:00 AM usando o `schedule`. Certifique-se de adaptar o nome da função e o horário conforme necessário para suas próprias tarefas.</p>
</details>

<!-- THIRD STEP IS HERE -->

<details>
<summary><strong>🔻Third Step</strong></summary>

<p></p>
<p>Agora vamos expandir a automação para incluir mais funções agendadas com o `schedule`.</p>

<p>Suponha que você tenha uma função `backup_data()` que precisa ser executada diariamente às 14:00. Você pode configurar o `schedule` da seguinte forma:</p>

```python
def backup_data():
    print("Executando backup de dados...")

def main():
    schedule.every().day.at("10:00").do(run_task)
    schedule.every().day.at("14:00").do(backup_data)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
```

<p>Agora, `backup_data()` será executada todos os dias às 14:00, juntamente com `run_task()` que é executada às 10:00 AM.</p>
</details>

<!--  -->

### Explicação das Etapas

- **Passo 1 (First Step)**:
  - Ensina como instalar a biblioteca `schedule` usando `pip install schedule`.
  - Explica como importar a biblioteca `schedule` no script Python para começar a usar suas funcionalidades de automação.

- **Passo 2 (Second Step)**:
  - Define uma função aleatória `run_task()` para demonstrar o uso do `schedule`.
  - Enfatiza a importância de estruturar o script com uma função principal (`main`) para gerenciar o agendamento das tarefas.

- **Passo 3 (Third Step)**:
  - Expande a automação adicionando outra função, `backup_data()`, que é agendada para ser executada todos os dias às 14:00 junto com `run_task()` às 10:00 AM.
  
Essas etapas guiadas ajudam a configurar e expandir a automação com `schedule` em seu script Python de maneira organizada e compreensível.
