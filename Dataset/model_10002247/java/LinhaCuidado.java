





import java.util.List;
import java.util.ArrayList;

public class LinhaCuidado  {

    private String nome;
    private int descricao;





    private List<Mensagem> mensagems;


    public LinhaCuidado(
        String nome,        int descricao    ) {
        this.nome = nome;
        this.descricao = descricao;
        this.mensagems = new ArrayList<>();
    }

    public LinhaCuidado(
        String nome,        int descricao        ArrayList<Mensagem> mensagems    ) {
        this.nome = nome;
        this.descricao = descricao;
        this.mensagems = mensagems;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getDescricao() {
        return descricao;
    }

    public void setDescricao(int descricao) {
        this.descricao = descricao;
    }

    public List<Mensagem> getMensagems() {
        return mensagems;
    }

    public void addMensagem(Mensagem mensagem) {
        this.mensagems.add(mensagem);
    }

}