





import java.util.List;
import java.util.ArrayList;

public class myDsl_expression extends jump_statement, expression_statement, primary_expression {






    private myDsl_iteration_statement mydsl_iteration_statement;




    private myDsl_conditional_expression mydsl_conditional_expression;




    private myDsl_assignment_expression mydsl_assignment_expression;




    private myDsl_postfix_expressionR mydsl_postfix_expressionr;


    public myDsl_expression(
    ) {
        super(
        );
    }



    public myDsl_iteration_statement getMydsl_iteration_statement() {
        return mydsl_iteration_statement;
    }

    public void setMydsl_iteration_statement(myDsl_iteration_statement mydsl_iteration_statement) {
        this.mydsl_iteration_statement = mydsl_iteration_statement;
    }
    public myDsl_conditional_expression getMydsl_conditional_expression() {
        return mydsl_conditional_expression;
    }

    public void setMydsl_conditional_expression(myDsl_conditional_expression mydsl_conditional_expression) {
        this.mydsl_conditional_expression = mydsl_conditional_expression;
    }
    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }
    public myDsl_postfix_expressionR getMydsl_postfix_expressionr() {
        return mydsl_postfix_expressionr;
    }

    public void setMydsl_postfix_expressionr(myDsl_postfix_expressionR mydsl_postfix_expressionr) {
        this.mydsl_postfix_expressionr = mydsl_postfix_expressionr;
    }

}