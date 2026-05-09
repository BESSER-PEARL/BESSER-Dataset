





import java.util.List;
import java.util.ArrayList;

public class ecore_EEnumLiteral extends ENamedElement {

    private String instance;
    private int value;
    private String literal;



    public ecore_EEnumLiteral(
        String instance,        int value,        String literal    ) {
        super(
        );
        this.instance = instance;
        this.value = value;
        this.literal = literal;
    }


    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
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


}