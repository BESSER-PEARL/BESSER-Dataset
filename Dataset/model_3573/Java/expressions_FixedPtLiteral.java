





import java.util.List;
import java.util.ArrayList;

public class expressions_FixedPtLiteral extends Expression {

    private int decimalPart;
    private String value;
    private int integerPart;



    public expressions_FixedPtLiteral(
        int decimalPart,        String value,        int integerPart    ) {
        super(
        );
        this.decimalPart = decimalPart;
        this.value = value;
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
    public int getIntegerpart() {
        return integerPart;
    }

    public void setIntegerpart(int integerPart) {
        this.integerPart = integerPart;
    }


}