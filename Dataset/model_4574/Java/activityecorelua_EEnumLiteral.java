





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_EEnumLiteral extends ENamedElement {

    private int value;
    private String instance;
    private String literal;



    public activityecorelua_EEnumLiteral(
        int value,        String instance,        String literal    ) {
        super(
        );
        this.value = value;
        this.instance = instance;
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
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }


}