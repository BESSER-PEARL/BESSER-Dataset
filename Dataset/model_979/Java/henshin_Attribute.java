





import java.util.List;
import java.util.ArrayList;

public class henshin_Attribute extends ModelElement, GraphElement {

    private boolean null;
    private String value;
    private String constant;



    public henshin_Attribute(
        boolean null,        String value,        String constant    ) {
        super(
        );
        this.null = null;
        this.value = value;
        this.constant = constant;
    }


    public boolean getNull() {
        return null;
    }

    public void setNull(boolean null) {
        this.null = null;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }


}