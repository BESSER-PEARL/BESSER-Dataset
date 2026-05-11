





import java.util.List;
import java.util.ArrayList;

public class pascal_simple_expression  {

    private String prefixOperator;
    private String operators;



    public pascal_simple_expression(
        String prefixOperator,        String operators    ) {
        this.prefixOperator = prefixOperator;
        this.operators = operators;
    }


    public String getPrefixoperator() {
        return prefixOperator;
    }

    public void setPrefixoperator(String prefixOperator) {
        this.prefixOperator = prefixOperator;
    }
    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }


}