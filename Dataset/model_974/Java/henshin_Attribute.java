





import java.util.List;
import java.util.ArrayList;

public class henshin_Attribute extends ModelElement, GraphElement {

    private String value;
    private String constant;
    private boolean null;



    public henshin_Attribute(
        String value,        String constant,        boolean null    ) {
        super(
        );
        this.value = value;
        this.constant = constant;
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
    public boolean getNull() {
        return null;
    }

    public void setNull(boolean null) {
        this.null = null;
    }


}