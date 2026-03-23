while True:  
    print("avaliação da disciplina do aluno")
    print("------------S2------------------")

    #entrada  (usuario)
    materia= input("nome da materia: ")
    aluno = input("nome do aluno: ")
    b1 = float(input("digite a nota do b1: "))
    b2 = float(input("digite a nota do b2: "))
    b3 = float(input("digite a nota do b3: "))
    b4 = float(input("digite a nota do b4: "))


    #processamento (pc + Humano = informação) 
    media = (b1+b2+b3+b4) / 4
    frequencia = float(input("Digite a porcentagem (%): "))

    print(f"materia: {materia}")
    print(f"media: {media:}")
    print(f"frequencia: {frequencia}")

    if(media >=5 and frequencia>= 75):
        print ("Aluno  aprovado")
    else:
        print("Aluno  recuperação")

    #perguntar se quer saber de outro aluno?
    continuar= input('adicionar outro aluno s/n?').strip()
    if continuar == "s":
        print("Pesquisar outro aluno!")
    else:    
        print("Não pesquisar outro aluno!")
        break

        
        
       
       
      
     