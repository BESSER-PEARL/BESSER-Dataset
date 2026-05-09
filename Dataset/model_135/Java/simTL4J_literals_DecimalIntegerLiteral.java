





import java.util.List;
import java.util.ArrayList;

public class simTL4J_literals_DecimalIntegerLiteral extends IntegerLiteral {

    private String decimalValue;



    public simTL4J_literals_DecimalIntegerLiteral(
        String decimalValue    ) {
        super(
        );
        this.decimalValue = decimalValue;
    }


    public String getDecimalvalue() {
        return decimalValue;
    }

    public void setDecimalvalue(String decimalValue) {
        this.decimalValue = decimalValue;
    }


}