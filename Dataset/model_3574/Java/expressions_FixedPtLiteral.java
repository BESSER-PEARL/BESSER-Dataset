





import java.util.List;
import java.util.ArrayList;

public class expressions_FixedPtLiteral extends Expression {

    private int integerPart;
    private String value;
    private int decimalPart;



    public expressions_FixedPtLiteral(
        int integerPart,        String value,        int decimalPart    ) {
        super(
        );
        this.integerPart = integerPart;
        this.value = value;
        this.decimalPart = decimalPart;
    }


    public int getIntegerpart() {
        return integerPart;
    }

    public void setIntegerpart(int integerPart) {
        this.integerPart = integerPart;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public int getDecimalpart() {
        return decimalPart;
    }

    public void setDecimalpart(int decimalPart) {
        this.decimalPart = decimalPart;
    }


}