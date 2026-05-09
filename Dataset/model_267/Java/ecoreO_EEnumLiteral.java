





import java.util.List;
import java.util.ArrayList;

public class ecoreO_EEnumLiteral extends ENamedElement {

    private String literal;
    private int value;
    private String instance;



    public ecoreO_EEnumLiteral(
        String literal,        int value,        String instance    ) {
        super(
        );
        this.literal = literal;
        this.value = value;
        this.instance = instance;
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
    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
        this.instance = instance;
    }


}