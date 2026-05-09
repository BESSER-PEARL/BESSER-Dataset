





import java.util.List;
import java.util.ArrayList;

public class graphbt_StandardNode extends Node {

    private String componentRef;
    private String operator;
    private String traceabilityLink;
    private String label;
    private String behaviorRef;
    private String traceabilityStatus;
    private boolean leaf;





    private graphbt_StandardNode graphbt_standardnode;




    private graphbt_BEModel graphbt_bemodel;




    private graphbt_BEModel graphbt_bemodel;


    public graphbt_StandardNode(
        String componentRef,        String operator,        String traceabilityLink,        String label,        String behaviorRef,        String traceabilityStatus,        boolean leaf    ) {
        super(
        );
        this.componentRef = componentRef;
        this.operator = operator;
        this.traceabilityLink = traceabilityLink;
        this.label = label;
        this.behaviorRef = behaviorRef;
        this.traceabilityStatus = traceabilityStatus;
        this.leaf = leaf;
    }


    public String getComponentref() {
        return componentRef;
    }

    public void setComponentref(String componentRef) {
        this.componentRef = componentRef;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getTraceabilitylink() {
        return traceabilityLink;
    }

    public void setTraceabilitylink(String traceabilityLink) {
        this.traceabilityLink = traceabilityLink;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getBehaviorref() {
        return behaviorRef;
    }

    public void setBehaviorref(String behaviorRef) {
        this.behaviorRef = behaviorRef;
    }
    public String getTraceabilitystatus() {
        return traceabilityStatus;
    }

    public void setTraceabilitystatus(String traceabilityStatus) {
        this.traceabilityStatus = traceabilityStatus;
    }
    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }

    public graphbt_StandardNode getGraphbt_standardnode() {
        return graphbt_standardnode;
    }

    public void setGraphbt_standardnode(graphbt_StandardNode graphbt_standardnode) {
        this.graphbt_standardnode = graphbt_standardnode;
    }
    public graphbt_BEModel getGraphbt_bemodel() {
        return graphbt_bemodel;
    }

    public void setGraphbt_bemodel(graphbt_BEModel graphbt_bemodel) {
        this.graphbt_bemodel = graphbt_bemodel;
    }
    public graphbt_BEModel getGraphbt_bemodel() {
        return graphbt_bemodel;
    }

    public void setGraphbt_bemodel(graphbt_BEModel graphbt_bemodel) {
        this.graphbt_bemodel = graphbt_bemodel;
    }

}