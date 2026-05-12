





import java.util.List;
import java.util.ArrayList;

public class Exame  {

    private String data;
    private String descricao;
    private String nome;





    private LocalExame localexame;


    public Exame(
        String data,        String descricao,        String nome    ) {
        this.data = data;
        this.descricao = descricao;
        this.nome = nome;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public LocalExame getLocalexame() {
        return localexame;
    }

    public void setLocalexame(LocalExame localexame) {
        this.localexame = localexame;
    }

}