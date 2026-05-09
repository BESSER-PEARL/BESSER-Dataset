





import java.util.List;
import java.util.ArrayList;

public class henshin_Attribute extends GraphElement, ModelElement {

    private String constant;
    private boolean null;
    private String value;





    private henshin_Node henshin_node;




    private henshin_Node henshin_node;


    public henshin_Attribute(
        String constant,        boolean null,        String value    ) {
        super(
        );
        this.constant = constant;
        this.null = null;
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
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public henshin_Node getHenshin_node() {
        return henshin_node;
    }

    public void setHenshin_node(henshin_Node henshin_node) {
        this.henshin_node = henshin_node;
    }
    public henshin_Node getHenshin_node() {
        return henshin_node;
    }

    public void setHenshin_node(henshin_Node henshin_node) {
        this.henshin_node = henshin_node;
    }

}