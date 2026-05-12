





import java.util.List;
import java.util.ArrayList;

public class Paciente  {

    private String endere_o;
    private String celular;
    private String nome;



    public Paciente(
        String endere_o,        String celular,        String nome    ) {
        this.endere_o = endere_o;
        this.celular = celular;
        this.nome = nome;
    }


    public String getEndere_o() {
        return endere_o;
    }

    public void setEndere_o(String endere_o) {
        this.endere_o = endere_o;
    }
    public String getCelular() {
        return celular;
    }

    public void setCelular(String celular) {
        this.celular = celular;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }


}