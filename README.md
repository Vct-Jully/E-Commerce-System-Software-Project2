# E-Commerce System - POO Project

## Descrição
Sistema de e-commerce desenvolvido em Python utilizando Programação Orientada a Objetos (POO) e padrões de projeto. O sistema permite:
- Administradores gerenciarem produtos
- Clientes visualizarem produtos, adicionarem ao carrinho e finalizarem compras
- Autenticação de usuários com diferentes níveis de acesso

## Arquitetura
Padrão MVC (Model-View-Controller) com os seguintes componentes:

### Models
- `user.py`: Classes de usuários (Administrador, Cliente)
- `product.py`: Gerenciamento de produtos
- `order.py`: Processamento de pedidos
- `observer.py`: Implementação do padrão Observer

### Views
- `auth_view.py`: Telas de autenticação
- `admin_view.py`: Interface do administrador
- `client_view.py`: Interface do cliente

### Controllers
- `auth_controller.py`: Gerencia autenticação
- `admin_controller.py`: Controla ações de admin
- `client_controller.py`: Controla ações do cliente

### Services
- `checkout_facade.py`: Facade para processo de checkout
- `payment_strategy.py`: Estratégias de pagamento

## Padrões de Projeto Implementados

### Factory Method
**Classe**: `UsuarioFactory` (em `models/user.py`)  
**Propósito**: Criar instâncias de diferentes tipos de usuários  
**Métodos**:
- `criar_usuario(tipo, usuario, senha)`: Retorna instância de Administrador ou Cliente

### Observer
**Classes** (em `models/observer.py`):
- `Subject`: Mantém lista de observers e notifica mudanças
- `Observer`: Interface abstrata para observers
- `EmailNotifier`: Implementação concreta para notificações por e-mail

**Uso**: Notifica clientes sobre novos produtos (integrado em `Product`)

### Facade
**Classe**: `CheckoutFacade` (em `services/checkout_facade.py`)  
**Propósito**: Simplificar interface para processo de checkout  
**Métodos principais**:
- `finalizar_compra()`: Orquestra validação, pagamento e criação de pedido
- Métodos privados para cada etapa do processo (`_validar_estoque`, `_processar_pagamento`)

### Strategy
**Classes** (em `services/payment_strategy.py`):
- `PaymentStrategy`: Interface para estratégias de pagamento
- `CreditCardPayment`: Implementação para pagamento com cartão
- `PixPayment`: Implementação para pagamento via Pix
- `PaymentContext`: Contexto que executa a estratégia selecionada

## Fluxo Principal

1. **Autenticação**:
   - Usuários fazem login ou se cadastram via `AuthController`
   - Factory Method cria instâncias adequadas de usuário

2. **Administração**:
   - Admins gerenciam produtos através do `AdminController`
   - Novos produtos notificam observers registrados

3. **Compra**:
   - Clientes adicionam itens ao carrinho
   - CheckoutFacade orquestra o processo de compra
   - PaymentStrategy processa o pagamento conforme método selecionado

## Como Executar
1. Instale Python 3+
2. Execute o arquivo principal:
   ```bash
   python main.py
   
---
# **Explicação Profunda do Projeto E-Commerce com Padrões de Projeto**

A seguir, uma explicação detalhada sobre **como os padrões de projeto foram aplicados**, **para que servem** e **como funcionam** no sistema.

---

## **1. Padrões Criacionais: Factory Method**
### **O que é?**
O **Factory Method** é um padrão que **centraliza a criação de objetos**, evitando acoplamento direto no código. Em vez de instanciar classes manualmente (`Administrador()` ou `Cliente()`), usamos uma **fábrica** (`UsuarioFactory`) para criar esses objetos de forma dinâmica.

### **Como foi aplicado?**
No arquivo `models/user.py`, adicionamos:
```python
class UsuarioFactory:
    @staticmethod
    def criar_usuario(tipo, usuario, senha, nome=None, email=None):
        if tipo == "admin":
            return Administrador(usuario, senha, nome, email)
        elif tipo == "cliente":
            return Cliente(usuario, senha, nome, email)
        else:
            raise ValueError("Tipo de usuário inválido.")
```
### **Para que serve?**
- **Evita repetição de código**: Sem a fábrica, teríamos que verificar o tipo de usuário em vários lugares (ex.: `if tipo == "admin": return Administrador(...)`).
- **Facilita manutenção**: Se surgir um novo tipo de usuário (ex.: `Vendedor`), basta modificar a fábrica, sem alterar o resto do sistema.
- **Uso no `AuthController`**:
  ```python
  # No cadastro de usuários:
  novo_usuario = UsuarioFactory.criar_usuario("cliente", "joao", "senha123")
  ```

---

## **2. Padrão Comportamental: Observer**
### **O que é?**
O **Observer** permite que **objetos sejam notificados quando um evento ocorre**. No e-commerce, usamos para **avisar clientes sobre novos produtos**.

### **Como foi aplicado?**
No arquivo `models/observer.py`:
```python
class Subject:
    def __init__(self):
        self._observers = []  # Lista de observadores

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def notificar(self, mensagem):
        for observer in self._observers:
            observer.update(mensagem)  # Notifica todos

class EmailNotifier(Observer):
    def update(self, mensagem):
        print(f"Email enviado: {mensagem}")  # Simulação de e-mail
```
### **Para que serve?**
- **Notificação automática**: Quando um novo produto é cadastrado (`Product.add_product()`), todos os clientes registrados como **observers** são notificados.
- **Baixo acoplamento**: O `Product` não precisa saber quem são os observers, apenas envia a mensagem.

### **Uso no `Product`**:
```python
class Product(Subject):  # Herda de Subject
    def add_product(nome, preco):
        produto = Product(nome, preco)
        produto.notificar(f"Novo produto: {nome} por R${preco}!")
```

---

## **3. Padrão Estrutural: Facade**
### **O que é?**
O **Facade** simplifica **operações complexas** (como o checkout) em uma **interface única**. Ele esconde detalhes internos (validação, pagamento, etc.) e fornece um método simples (`finalizar_compra()`).

### **Como foi aplicado?**
No arquivo `services/checkout_facade.py`:
```python
class CheckoutFacade:
    def __init__(self, carrinho, usuario):
        self.carrinho = carrinho
        self.usuario = usuario

    def finalizar_compra(self):
        if self._validar_estoque() and self._processar_pagamento():
            self._gerar_pedido()
            return True
        return False

    def _validar_estoque(self): ...
    def _processar_pagamento(self): ...
    def _gerar_pedido(self): ...
```
### **Para que serve?**
- **Organiza o fluxo de checkout**: Em vez de espalhar a lógica em vários lugares, tudo é centralizado no `Facade`.
- **Facilita testes**: Podemos testar o checkout isoladamente.
- **Uso no `ClientController`**:
  ```python
  facade = CheckoutFacade(cliente.carrinho, cliente)
  facade.finalizar_compra()
  ```

---

## **4. Padrão Comportamental: Strategy**
### **O que é?**
O **Strategy** permite **definir algoritmos intercambiáveis** (ex.: métodos de pagamento: cartão, Pix, boleto). Cada estratégia é uma classe separada, e o sistema escolhe a adequada em tempo de execução.

### **Como foi aplicado?**
No arquivo `services/payment_strategy.py`:
```python
class CreditCardPayment:
    def pay(self, valor):
        print(f"Pagando R${valor} via cartão")
        return True

class PixPayment:
    def pay(self, valor):
        print(f"Pagando R${valor} via Pix")
        return True

class PaymentContext:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def executar_pagamento(self, valor):
        return self.estrategia.pay(valor)
```
### **Para que serve?**
- **Flexibilidade**: Podemos adicionar novos métodos de pagamento sem modificar o código existente.
- **Uso no `CheckoutFacade`**:
  ```python
  if metodo == "cartao":
      estrategia = CreditCardPayment()
  contexto = PaymentContext(estrategia)
  contexto.executar_pagamento(100.0)
  ```

---

## **Conclusão**
Este projeto demonstra como **padrões de projeto** resolvem problemas comuns em sistemas reais:
1. **Factory Method**: Centraliza a criação de usuários.
2. **Observer**: Notifica clientes sobre mudanças.
3. **Facade**: Simplifica o processo de checkout.
4. **Strategy**: Gerencia diferentes formas de pagamento.

Cada padrão foi aplicado **sem alterar o fluxo principal**, mantendo o código **organizado, testável e escalável**. Se surgirem dúvidas durante a apresentação, posso esclarecer!
