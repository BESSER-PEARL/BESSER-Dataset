





import java.util.List;
import java.util.ArrayList;

public class henshin_Attribute extends ModelElement, GraphElement {

    private String value;
    private String constant;
    private boolean null;





    private henshin_Node henshin_node;




    private henshin_Node henshin_node;


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