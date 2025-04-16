# Pizzaria

## Tecnologias Utilizadas

- *Backend*: Python com Flask
- *Frontend*: HTML e CSS 
- *Banco de Dados*: SQLite3 com Python

---

## ✅ Casos de Uso

1. **Criar Conta**  
   - Formulário: E-mail, Senha.  
   - Cadastro na tabela de usuários.

2. **Fazer Login**  
   - Verificação de e-mail e senha.
   - Se válido, manter login com sessão (`session` do Flask).

3. **Criar Pedidos de pizza**  
   

3. **Criar tipos de Pizza, Atualizar, Deletar e Listar os tipos de Pizzas**

5. **Ver Pedidos de Pizza**  
   - Exibir em formato de tabela 

6. **Cancelar o pedido de Pizza**  
   - Botão de remover Pizza

7. **Alterar o pedido de Pizza**  
   - Alterar detalhes do pedido

---

## 🗃 Diagrama Banco de Dados

**Tabelas:**  

- `usuarios`
  - email (primary key)
  - senha
    
 -  `pedidos`
     - id (primary key)
     - nome_pizza 
     - tamanho_pizza 
     - preco_pizza 
     - preco_refri
     - preco_entrega
     - preco_borda
     - endereco
     - telefone
     - nome_cliente

  - `pizzas`
    - id (primary key)
    - nome
    - ingredientes


