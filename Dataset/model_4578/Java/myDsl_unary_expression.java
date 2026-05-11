





import java.util.List;
import java.util.ArrayList;

public class myDsl_unary_expression extends cast_expression {

    private String Unary_operator;





    private myDsl_assignment_expression mydsl_assignment_expression;


    public myDsl_unary_expression(
        String Unary_operator    ) {
        super(
        );
        this.Unary_operator = Unary_operator;
    }


    public String getUnary_operator() {
        return Unary_operator;
    }

    public void setUnary_operator(String Unary_operator) {
        this.Unary_operator = Unary_operator;
    }

    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }

}