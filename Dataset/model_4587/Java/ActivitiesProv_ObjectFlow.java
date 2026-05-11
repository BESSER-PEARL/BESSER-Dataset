





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_ObjectFlow extends ActivityEdge {

    private boolean isMulticast;
    private boolean isMultireceive;
    private boolean isControlType;





    private ActivitiesProv_DecisionNode activitiesprov_decisionnode;


    public ActivitiesProv_ObjectFlow(
        boolean isMulticast,        boolean isMultireceive,        boolean isControlType    ) {
        super(
        );
        this.isMulticast = isMulticast;
        this.isMultireceive = isMultireceive;
        this.isControlType = isControlType;
    }


    public boolean getIsmulticast() {
        return isMulticast;
    }

    public void setIsmulticast(boolean isMulticast) {
        this.isMulticast = isMulticast;
    }
    public boolean getIsmultireceive() {
        return isMultireceive;
    }

    public void setIsmultireceive(boolean isMultireceive) {
        this.isMultireceive = isMultireceive;
    }
    public boolean getIscontroltype() {
        return isControlType;
    }

    public void setIscontroltype(boolean isControlType) {
        this.isControlType = isControlType;
    }

    public ActivitiesProv_DecisionNode getActivitiesprov_decisionnode() {
        return activitiesprov_decisionnode;
    }

    public void setActivitiesprov_decisionnode(ActivitiesProv_DecisionNode activitiesprov_decisionnode) {
        this.activitiesprov_decisionnode = activitiesprov_decisionnode;
    }

}