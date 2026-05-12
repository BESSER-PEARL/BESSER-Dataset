





import java.util.List;
import java.util.ArrayList;

public class Conta_Poupan_a  {

    private float Senha;
    private String Nome;
    private int CPF;



    public Conta_Poupan_a(
        float Senha,        String Nome,        int CPF    ) {
        this.Senha = Senha;
        this.Nome = Nome;
        this.CPF = CPF;
    }


    public float getSenha() {
        return Senha;
    }

    public void setSenha(float Senha) {
        this.Senha = Senha;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public int getCpf() {
        return CPF;
    }

    public void setCpf(int CPF) {
        this.CPF = CPF;
    }


}