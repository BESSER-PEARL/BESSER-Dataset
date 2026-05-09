





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ActivityEdge extends RedefinableElement {

    private String redefinedEdge;
    private String inStructuredNode;
    private String activity;
    private String source;
    private String target;
    private String inPartition;
    private String inGroup;
    private String interrupts;





    private UMLModel_ValueSpecification umlmodel_valuespecification;




    private UMLModel_ValueSpecification umlmodel_valuespecification;




    private UMLModel_StructuredActivityNode umlmodel_structuredactivitynode;


    public UMLModel_ActivityEdge(
        String redefinedEdge,        String inStructuredNode,        String activity,        String source,        String target,        String inPartition,        String inGroup,        String interrupts    ) {
        super(
        );
        this.redefinedEdge = redefinedEdge;
        this.inStructuredNode = inStructuredNode;
        this.activity = activity;
        this.source = source;
        this.target = target;
        this.inPartition = inPartition;
        this.inGroup = inGroup;
        this.interrupts = interrupts;
    }


    public String getRedefinededge() {
        return redefinedEdge;
    }

    public void setRedefinededge(String redefinedEdge) {
        this.redefinedEdge = redefinedEdge;
    }
    public String getInstructurednode() {
        return inStructuredNode;
    }

    public void setInstructurednode(String inStructuredNode) {
        this.inStructuredNode = inStructuredNode;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getInpartition() {
        return inPartition;
    }

    public void setInpartition(String inPartition) {
        this.inPartition = inPartition;
    }
    public String getIngroup() {
        return inGroup;
    }

    public void setIngroup(String inGroup) {
        this.inGroup = inGroup;
    }
    public String getInterrupts() {
        return interrupts;
    }

    public void setInterrupts(String interrupts) {
        this.interrupts = interrupts;
    }

    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }
    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }
    public UMLModel_StructuredActivityNode getUmlmodel_structuredactivitynode() {
        return umlmodel_structuredactivitynode;
    }

    public void setUmlmodel_structuredactivitynode(UMLModel_StructuredActivityNode umlmodel_structuredactivitynode) {
        this.umlmodel_structuredactivitynode = umlmodel_structuredactivitynode;
    }

}