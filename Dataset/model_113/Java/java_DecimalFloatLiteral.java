





import java.util.List;
import java.util.ArrayList;

public class java_DecimalFloatLiteral extends FloatLiteral {

    private float decimalValue;



    public java_DecimalFloatLiteral(
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