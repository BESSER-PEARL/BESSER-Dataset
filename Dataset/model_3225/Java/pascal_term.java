





import java.util.List;
import java.util.ArrayList;

public class pascal_term  {

    private String multiplication_operator;





    private pascal_simple_expression pascal_simple_expression;


    public pascal_term(
        String multiplication_operator    ) {
        this.multiplication_operator = multiplication_operator;
    }


    public String getMultiplication_operator() {
        return multiplication_operator;
    }

    public void setMultiplication_operator(String multiplication_operator) {
        this.multiplication_operator = multiplication_operator;
    }

    public pascal_simple_expression getPascal_simple_expression() {
        return pascal_simple_expression;
    }

    public void setPascal_simple_expression(pascal_simple_expression pascal_simple_expression) {
        this.pascal_simple_expression = pascal_simple_expression;
    }

}