





import java.util.List;
import java.util.ArrayList;

public class pascal_expression_list  {






    private pascal_variable pascal_variable;




    private List<pascal_expression> pascal_expressions;


    public pascal_expression_list(
    ) {
        this.pascal_expressions = new ArrayList<>();
    }

    public pascal_expression_list(
        ArrayList<pascal_expression> pascal_expressions    ) {
        this.pascal_expressions = pascal_expressions;
    }


    public pascal_variable getPascal_variable() {
        return pascal_variable;
    }

    public void setPascal_variable(pascal_variable pascal_variable) {
        this.pascal_variable = pascal_variable;
    }
    public List<pascal_expression> getPascal_expressions() {
        return pascal_expressions;
    }

    public void addPascal_expression(Pascal_expression pascal_expression) {
        this.pascal_expressions.add(pascal_expression);
    }

}