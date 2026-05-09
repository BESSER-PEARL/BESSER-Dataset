





import java.util.List;
import java.util.ArrayList;

public class uml_ObjectFlow extends ActivityEdge {

    private String isMulticast;
    private String isMultireceive;





    private uml_Behavior uml_behavior;




    private uml_Behavior uml_behavior;


    public uml_ObjectFlow(
        String isMulticast,        String isMultireceive    ) {
        super(
        );
        this.isMulticast = isMulticast;
        this.isMultireceive = isMultireceive;
    }


    public String getIsmulticast() {
        return isMulticast;
    }

    public void setIsmulticast(String isMulticast) {
        this.isMulticast = isMulticast;
    }
    public String getIsmultireceive() {
        return isMultireceive;
    }

    public void setIsmultireceive(String isMultireceive) {
        this.isMultireceive = isMultireceive;
    }

    public uml_Behavior getUml_behavior() {
        return uml_behavior;
    }

    public void setUml_behavior(uml_Behavior uml_behavior) {
        this.uml_behavior = uml_behavior;
    }
    public uml_Behavior getUml_behavior() {
        return uml_behavior;
    }

    public void setUml_behavior(uml_Behavior uml_behavior) {
        this.uml_behavior = uml_behavior;
    }

}