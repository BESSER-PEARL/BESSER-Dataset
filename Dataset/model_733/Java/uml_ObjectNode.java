





import java.util.List;
import java.util.ArrayList;

public class uml_ObjectNode extends ActivityNode, TypedElement {

    private String isControlType;



    public uml_ObjectNode(
        String isControlType    ) {
        super(
        );
        this.isControlType = isControlType;
    }


    public String getIscontroltype() {
        return isControlType;
    }

    public void setIscontroltype(String isControlType) {
        this.isControlType = isControlType;
    }


}