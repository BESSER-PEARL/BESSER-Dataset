





import java.util.List;
import java.util.ArrayList;

public class UML2_Transition extends RedefinableElement {

    private String kind;





    private UML2_Region uml2_region;




    private UML2_Vertex uml2_vertex;




    private UML2_Vertex uml2_vertex;




    private UML2_Region uml2_region;




    private UML2_Constraint uml2_constraint;




    private UML2_Transition uml2_transition;




    private UML2_Vertex uml2_vertex;




    private UML2_Vertex uml2_vertex;




    private List<UML2_Trigger> uml2_triggers;


    public UML2_Transition(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.uml2_triggers = new ArrayList<>();
    }

    public UML2_Transition(
        String kind        ArrayList<UML2_Trigger> uml2_triggers    ) {
        this.kind = kind;
        this.uml2_triggers = uml2_triggers;
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
    public UML2_Vertex getUml2_vertex() {
        return uml2_vertex;
    }

    public void setUml2_vertex(UML2_Vertex uml2_vertex) {
        this.uml2_vertex = uml2_vertex;
    }
    public UML2_Vertex getUml2_vertex() {
        return uml2_vertex;
    }

    public void setUml2_vertex(UML2_Vertex uml2_vertex) {
        this.uml2_vertex = uml2_vertex;
    }
    public UML2_Region getUml2_region() {
        return uml2_region;
    }

    public void setUml2_region(UML2_Region uml2_region) {
        this.uml2_region = uml2_region;
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }
    public UML2_Transition getUml2_transition() {
        return uml2_transition;
    }

    public void setUml2_transition(UML2_Transition uml2_transition) {
        this.uml2_transition = uml2_transition;
    }
    public UML2_Vertex getUml2_vertex() {
        return uml2_vertex;
    }

    public void setUml2_vertex(UML2_Vertex uml2_vertex) {
        this.uml2_vertex = uml2_vertex;
    }
    public UML2_Vertex getUml2_vertex() {
        return uml2_vertex;
    }

    public void setUml2_vertex(UML2_Vertex uml2_vertex) {
        this.uml2_vertex = uml2_vertex;
    }
    public List<UML2_Trigger> getUml2_triggers() {
        return uml2_triggers;
    }

    public void addUml2_trigger(Uml2_trigger uml2_trigger) {
        this.uml2_triggers.add(uml2_trigger);
    }

}