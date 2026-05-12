





import java.util.List;
import java.util.ArrayList;

public class Medico  {

    private String nome;
    private String endereco;
    private String crm;
    private String foto;



    public Medico(
        String nome,        String endereco,        String crm,        String foto    ) {
        this.nome = nome;
        this.endereco = endereco;
        this.crm = crm;
        this.foto = foto;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
    public String getCrm() {
        return crm;
    }

    public void setCrm(String crm) {
        this.crm = crm;
    }
    public String getFoto() {
        return foto;
    }

    public void setFoto(String foto) {
        this.foto = foto;
    }


}