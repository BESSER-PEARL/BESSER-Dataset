





import java.util.List;
import java.util.ArrayList;

public class Cliente  {

    private String Telefone;
    private String Cpf;
    private int ClienteId;
    private String Nome;
    private String Email;



    public Cliente(
        String Telefone,        String Cpf,        int ClienteId,        String Nome,        String Email    ) {
        this.Telefone = Telefone;
        this.Cpf = Cpf;
        this.ClienteId = ClienteId;
        this.Nome = Nome;
        this.Email = Email;
    }


    public String getTelefone() {
        return Telefone;
    }

    public void setTelefone(String Telefone) {
        this.Telefone = Telefone;
    }
    public String getCpf() {
        return Cpf;
    }

    public void setCpf(String Cpf) {
        this.Cpf = Cpf;
    }
    public int getClienteid() {
        return ClienteId;
    }

    public void setClienteid(int ClienteId) {
        this.ClienteId = ClienteId;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}