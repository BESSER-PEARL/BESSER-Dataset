





import java.util.List;
import java.util.ArrayList;

public class GraphML_Key extends Element {

    private String for_;
    private String type;
    private String defValue;
    private String attrName;



    public GraphML_Key(
        String for_,        String type,        String defValue,        String attrName    ) {
        super(
        );
        this.for_ = for_;
        this.type = type;
        this.defValue = defValue;
        this.attrName = attrName;
    }


    public String getFor_() {
        return for_;
    }

    public void setFor_(String for_) {
        this.for_ = for_;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDefvalue() {
        return defValue;
    }

    public void setDefvalue(String defValue) {
        this.defValue = defValue;
    }
    public String getAttrname() {
        return attrName;
    }

    public void setAttrname(String attrName) {
        this.attrName = attrName;
    }


}