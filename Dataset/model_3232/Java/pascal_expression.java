





import java.util.List;
import java.util.ArrayList;

public class pascal_expression  {

    private String operators;





    private pascal_expression_list pascal_expression_list;




    private pascal_factor pascal_factor;




    private pascal_while_statement pascal_while_statement;




    private List<pascal_simple_expression> pascal_simple_expressions;




    private pascal_assignment_statement pascal_assignment_statement;


    public pascal_expression(
        String operators    ) {
        this.operators = operators;
        this.pascal_simple_expressions = new ArrayList<>();
    }

    public pascal_expression(
        String operators        ArrayList<pascal_simple_expression> pascal_simple_expressions    ) {
        this.operators = operators;
        this.pascal_simple_expressions = pascal_simple_expressions;
    }

    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public pascal_expression_list getPascal_expression_list() {
        return pascal_expression_list;
    }

    public void setPascal_expression_list(pascal_expression_list pascal_expression_list) {
        this.pascal_expression_list = pascal_expression_list;
    }
    public pascal_factor getPascal_factor() {
        return pascal_factor;
    }

    public void setPascal_factor(pascal_factor pascal_factor) {
        this.pascal_factor = pascal_factor;
    }
    public pascal_while_statement getPascal_while_statement() {
        return pascal_while_statement;
    }

    public void setPascal_while_statement(pascal_while_statement pascal_while_statement) {
        this.pascal_while_statement = pascal_while_statement;
    }
    public List<pascal_simple_expression> getPascal_simple_expressions() {
        return pascal_simple_expressions;
    }

    public void addPascal_simple_expression(Pascal_simple_expression pascal_simple_expression) {
        this.pascal_simple_expressions.add(pascal_simple_expression);
    }
    public pascal_assignment_statement getPascal_assignment_statement() {
        return pascal_assignment_statement;
    }

    public void setPascal_assignment_statement(pascal_assignment_statement pascal_assignment_statement) {
        this.pascal_assignment_statement = pascal_assignment_statement;
    }

}