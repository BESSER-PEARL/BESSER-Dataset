





import java.util.List;
import java.util.ArrayList;

public class StateMachines_Transition  {

    private String kind;





    private StateMachines_Region statemachines_region;




    private StateMachines_Vertex statemachines_vertex;




    private StateMachines_Vertex statemachines_vertex;


    public StateMachines_Transition(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public StateMachines_Region getStatemachines_region() {
        return statemachines_region;
    }

    public void setStatemachines_region(StateMachines_Region statemachines_region) {
        this.statemachines_region = statemachines_region;
    }
    public StateMachines_Vertex getStatemachines_vertex() {
        return statemachines_vertex;
    }

    public void setStatemachines_vertex(StateMachines_Vertex statemachines_vertex) {
        this.statemachines_vertex = statemachines_vertex;
    }
    public StateMachines_Vertex getStatemachines_vertex() {
        return statemachines_vertex;
    }

    public void setStatemachines_vertex(StateMachines_Vertex statemachines_vertex) {
        this.statemachines_vertex = statemachines_vertex;
    }

}