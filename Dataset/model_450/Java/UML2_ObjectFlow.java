





import java.util.List;
import java.util.ArrayList;

public class UML2_ObjectFlow extends ActivityEdge {

    private boolean isMultireceive;
    private boolean isMulticast;





    private UML2_Behavior uml2_behavior;




    private UML2_Behavior uml2_behavior;


    public UML2_ObjectFlow(
        boolean isMultireceive,        boolean isMulticast    ) {
        super(
        );
        this.isMultireceive = isMultireceive;
        this.isMulticast = isMulticast;
    }


    public boolean getIsmultireceive() {
        return isMultireceive;
    }

    public void setIsmultireceive(boolean isMultireceive) {
        this.isMultireceive = isMultireceive;
    }
    public boolean getIsmulticast() {
        return isMulticast;
    }

    public void setIsmulticast(boolean isMulticast) {
        this.isMulticast = isMulticast;
    }

    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }
    public UML2_Behavior getUml2_behavior() {
        return uml2_behavior;
    }

    public void setUml2_behavior(UML2_Behavior uml2_behavior) {
        this.uml2_behavior = uml2_behavior;
    }

}