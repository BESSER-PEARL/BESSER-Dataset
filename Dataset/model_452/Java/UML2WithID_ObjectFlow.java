





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ObjectFlow extends ActivityEdge {

    private boolean isMulticast;
    private boolean isMultireceive;





    private UML2WithID_Behavior uml2withid_behavior;




    private UML2WithID_Behavior uml2withid_behavior;


    public UML2WithID_ObjectFlow(
        boolean isMulticast,        boolean isMultireceive    ) {
        super(
        );
        this.isMulticast = isMulticast;
        this.isMultireceive = isMultireceive;
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

    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }
    public UML2WithID_Behavior getUml2withid_behavior() {
        return uml2withid_behavior;
    }

    public void setUml2withid_behavior(UML2WithID_Behavior uml2withid_behavior) {
        this.uml2withid_behavior = uml2withid_behavior;
    }

}