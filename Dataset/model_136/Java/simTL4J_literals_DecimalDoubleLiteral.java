





import java.util.List;
import java.util.ArrayList;

public class simTL4J_literals_DecimalDoubleLiteral extends DoubleLiteral {

    private float decimalValue;



    public simTL4J_literals_DecimalDoubleLiteral(
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