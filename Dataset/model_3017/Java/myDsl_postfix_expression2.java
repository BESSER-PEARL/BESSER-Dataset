





import java.util.List;
import java.util.ArrayList;

public class myDsl_postfix_expression2  {






    private myDsl_assignment_expression mydsl_assignment_expression;




    private myDsl_postfix_expression mydsl_postfix_expression;


    public myDsl_postfix_expression2(
    ) {
    }



    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }
    public myDsl_postfix_expression getMydsl_postfix_expression() {
        return mydsl_postfix_expression;
    }

    public void setMydsl_postfix_expression(myDsl_postfix_expression mydsl_postfix_expression) {
        this.mydsl_postfix_expression = mydsl_postfix_expression;
    }

}