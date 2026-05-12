





import java.util.List;
import java.util.ArrayList;

public class Conta_Corrente  {

    private int CPF;
    private String Nome;
    private float Senha;
    private float Taxa_de_Movimenta__o;



    public Conta_Corrente(
        int CPF,        String Nome,        float Senha,        float Taxa_de_Movimenta__o    ) {
        this.CPF = CPF;
        this.Nome = Nome;
        this.Senha = Senha;
        this.Taxa_de_Movimenta__o = Taxa_de_Movimenta__o;
    }


    public int getCpf() {
        return CPF;
    }

    public void setCpf(int CPF) {
        this.CPF = CPF;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public float getSenha() {
        return Senha;
    }

    public void setSenha(float Senha) {
        this.Senha = Senha;
    }
    public float getTaxa_de_movimenta__o() {
        return Taxa_de_Movimenta__o;
    }

    public void setTaxa_de_movimenta__o(float Taxa_de_Movimenta__o) {
        this.Taxa_de_Movimenta__o = Taxa_de_Movimenta__o;
    }


}