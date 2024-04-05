import scipy.io


dados = scipy.io.loadmat("C:/Users/Renan/Documents/Mestrado/PO-233/GradPRN22.mat")

dados.keys()

#(dados.keys())

Grad_tempo  = dados["Grad_tempo"];
Grad_data  = dados["Grad_data"];

print(Grad_tempo[0,0]);