





import java.util.List;
import java.util.ArrayList;

public class expression_NegativeIntExpression extends SubExpression2 {

    private String isNegative;
    private String value;



    public expression_NegativeIntExpression(
        String isNegative,        String value    ) {
        super(
        );
        this.isNegative = isNegative;
        this.value = value;
    }


    public String getIsnegative() {
        return isNegative;
    }

    public void setIsnegative(String isNegative) {
        this.isNegative = isNegative;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}