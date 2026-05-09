





import java.util.List;
import java.util.ArrayList;

public class graphbt_StandardNode extends Node {

    private boolean leaf;
    private String componentRef;
    private String traceabilityStatus;
    private String behaviorRef;
    private String operator;
    private String label;
    private String traceabilityLink;





    private graphbt_StandardNode graphbt_standardnode;


    public graphbt_StandardNode(
        boolean leaf,        String componentRef,        String traceabilityStatus,        String behaviorRef,        String operator,        String label,        String traceabilityLink    ) {
        super(
        );
        this.leaf = leaf;
        this.componentRef = componentRef;
        this.traceabilityStatus = traceabilityStatus;
        this.behaviorRef = behaviorRef;
        this.operator = operator;
        this.label = label;
        this.traceabilityLink = traceabilityLink;
    }


    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }
    public String getComponentref() {
        return componentRef;
    }

    public void setComponentref(String componentRef) {
        this.componentRef = componentRef;
    }
    public String getTraceabilitystatus() {
        return traceabilityStatus;
    }

    public void setTraceabilitystatus(String traceabilityStatus) {
        this.traceabilityStatus = traceabilityStatus;
    }
    public String getBehaviorref() {
        return behaviorRef;
    }

    public void setBehaviorref(String behaviorRef) {
        this.behaviorRef = behaviorRef;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getTraceabilitylink() {
        return traceabilityLink;
    }

    public void setTraceabilitylink(String traceabilityLink) {
        this.traceabilityLink = traceabilityLink;
    }

    public graphbt_StandardNode getGraphbt_standardnode() {
        return graphbt_standardnode;
    }

    public void setGraphbt_standardnode(graphbt_StandardNode graphbt_standardnode) {
        this.graphbt_standardnode = graphbt_standardnode;
    }

}