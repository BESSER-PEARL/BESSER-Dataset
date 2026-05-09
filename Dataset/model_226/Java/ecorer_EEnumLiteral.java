





import java.util.List;
import java.util.ArrayList;

public class ecorer_EEnumLiteral extends ENamedElement {

    private int value;
    private String literal;
    private String instance;



    public ecorer_EEnumLiteral(
        int value,        String literal,        String instance    ) {
        super(
        );
        this.value = value;
        this.literal = literal;
        this.instance = instance;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
        this.instance = instance;
    }


}