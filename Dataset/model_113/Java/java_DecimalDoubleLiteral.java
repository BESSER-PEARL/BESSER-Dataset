





import java.util.List;
import java.util.ArrayList;

public class java_DecimalDoubleLiteral extends DoubleLiteral {

    private float decimalValue;



    public java_DecimalDoubleLiteral(
        float decimalValue    ) {
        super(
        );
        this.decimalValue = decimalValue;
    }


    public float getDecimalvalue() {
        return decimalValue;
    }

    public void setDecimalvalue(float decimalValue) {
        this.decimalValue = decimalValue;
    }


}