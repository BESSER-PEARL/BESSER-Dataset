





import java.util.List;
import java.util.ArrayList;

public class iec61131_literals_Real_Literal extends Numeric_Literal {

    private boolean negative;
    private String exponent;



    public iec61131_literals_Real_Literal(
        boolean negative,        String exponent    ) {
        super(
        );
        this.negative = negative;
        this.exponent = exponent;
    }


    public boolean getNegative() {
        return negative;
    }

    public void setNegative(boolean negative) {
        this.negative = negative;
    }
    public String getExponent() {
        return exponent;
    }

    public void setExponent(String exponent) {
        this.exponent = exponent;
    }


}