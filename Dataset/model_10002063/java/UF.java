





import java.util.List;
import java.util.ArrayList;

public class UF  {

    private String nome;
    private String sigla;





    private Cidade cidade;


    public UF(
        String nome,        String sigla    ) {
        this.nome = nome;
        this.sigla = sigla;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getSigla() {
        return sigla;
    }

    public void setSigla(String sigla) {
        this.sigla = sigla;
    }

    public Cidade getCidade() {
        return cidade;
    }

    public void setCidade(Cidade cidade) {
        this.cidade = cidade;
    }

}