





import java.util.List;
import java.util.ArrayList;

public class myDsl_argument_expression_list extends postfix_expression2 {






    private List<myDsl_assignment_expression> mydsl_assignment_expressions;


    public myDsl_argument_expression_list(
    ) {
        super(
        );
        this.mydsl_assignment_expressions = new ArrayList<>();
    }

    public myDsl_argument_expression_list(
        ArrayList<myDsl_assignment_expression> mydsl_assignment_expressions    ) {
        this.mydsl_assignment_expressions = mydsl_assignment_expressions;
    }


    public List<myDsl_assignment_expression> getMydsl_assignment_expressions() {
        return mydsl_assignment_expressions;
    }

    public void addMydsl_assignment_expression(Mydsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expressions.add(mydsl_assignment_expression);
    }

}