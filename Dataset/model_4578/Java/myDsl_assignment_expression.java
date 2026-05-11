





import java.util.List;
import java.util.ArrayList;

public class myDsl_assignment_expression extends initializer {

    private String Assignment_operator;





    private myDsl_assignment_expression mydsl_assignment_expression;


    public myDsl_assignment_expression(
        String Assignment_operator    ) {
        super(
        );
        this.Assignment_operator = Assignment_operator;
    }


    public String getAssignment_operator() {
        return Assignment_operator;
    }

    public void setAssignment_operator(String Assignment_operator) {
        this.Assignment_operator = Assignment_operator;
    }

    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }

}