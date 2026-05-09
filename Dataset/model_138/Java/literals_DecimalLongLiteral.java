





import java.util.List;
import java.util.ArrayList;

public class literals_DecimalLongLiteral extends LongLiteral {

    private String decimalValue;



    public literals_DecimalLongLiteral(
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