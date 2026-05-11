





import java.util.List;
import java.util.ArrayList;

public class pascal_addition_operator  {

    private String sign;





    private pascal_simple_expression pascal_simple_expression;


    public pascal_addition_operator(
        String sign    ) {
        this.sign = sign;
    }


    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }

    public pascal_simple_expression getPascal_simple_expression() {
        return pascal_simple_expression;
    }

    public void setPascal_simple_expression(pascal_simple_expression pascal_simple_expression) {
        this.pascal_simple_expression = pascal_simple_expression;
    }

}