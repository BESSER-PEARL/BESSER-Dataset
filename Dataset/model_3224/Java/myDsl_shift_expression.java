





import java.util.List;
import java.util.ArrayList;

public class myDsl_shift_expression  {






    private myDsl_relational_expression_complement mydsl_relational_expression_complement;




    private myDsl_relational_expression mydsl_relational_expression;




    private myDsl_additive_expression mydsl_additive_expression;


    public myDsl_shift_expression(
    ) {
    }



    public myDsl_relational_expression_complement getMydsl_relational_expression_complement() {
        return mydsl_relational_expression_complement;
    }

    public void setMydsl_relational_expression_complement(myDsl_relational_expression_complement mydsl_relational_expression_complement) {
        this.mydsl_relational_expression_complement = mydsl_relational_expression_complement;
    }
    public myDsl_relational_expression getMydsl_relational_expression() {
        return mydsl_relational_expression;
    }

    public void setMydsl_relational_expression(myDsl_relational_expression mydsl_relational_expression) {
        this.mydsl_relational_expression = mydsl_relational_expression;
    }
    public myDsl_additive_expression getMydsl_additive_expression() {
        return mydsl_additive_expression;
    }

    public void setMydsl_additive_expression(myDsl_additive_expression mydsl_additive_expression) {
        this.mydsl_additive_expression = mydsl_additive_expression;
    }

}