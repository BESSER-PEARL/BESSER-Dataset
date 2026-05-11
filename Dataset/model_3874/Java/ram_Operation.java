





import java.util.List;
import java.util.ArrayList;

public class ram_Operation extends NamedElement, MappableElement, Traceable {

    private String operationType;
    private boolean abstract;
    private String extendedVisibility;
    private boolean static;





    private ram_AspectMessageView ram_aspectmessageview;




    private ram_Type ram_type;


    public ram_Operation(
        String operationType,        boolean abstract,        String extendedVisibility,        boolean static    ) {
        super(
        );
        this.operationType = operationType;
        this.abstract = abstract;
        this.extendedVisibility = extendedVisibility;
        this.static = static;
    }


    public String getOperationtype() {
        return operationType;
    }

    public void setOperationtype(String operationType) {
        this.operationType = operationType;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getExtendedvisibility() {
        return extendedVisibility;
    }

    public void setExtendedvisibility(String extendedVisibility) {
        this.extendedVisibility = extendedVisibility;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public ram_AspectMessageView getRam_aspectmessageview() {
        return ram_aspectmessageview;
    }

    public void setRam_aspectmessageview(ram_AspectMessageView ram_aspectmessageview) {
        this.ram_aspectmessageview = ram_aspectmessageview;
    }
    public ram_Type getRam_type() {
        return ram_type;
    }

    public void setRam_type(ram_Type ram_type) {
        this.ram_type = ram_type;
    }

}