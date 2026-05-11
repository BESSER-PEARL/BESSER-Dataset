





import java.util.List;
import java.util.ArrayList;

public class ram_Operation extends NamedElement, MappableElement, Traceable {

    private boolean abstract;
    private boolean static;
    private String extendedVisibility;
    private String operationType;





    private ram_Transition ram_transition;




    private ram_AspectMessageView ram_aspectmessageview;




    private ram_Classifier ram_classifier;




    private ram_Type ram_type;


    public ram_Operation(
        boolean abstract,        boolean static,        String extendedVisibility,        String operationType    ) {
        super(
        );
        this.abstract = abstract;
        this.static = static;
        this.extendedVisibility = extendedVisibility;
        this.operationType = operationType;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getExtendedvisibility() {
        return extendedVisibility;
    }

    public void setExtendedvisibility(String extendedVisibility) {
        this.extendedVisibility = extendedVisibility;
    }
    public String getOperationtype() {
        return operationType;
    }

    public void setOperationtype(String operationType) {
        this.operationType = operationType;
    }

    public ram_Transition getRam_transition() {
        return ram_transition;
    }

    public void setRam_transition(ram_Transition ram_transition) {
        this.ram_transition = ram_transition;
    }
    public ram_AspectMessageView getRam_aspectmessageview() {
        return ram_aspectmessageview;
    }

    public void setRam_aspectmessageview(ram_AspectMessageView ram_aspectmessageview) {
        this.ram_aspectmessageview = ram_aspectmessageview;
    }
    public ram_Classifier getRam_classifier() {
        return ram_classifier;
    }

    public void setRam_classifier(ram_Classifier ram_classifier) {
        this.ram_classifier = ram_classifier;
    }
    public ram_Type getRam_type() {
        return ram_type;
    }

    public void setRam_type(ram_Type ram_type) {
        this.ram_type = ram_type;
    }

}