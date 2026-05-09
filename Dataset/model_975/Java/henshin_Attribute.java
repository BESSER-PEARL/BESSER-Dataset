





import java.util.List;
import java.util.ArrayList;

public class henshin_Attribute extends ModelElement, GraphElement {

    private boolean null;
    private String constant;
    private String value;



    public henshin_Attribute(
        boolean null,        String constant,        String value    ) {
        super(
        );
        this.null = null;
        this.constant = constant;
        this.value = value;
    }


    public boolean getNull() {
        return null;
    }

    public void setNull(boolean null) {
        this.null = null;
    }
    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}