





import java.util.List;
import java.util.ArrayList;

public class activity_ObjectNode extends AbstractNamedElement, ActivityNode {

    private String kindOfNode;
    private String ordering;
    private boolean isControlType;





    private activity_ValueSpecification activity_valuespecification;


    public activity_ObjectNode(
        String kindOfNode,        String ordering,        boolean isControlType    ) {
        super(
        );
        this.kindOfNode = kindOfNode;
        this.ordering = ordering;
        this.isControlType = isControlType;
    }


    public String getKindofnode() {
        return kindOfNode;
    }

    public void setKindofnode(String kindOfNode) {
        this.kindOfNode = kindOfNode;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public boolean getIscontroltype() {
        return isControlType;
    }

    public void setIscontroltype(boolean isControlType) {
        this.isControlType = isControlType;
    }

    public activity_ValueSpecification getActivity_valuespecification() {
        return activity_valuespecification;
    }

    public void setActivity_valuespecification(activity_ValueSpecification activity_valuespecification) {
        this.activity_valuespecification = activity_valuespecification;
    }

}