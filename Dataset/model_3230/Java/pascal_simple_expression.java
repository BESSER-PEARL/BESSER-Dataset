





import java.util.List;
import java.util.ArrayList;

public class pascal_simple_expression  {

    private String operators;
    private String prefixOperator;





    private pascal_expression pascal_expression;


    public pascal_simple_expression(
        String operators,        String prefixOperator    ) {
        this.operators = operators;
        this.prefixOperator = prefixOperator;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }
    public String getPrefixoperator() {
        return prefixOperator;
    }

    public void setPrefixoperator(String prefixOperator) {
        this.prefixOperator = prefixOperator;
    }

    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }

}