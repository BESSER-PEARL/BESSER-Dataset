





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ObjectFlow extends ActivityEdge {

    private String ordering;
    private boolean isControlType;
    private boolean isMulticast;
    private boolean isMultireceive;





    private CompleteDSLPckg_Behavior completedslpckg_behavior;




    private List<CompleteDSLPckg_State> completedslpckg_states;




    private CompleteDSLPckg_Behavior completedslpckg_behavior;




    private CompleteDSLPckg_DecisionNode completedslpckg_decisionnode;


    public CompleteDSLPckg_ObjectFlow(
        String ordering,        boolean isControlType,        boolean isMulticast,        boolean isMultireceive    ) {
        super(
        );
        this.ordering = ordering;
        this.isControlType = isControlType;
        this.isMulticast = isMulticast;
        this.isMultireceive = isMultireceive;
        this.completedslpckg_states = new ArrayList<>();
    }

    public CompleteDSLPckg_ObjectFlow(
        String ordering,        boolean isControlType,        boolean isMulticast,        boolean isMultireceive        ArrayList<CompleteDSLPckg_State> completedslpckg_states    ) {
        this.ordering = ordering;
        this.isControlType = isControlType;
        this.isMulticast = isMulticast;
        this.isMultireceive = isMultireceive;
        this.completedslpckg_states = completedslpckg_states;
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

    public CompleteDSLPckg_Behavior getCompletedslpckg_behavior() {
        return completedslpckg_behavior;
    }

    public void setCompletedslpckg_behavior(CompleteDSLPckg_Behavior completedslpckg_behavior) {
        this.completedslpckg_behavior = completedslpckg_behavior;
    }
    public List<CompleteDSLPckg_State> getCompletedslpckg_states() {
        return completedslpckg_states;
    }

    public void addCompletedslpckg_state(Completedslpckg_state completedslpckg_state) {
        this.completedslpckg_states.add(completedslpckg_state);
    }
    public CompleteDSLPckg_Behavior getCompletedslpckg_behavior() {
        return completedslpckg_behavior;
    }

    public void setCompletedslpckg_behavior(CompleteDSLPckg_Behavior completedslpckg_behavior) {
        this.completedslpckg_behavior = completedslpckg_behavior;
    }
    public CompleteDSLPckg_DecisionNode getCompletedslpckg_decisionnode() {
        return completedslpckg_decisionnode;
    }

    public void setCompletedslpckg_decisionnode(CompleteDSLPckg_DecisionNode completedslpckg_decisionnode) {
        this.completedslpckg_decisionnode = completedslpckg_decisionnode;
    }

}