





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ObjectNode extends ActivityNode, TypedElement {

    private String ordering;
    private String isControlType;
    private String inState;
    private String selection;



    public UMLModel_ObjectNode(
        String ordering,        String isControlType,        String inState,        String selection    ) {
        super(
        );
        this.ordering = ordering;
        this.isControlType = isControlType;
        this.inState = inState;
        this.selection = selection;
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
    public String getInstate() {
        return inState;
    }

    public void setInstate(String inState) {
        this.inState = inState;
    }
    public String getSelection() {
        return selection;
    }

    public void setSelection(String selection) {
        this.selection = selection;
    }


}