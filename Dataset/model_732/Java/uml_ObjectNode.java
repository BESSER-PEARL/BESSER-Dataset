





import java.util.List;
import java.util.ArrayList;

public class uml_ObjectNode extends ActivityNode, TypedElement {

    private String ordering;
    private String isControlType;



    public uml_ObjectNode(
        String ordering,        String isControlType    ) {
        super(
        );
        this.ordering = ordering;
        this.isControlType = isControlType;
    }


    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public String getIscontroltype() {
        return isControlType;
    }

    public void setIscontroltype(String isControlType) {
        this.isControlType = isControlType;
    }


}