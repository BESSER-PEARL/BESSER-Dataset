





import java.util.List;
import java.util.ArrayList;

public class myDsl_expression extends postfix_expression2 {






    private myDsl_conditional_expression mydsl_conditional_expression;


    public myDsl_expression(
    ) {
        super(
        );
    }



    public myDsl_conditional_expression getMydsl_conditional_expression() {
        return mydsl_conditional_expression;
    }

    public void setMydsl_conditional_expression(myDsl_conditional_expression mydsl_conditional_expression) {
        this.mydsl_conditional_expression = mydsl_conditional_expression;
    }

}