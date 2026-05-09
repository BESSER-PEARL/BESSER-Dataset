





import java.util.List;
import java.util.ArrayList;

public class uml_Transition extends Namespace, RedefinableElement {

    private String kind;





    private uml_Region uml_region;




    private uml_Region uml_region;




    private uml_Transition uml_transition;


    public uml_Transition(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public uml_Region getUml_region() {
        return uml_region;
    }

    public void setUml_region(uml_Region uml_region) {
        this.uml_region = uml_region;
    }
    public uml_Region getUml_region() {
        return uml_region;
    }

    public void setUml_region(uml_Region uml_region) {
        this.uml_region = uml_region;
    }
    public uml_Transition getUml_transition() {
        return uml_transition;
    }

    public void setUml_transition(uml_Transition uml_transition) {
        this.uml_transition = uml_transition;
    }

}