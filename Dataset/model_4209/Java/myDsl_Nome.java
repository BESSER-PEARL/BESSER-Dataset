





import java.util.List;
import java.util.ArrayList;

public class myDsl_Nome  {

    private String nome;





    private myDsl_Entidade mydsl_entidade;


    public myDsl_Nome(
        String nome    ) {
        this.nome = nome;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public myDsl_Entidade getMydsl_entidade() {
        return mydsl_entidade;
    }

    public void setMydsl_entidade(myDsl_Entidade mydsl_entidade) {
        this.mydsl_entidade = mydsl_entidade;
    }

}