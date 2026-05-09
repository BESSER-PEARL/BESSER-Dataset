





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ActivityNode extends RedefinableElement {

    private String inGroup;
    private String inStructuredNode;
    private String redefinedNode;
    private String activity;
    private String inInterruptibleRegion;
    private String outgoing;
    private String incoming;
    private String inPartition;





    private UMLModel_StructuredActivityNode umlmodel_structuredactivitynode;




    private UMLModel_Activity umlmodel_activity;




    private UMLModel_ActivityGroup umlmodel_activitygroup;


    public UMLModel_ActivityNode(
        String inGroup,        String inStructuredNode,        String redefinedNode,        String activity,        String inInterruptibleRegion,        String outgoing,        String incoming,        String inPartition    ) {
        super(
        );
        this.inGroup = inGroup;
        this.inStructuredNode = inStructuredNode;
        this.redefinedNode = redefinedNode;
        this.activity = activity;
        this.inInterruptibleRegion = inInterruptibleRegion;
        this.outgoing = outgoing;
        this.incoming = incoming;
        this.inPartition = inPartition;
    }


    public String getIngroup() {
        return inGroup;
    }

    public void setIngroup(String inGroup) {
        this.inGroup = inGroup;
    }
    public String getInstructurednode() {
        return inStructuredNode;
    }

    public void setInstructurednode(String inStructuredNode) {
        this.inStructuredNode = inStructuredNode;
    }
    public String getRedefinednode() {
        return redefinedNode;
    }

    public void setRedefinednode(String redefinedNode) {
        this.redefinedNode = redefinedNode;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getIninterruptibleregion() {
        return inInterruptibleRegion;
    }

    public void setIninterruptibleregion(String inInterruptibleRegion) {
        this.inInterruptibleRegion = inInterruptibleRegion;
    }
    public String getOutgoing() {
        return outgoing;
    }

    public void setOutgoing(String outgoing) {
        this.outgoing = outgoing;
    }
    public String getIncoming() {
        return incoming;
    }

    public void setIncoming(String incoming) {
        this.incoming = incoming;
    }
    public String getInpartition() {
        return inPartition;
    }

    public void setInpartition(String inPartition) {
        this.inPartition = inPartition;
    }

    public UMLModel_StructuredActivityNode getUmlmodel_structuredactivitynode() {
        return umlmodel_structuredactivitynode;
    }

    public void setUmlmodel_structuredactivitynode(UMLModel_StructuredActivityNode umlmodel_structuredactivitynode) {
        this.umlmodel_structuredactivitynode = umlmodel_structuredactivitynode;
    }
    public UMLModel_Activity getUmlmodel_activity() {
        return umlmodel_activity;
    }

    public void setUmlmodel_activity(UMLModel_Activity umlmodel_activity) {
        this.umlmodel_activity = umlmodel_activity;
    }
    public UMLModel_ActivityGroup getUmlmodel_activitygroup() {
        return umlmodel_activitygroup;
    }

    public void setUmlmodel_activitygroup(UMLModel_ActivityGroup umlmodel_activitygroup) {
        this.umlmodel_activitygroup = umlmodel_activitygroup;
    }

}