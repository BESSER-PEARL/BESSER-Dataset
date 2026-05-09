





import java.util.List;
import java.util.ArrayList;

public class ecore_EEnumLiteral extends ENamedElement {

    private String literal;
    private String instance;
    private String value;



    public ecore_EEnumLiteral(
        String literal,        String instance,        String value    ) {
        super(
        );
        this.literal = literal;
        this.instance = instance;
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
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}