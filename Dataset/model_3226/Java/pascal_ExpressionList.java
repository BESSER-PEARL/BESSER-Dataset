





import java.util.List;
import java.util.ArrayList;

public class pascal_ExpressionList  {






    private List<pascal_expression> pascal_expressions;




    private pascal_Variable1 pascal_variable1;


    public pascal_ExpressionList(
    ) {
        this.pascal_expressions = new ArrayList<>();
    }

    public pascal_ExpressionList(
        ArrayList<pascal_expression> pascal_expressions    ) {
        this.pascal_expressions = pascal_expressions;
    }


    public List<pascal_expression> getPascal_expressions() {
        return pascal_expressions;
    }

    public void addPascal_expression(Pascal_expression pascal_expression) {
        this.pascal_expressions.add(pascal_expression);
    }
    public pascal_Variable1 getPascal_variable1() {
        return pascal_variable1;
    }

    public void setPascal_variable1(pascal_Variable1 pascal_variable1) {
        this.pascal_variable1 = pascal_variable1;
    }

}