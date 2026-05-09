





import java.util.List;
import java.util.ArrayList;

public class ecore_EEnumLiteral extends ENamedElement {

    private String value;
    private String literal;
    private String instance;



    public ecore_EEnumLiteral(
        String value,        String literal,        String instance    ) {
        super(
        );
        this.value = value;
        this.literal = literal;
        this.instance = instance;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
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