





import java.util.List;
import java.util.ArrayList;

public class myDsl_ApiNome  {

    private String nome;





    private myDsl_Api mydsl_api;


    public myDsl_ApiNome(
        String nome    ) {
        this.nome = nome;
    }


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public myDsl_Api getMydsl_api() {
        return mydsl_api;
    }

    public void setMydsl_api(myDsl_Api mydsl_api) {
        this.mydsl_api = mydsl_api;
    }

}