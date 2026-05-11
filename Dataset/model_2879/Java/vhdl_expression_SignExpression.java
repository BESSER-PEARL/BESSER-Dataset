





import java.util.List;
import java.util.ArrayList;

public class vhdl_expression_SignExpression extends Expression {

    private String sign;



    public vhdl_expression_SignExpression(
        String sign    ) {
        super(
        );
        this.sign = sign;
    }


    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }


}