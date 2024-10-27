# Design de Código para Calculadoras

Este projeto implementa diversas calculadoras que realizam operações matemáticas variadas, aplicando boas práticas de design e arquitetura de software para garantir um código bem estruturado, fácil de manter e testável.

## 📋 Descrição do Projeto

Este repositório explora a aplicação de princípios de design de código e arquitetura, focando nas seguintes práticas:

- **Estruturação dos arquivos** para facilitar a navegação e o entendimento do projeto
- **Uso de typing** para melhorar a legibilidade e reduzir erros
- **Interfaces e dependências** bem definidas, garantindo flexibilidade e coesão
- **Injeção de dependência** para desacoplar e tornar o código mais modular
- **Design Pattern Factory** para instanciar objetos de forma dinâmica, conforme a necessidade de cada cálculo
- **Testes unitários e de integração** para garantir a confiabilidade e robustez das funcionalidades

## 🧪 Testes

O projeto inclui:

- **Testes Unitários**: Garantem que componentes individuais funcionem corretamente em isolamento.
- **Testes de Integração**: Verificam a integração dos componentes, garantindo que eles colaborem corretamente.

Para rodar os testes, utilize:

```bash
pytest -s -v 
```

Além disso, este projeto adota e demonstra os princípios SOLID para promover um código escalável e de fácil manutenção.

## 🧩 SOLID

Aplicação dos princípios SOLID:

1. **Single Responsibility Principle (SRP)**: Cada classe tem uma única responsabilidade, evitando funcionalidades excessivas e promovendo coesão.
2. **Open/Closed Principle (OCP)**: As classes estão abertas para extensão, mas fechadas para modificação, permitindo adicionar novas funcionalidades sem alterar o código existente.
3. **Liskov Substitution Principle (LSP)**: As subclasses substituem suas superclasses sem alterar a corretude do programa.
4. **Interface Segregation Principle (ISP)**: Interfaces específicas e focadas são usadas para evitar dependências desnecessárias.
5. **Dependency Inversion Principle (DIP)**: Abstrações são usadas para desacoplar o código, facilitando a substituição de dependências.


