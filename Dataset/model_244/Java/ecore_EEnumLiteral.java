





import java.util.List;
import java.util.ArrayList;

public class ecore_EEnumLiteral extends ENamedElement {

    private String value;
    private String instance;
    private String literal;



    public ecore_EEnumLiteral(
        String value,        String instance,        String literal    ) {
        super(
        );
        this.value = value;
        this.instance = instance;
        this.literal = literal;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
        this.instance = instance;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }


}