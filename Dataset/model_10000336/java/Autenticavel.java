





import java.util.List;
import java.util.ArrayList;

public class Autenticavel  {

    private String Autenticar;
    private String Senha;





    private ContaBancaria contabancaria;


    public Autenticavel(
        String Autenticar,        String Senha    ) {
        this.Autenticar = Autenticar;
        this.Senha = Senha;
    }


    public String getAutenticar() {
        return Autenticar;
    }

    public void setAutenticar(String Autenticar) {
        this.Autenticar = Autenticar;
    }
    public String getSenha() {
        return Senha;
    }

    public void setSenha(String Senha) {
        this.Senha = Senha;
    }

    public ContaBancaria getContabancaria() {
        return contabancaria;
    }

    public void setContabancaria(ContaBancaria contabancaria) {
        this.contabancaria = contabancaria;
    }

}