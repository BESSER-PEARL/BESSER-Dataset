





import java.util.List;
import java.util.ArrayList;

public class myDsl_labeled_statement extends statement {






    private myDsl_constant_expression mydsl_constant_expression;


    public myDsl_labeled_statement(
    ) {
        super(
        );
    }



    public myDsl_constant_expression getMydsl_constant_expression() {
        return mydsl_constant_expression;
    }

    public void setMydsl_constant_expression(myDsl_constant_expression mydsl_constant_expression) {
        this.mydsl_constant_expression = mydsl_constant_expression;
    }

}