# E-Commerce System - POO Project (Versão Atualizada)

## Descrição
Sistema completo de e-commerce desenvolvido em Python utilizando Programação Orientada a Objetos (POO) e padrões de projeto. O sistema agora inclui:

- Cadastro e autenticação de usuários
- Gerenciamento completo de produtos (estoque, notificações)
- Processo de compra com múltiplos métodos de pagamento
- Sistema de pedidos e rastreamento

## Arquitetura MVC Atualizada

### Models (Camada de Dados)
- `user.py`: 
  - Classes `Usuario` (abstrata), `Administrador`, `Cliente`
  - `UsuarioFactory` (Factory Method para criação de usuários)
- `product.py`:
  - Classe `Product` (com padrão Observer integrado)
  - Controle de estoque e notificações
- `order.py`:
  - Classes `Order` e `OrderManager`
  - Rastreamento de status de pedidos
- `observer.py`:
  - Implementação completa do padrão Observer
  - Classes `Subject`, `Observer`, `EmailNotifier`

### Views (Interface)
- `auth_view.py`: Fluxo de autenticação e cadastro
- `admin_view.py`: Interface para gerenciamento de produtos
- `client_view.py`: 
  - Catálogo de produtos
  - Carrinho de compras
  - Acompanhamento de pedidos

### Controllers (Lógica)
- `auth_controller.py`: 
  - Gerencia login/cadastro
  - Utiliza `UsuarioFactory`
- `admin_controller.py`:
  - CRUD de produtos
  - Integra com sistema de notificações
- `client_controller.py`:
  - Processo de compra completo
  - Integração com `CheckoutFacade`

### Services (Lógica Complexa)
- `checkout_facade.py`:
  - Orquestra todo o fluxo de checkout
  - Integra validação, pagamento e estoque
- `payment_strategy.py`:
  - Implementa Strategy para pagamentos
  - Classes `PaymentStrategy`, `CreditCardPayment`, `PixPayment`

## Padrões de Projeto Implementados (Detalhados)

### 1. Factory Method (`UsuarioFactory`)
**Localização**: `models/user.py`  
**Funcionamento**:
```python
user = UsuarioFactory.criar_usuario("admin", "admin1", "senha123")
```
**Benefícios**:
- Centraliza a criação de objetos usuário
- Facilita adicionar novos tipos de usuários
- Elimina condicionais complexas no código

### 2. Observer (Sistema de Notificações)
**Localização**: `models/observer.py` e `models/product.py`  
**Fluxo**:
1. Produto é criado/adicionado
2. Notifica todos os observers registrados:
```python
produto.notificar("Novo iPhone em estoque!")
```
**Implementação**:
- `EmailNotifier`: Envia e-mails para clientes
- Pode ser estendido para SMS ou push notifications

### 3. Facade (Processo de Checkout)
**Localização**: `services/checkout_facade.py`  
**Métodos Principais**:
- `_validar_estoque()`: Checa disponibilidade
- `_processar_pagamento()`: Usa Strategy pattern
- `_gerar_pedido()`: Cria registro de pedido

**Exemplo de Uso**:
```python
facade = CheckoutFacade(carrinho, usuario)
facade.finalizar_compra("pix")
```

### 4. Strategy (Métodos de Pagamento)
**Localização**: `services/payment_strategy.py`  
**Estrutura**:
```python
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        # Lógica específica para cartão
        return True
```
**Como Trocar Métodos**:
```python
contexto = PaymentContext(PixPayment())
contexto.executar_pagamento(100.00)
```

## Fluxo Completo do Sistema

1. **Inicialização**:
   - Carrega produtos pré-cadastrados
   - Inicializa serviços

2. **Autenticação**:
   - Usuário faz login ou cadastro
   - `UsuarioFactory` cria instância adequada

3. **Admin Logado**:
   - Adiciona/edita produtos
   - Cada novo produto notifica observers

4. **Cliente Logado**:
   - Navega por produtos
   - Adiciona ao carrinho
   - Finaliza compra via Facade:
     - Valida estoque
     - Processa pagamento (Strategy)
     - Gera pedido
     - Atualiza estoque

5. **Pós-Compra**:
   - Notificações por e-mail (Observer)
   - Acompanhamento de pedido

## Como Executar

1. Clone o repositório
2. Execute:
```bash
python main.py
```

3. Use as credenciais:
   - Admin: usuario="admin", senha="admin123"
   - Ou crie novo usuário

## Dependências
- Python 3.8+
- Nenhuma biblioteca externa necessária

## Diagrama de Componentes

```
[Main]
  |
  |--> [AuthController] ↔ [AuthView]
  |     |
  |     |--> UsuarioFactory
  |
  |--> [AdminController] ↔ [AdminView]
  |     |
  |     |--> Product (Observer)
  |
  |--> [ClientController] ↔ [ClientView]
        |
        |--> CheckoutFacade
              |
              |--> PaymentStrategy
              |--> OrderManager
```

## Melhorias Futuras
1. Persistência em banco de dados
2. Sistema de avaliação de produtos
3. Cupons de desconto
4. Dashboard administrativo

---
# **Explicação Profunda do Projeto E-Commerce com Padrões de Projeto**

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

