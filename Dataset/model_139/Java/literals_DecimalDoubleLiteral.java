





import java.util.List;
import java.util.ArrayList;

public class literals_DecimalDoubleLiteral extends DoubleLiteral {

    private float decimalValue;



    public literals_DecimalDoubleLiteral(
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