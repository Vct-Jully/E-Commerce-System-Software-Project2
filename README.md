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
