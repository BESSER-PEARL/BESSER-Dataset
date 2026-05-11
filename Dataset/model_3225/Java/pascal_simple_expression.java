





import java.util.List;
import java.util.ArrayList;

public class pascal_simple_expression  {

    private String sign;





    private pascal_expression pascal_expression;


    public pascal_simple_expression(
        String sign    ) {
        this.sign = sign;
    }


    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }

    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }

}