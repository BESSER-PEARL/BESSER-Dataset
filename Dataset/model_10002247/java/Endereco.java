





import java.util.List;
import java.util.ArrayList;

public class Endereco  {

    private String cidade;
    private String cep;
    private String bairro;
    private int numero;
    private String logradouro;





    private LocalExame localexame;


    public Endereco(
        String cidade,        String cep,        String bairro,        int numero,        String logradouro    ) {
        this.cidade = cidade;
        this.cep = cep;
        this.bairro = bairro;
        this.numero = numero;
        this.logradouro = logradouro;
    }


    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }
    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }
    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }
    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }
    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public LocalExame getLocalexame() {
        return localexame;
    }

    public void setLocalexame(LocalExame localexame) {
        this.localexame = localexame;
    }

}