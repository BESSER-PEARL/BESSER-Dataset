





import java.util.List;
import java.util.ArrayList;

public class myDsl_PostfixExpressionLinhaAction extends postfix_expression_linha {






    private myDsl_postfix_expression_complement mydsl_postfix_expression_complement;




    private myDsl_postfix_expression_linha mydsl_postfix_expression_linha;


    public myDsl_PostfixExpressionLinhaAction(
    ) {
        super(
        );
    }



    public myDsl_postfix_expression_complement getMydsl_postfix_expression_complement() {
        return mydsl_postfix_expression_complement;
    }

    public void setMydsl_postfix_expression_complement(myDsl_postfix_expression_complement mydsl_postfix_expression_complement) {
        this.mydsl_postfix_expression_complement = mydsl_postfix_expression_complement;
    }
    public myDsl_postfix_expression_linha getMydsl_postfix_expression_linha() {
        return mydsl_postfix_expression_linha;
    }

    public void setMydsl_postfix_expression_linha(myDsl_postfix_expression_linha mydsl_postfix_expression_linha) {
        this.mydsl_postfix_expression_linha = mydsl_postfix_expression_linha;
    }

}