





import java.util.List;
import java.util.ArrayList;

public class expressions_FixedPtLiteral extends Expression {

    private int integerPart;
    private int decimalPart;
    private String value;



    public expressions_FixedPtLiteral(
        int integerPart,        int decimalPart,        String value    ) {
        super(
        );
        this.integerPart = integerPart;
        this.decimalPart = decimalPart;
        this.value = value;
    }


    public int getIntegerpart() {
        return integerPart;
    }

    public void setIntegerpart(int integerPart) {
        this.integerPart = integerPart;
    }
    public int getDecimalpart() {
        return decimalPart;
    }

    public void setDecimalpart(int decimalPart) {
        this.decimalPart = decimalPart;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}