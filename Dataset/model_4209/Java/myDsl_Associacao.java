





import java.util.List;
import java.util.ArrayList;

public class myDsl_Associacao  {

    private String associacao;





    private myDsl_Atributo mydsl_atributo;


    public myDsl_Associacao(
        String associacao    ) {
        this.associacao = associacao;
    }


    public String getAssociacao() {
        return associacao;
    }

    public void setAssociacao(String associacao) {
        this.associacao = associacao;
    }

    public myDsl_Atributo getMydsl_atributo() {
        return mydsl_atributo;
    }

    public void setMydsl_atributo(myDsl_Atributo mydsl_atributo) {
        this.mydsl_atributo = mydsl_atributo;
    }

}