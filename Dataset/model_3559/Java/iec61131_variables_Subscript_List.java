





import java.util.List;
import java.util.ArrayList;

public class iec61131_variables_Subscript_List  {






    private List<Expression_Types> expression_typess;


    public iec61131_variables_Subscript_List(
    ) {
        this.expression_typess = new ArrayList<>();
    }

    public iec61131_variables_Subscript_List(
        ArrayList<Expression_Types> expression_typess    ) {
        this.expression_typess = expression_typess;
    }


    public List<Expression_Types> getExpression_typess() {
        return expression_typess;
    }

    public void addExpression_types(Expression_types expression_types) {
        this.expression_typess.add(expression_types);
    }

}