





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Transition extends RedefinableElement {

    private String kind;





    private UML2WithID_Constraint uml2withid_constraint;




    private UML2WithID_Vertex uml2withid_vertex;




    private UML2WithID_Region uml2withid_region;




    private UML2WithID_Transition uml2withid_transition;




    private UML2WithID_Vertex uml2withid_vertex;




    private UML2WithID_Vertex uml2withid_vertex;




    private UML2WithID_Activity uml2withid_activity;




    private UML2WithID_Vertex uml2withid_vertex;




    private List<UML2WithID_Trigger> uml2withid_triggers;




    private UML2WithID_Region uml2withid_region;


    public UML2WithID_Transition(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml2withid_triggers = new ArrayList<>();
    }

    public UML2WithID_Transition(
        String kind        ArrayList<UML2WithID_Trigger> uml2withid_triggers    ) {
        this.kind = kind;
        this.uml2withid_triggers = uml2withid_triggers;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public UML2WithID_Constraint getUml2withid_constraint() {
        return uml2withid_constraint;
    }

    public void setUml2withid_constraint(UML2WithID_Constraint uml2withid_constraint) {
        this.uml2withid_constraint = uml2withid_constraint;
    }
    public UML2WithID_Vertex getUml2withid_vertex() {
        return uml2withid_vertex;
    }

    public void setUml2withid_vertex(UML2WithID_Vertex uml2withid_vertex) {
        this.uml2withid_vertex = uml2withid_vertex;
    }
    public UML2WithID_Region getUml2withid_region() {
        return uml2withid_region;
    }

    public void setUml2withid_region(UML2WithID_Region uml2withid_region) {
        this.uml2withid_region = uml2withid_region;
    }
    public UML2WithID_Transition getUml2withid_transition() {
        return uml2withid_transition;
    }

    public void setUml2withid_transition(UML2WithID_Transition uml2withid_transition) {
        this.uml2withid_transition = uml2withid_transition;
    }
    public UML2WithID_Vertex getUml2withid_vertex() {
        return uml2withid_vertex;
    }

    public void setUml2withid_vertex(UML2WithID_Vertex uml2withid_vertex) {
        this.uml2withid_vertex = uml2withid_vertex;
    }
    public UML2WithID_Vertex getUml2withid_vertex() {
        return uml2withid_vertex;
    }

    public void setUml2withid_vertex(UML2WithID_Vertex uml2withid_vertex) {
        this.uml2withid_vertex = uml2withid_vertex;
    }
    public UML2WithID_Activity getUml2withid_activity() {
        return uml2withid_activity;
    }

    public void setUml2withid_activity(UML2WithID_Activity uml2withid_activity) {
        this.uml2withid_activity = uml2withid_activity;
    }
    public UML2WithID_Vertex getUml2withid_vertex() {
        return uml2withid_vertex;
    }

    public void setUml2withid_vertex(UML2WithID_Vertex uml2withid_vertex) {
        this.uml2withid_vertex = uml2withid_vertex;
    }
    public List<UML2WithID_Trigger> getUml2withid_triggers() {
        return uml2withid_triggers;
    }

    public void addUml2withid_trigger(Uml2withid_trigger uml2withid_trigger) {
        this.uml2withid_triggers.add(uml2withid_trigger);
    }
    public UML2WithID_Region getUml2withid_region() {
        return uml2withid_region;
    }

    public void setUml2withid_region(UML2WithID_Region uml2withid_region) {
        this.uml2withid_region = uml2withid_region;
    }

}