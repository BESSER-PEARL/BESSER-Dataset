





import java.util.List;
import java.util.ArrayList;

public class myDsl_selection_statement extends statement {






    private myDsl_expression mydsl_expression;


    public myDsl_selection_statement(
    ) {
        super(
        );
    }



    public myDsl_expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }

}