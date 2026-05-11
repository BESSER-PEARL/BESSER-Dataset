





import java.util.List;
import java.util.ArrayList;

public class myDsl_additive_expression_complement  {

    private String menos;
    private String mais;





    private myDsl_multiplicative_expression mydsl_multiplicative_expression;




    private myDsl_additive_expression_linha mydsl_additive_expression_linha;


    public myDsl_additive_expression_complement(
        String menos,        String mais    ) {
        this.menos = menos;
        this.mais = mais;
    }


    public String getMenos() {
        return menos;
    }

    public void setMenos(String menos) {
        this.menos = menos;
    }
    public String getMais() {
        return mais;
    }

    public void setMais(String mais) {
        this.mais = mais;
    }

    public myDsl_multiplicative_expression getMydsl_multiplicative_expression() {
        return mydsl_multiplicative_expression;
    }

    public void setMydsl_multiplicative_expression(myDsl_multiplicative_expression mydsl_multiplicative_expression) {
        this.mydsl_multiplicative_expression = mydsl_multiplicative_expression;
    }
    public myDsl_additive_expression_linha getMydsl_additive_expression_linha() {
        return mydsl_additive_expression_linha;
    }

    public void setMydsl_additive_expression_linha(myDsl_additive_expression_linha mydsl_additive_expression_linha) {
        this.mydsl_additive_expression_linha = mydsl_additive_expression_linha;
    }

}