





import java.util.List;
import java.util.ArrayList;

public class TTMCConstraint_DecimalLiteralExpression extends ArithmeticLiteralExpression {

    private String value;



    public TTMCConstraint_DecimalLiteralExpression(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}