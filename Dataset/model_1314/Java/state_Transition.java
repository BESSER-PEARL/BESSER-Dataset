





import java.util.List;
import java.util.ArrayList;

public class state_Transition extends NamedElement {

    private String kind;





    private state_Vertex state_vertex;




    private state_Constraint state_constraint;




    private state_Vertex state_vertex;




    private state_Vertex state_vertex;




    private state_Vertex state_vertex;




    private state_Trigger state_trigger;


    public state_Transition(
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

    public state_Vertex getState_vertex() {
        return state_vertex;
    }

    public void setState_vertex(state_Vertex state_vertex) {
        this.state_vertex = state_vertex;
    }
    public state_Constraint getState_constraint() {
        return state_constraint;
    }

    public void setState_constraint(state_Constraint state_constraint) {
        this.state_constraint = state_constraint;
    }
    public state_Vertex getState_vertex() {
        return state_vertex;
    }

    public void setState_vertex(state_Vertex state_vertex) {
        this.state_vertex = state_vertex;
    }
    public state_Vertex getState_vertex() {
        return state_vertex;
    }

    public void setState_vertex(state_Vertex state_vertex) {
        this.state_vertex = state_vertex;
    }
    public state_Vertex getState_vertex() {
        return state_vertex;
    }

    public void setState_vertex(state_Vertex state_vertex) {
        this.state_vertex = state_vertex;
    }
    public state_Trigger getState_trigger() {
        return state_trigger;
    }

    public void setState_trigger(state_Trigger state_trigger) {
        this.state_trigger = state_trigger;
    }

}