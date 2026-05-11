





import java.util.List;
import java.util.ArrayList;

public class myDsl_logical_or_expression  {






    private myDsl_conditional_expression mydsl_conditional_expression;




    private myDsl_logical_and_expression mydsl_logical_and_expression;


    public myDsl_logical_or_expression(
    ) {
    }



    public myDsl_conditional_expression getMydsl_conditional_expression() {
        return mydsl_conditional_expression;
    }

    public void setMydsl_conditional_expression(myDsl_conditional_expression mydsl_conditional_expression) {
        this.mydsl_conditional_expression = mydsl_conditional_expression;
    }
    public myDsl_logical_and_expression getMydsl_logical_and_expression() {
        return mydsl_logical_and_expression;
    }

    public void setMydsl_logical_and_expression(myDsl_logical_and_expression mydsl_logical_and_expression) {
        this.mydsl_logical_and_expression = mydsl_logical_and_expression;
    }

}