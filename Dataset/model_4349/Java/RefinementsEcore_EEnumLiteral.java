





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EEnumLiteral extends ENamedElement {

    private String literal;
    private int value;



    public RefinementsEcore_EEnumLiteral(
        String literal,        int value    ) {
        super(
        );
        this.literal = literal;
        this.value = value;
    }


    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}