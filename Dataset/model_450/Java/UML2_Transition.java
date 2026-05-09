





import java.util.List;
import java.util.ArrayList;

public class UML2_Transition extends RedefinableElement {

    private String kind;





    private UML2_Region uml2_region;




    private UML2_Region uml2_region;




    private UML2_Transition uml2_transition;




    private UML2_Constraint uml2_constraint;


    public UML2_Transition(
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

    public UML2_Region getUml2_region() {
        return uml2_region;
    }

    public void setUml2_region(UML2_Region uml2_region) {
        this.uml2_region = uml2_region;
    }
    public UML2_Region getUml2_region() {
        return uml2_region;
    }

    public void setUml2_region(UML2_Region uml2_region) {
        this.uml2_region = uml2_region;
    }
    public UML2_Transition getUml2_transition() {
        return uml2_transition;
    }

    public void setUml2_transition(UML2_Transition uml2_transition) {
        this.uml2_transition = uml2_transition;
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }

}