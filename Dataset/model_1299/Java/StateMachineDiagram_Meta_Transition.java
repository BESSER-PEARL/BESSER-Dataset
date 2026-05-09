





import java.util.List;
import java.util.ArrayList;

public class StateMachineDiagram_Meta_Transition  {

    private String trigger;
    private String name;





    private StateMachineDiagram_Meta_StateMachine statemachinediagram_meta_statemachine;




    private StateMachineDiagram_Meta_Vertex statemachinediagram_meta_vertex;




    private List<StateMachineDiagram_Meta_Vertex> statemachinediagram_meta_vertexs;




    private List<StateMachineDiagram_Meta_Vertex> statemachinediagram_meta_vertexs;




    private StateMachineDiagram_Meta_Vertex statemachinediagram_meta_vertex;


    public StateMachineDiagram_Meta_Transition(
        String trigger,        String name    ) {
        this.trigger = trigger;
        this.name = name;
        this.statemachinediagram_meta_vertexs = new ArrayList<>();
        this.statemachinediagram_meta_vertexs = new ArrayList<>();
    }

    public StateMachineDiagram_Meta_Transition(
        String trigger,        String name        ArrayList<StateMachineDiagram_Meta_Vertex> statemachinediagram_meta_vertexs,        ArrayList<StateMachineDiagram_Meta_Vertex> statemachinediagram_meta_vertexs    ) {
        this.trigger = trigger;
        this.name = name;
        this.statemachinediagram_meta_vertexs = statemachinediagram_meta_vertexs;
        this.statemachinediagram_meta_vertexs = statemachinediagram_meta_vertexs;
    }

    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public StateMachineDiagram_Meta_StateMachine getStatemachinediagram_meta_statemachine() {
        return statemachinediagram_meta_statemachine;
    }

    public void setStatemachinediagram_meta_statemachine(StateMachineDiagram_Meta_StateMachine statemachinediagram_meta_statemachine) {
        this.statemachinediagram_meta_statemachine = statemachinediagram_meta_statemachine;
    }
    public StateMachineDiagram_Meta_Vertex getStatemachinediagram_meta_vertex() {
        return statemachinediagram_meta_vertex;
    }

    public void setStatemachinediagram_meta_vertex(StateMachineDiagram_Meta_Vertex statemachinediagram_meta_vertex) {
        this.statemachinediagram_meta_vertex = statemachinediagram_meta_vertex;
    }
    public List<StateMachineDiagram_Meta_Vertex> getStatemachinediagram_meta_vertexs() {
        return statemachinediagram_meta_vertexs;
    }

    public void addStatemachinediagram_meta_vertex(Statemachinediagram_meta_vertex statemachinediagram_meta_vertex) {
        this.statemachinediagram_meta_vertexs.add(statemachinediagram_meta_vertex);
    }
    public List<StateMachineDiagram_Meta_Vertex> getStatemachinediagram_meta_vertexs() {
        return statemachinediagram_meta_vertexs;
    }

    public void addStatemachinediagram_meta_vertex(Statemachinediagram_meta_vertex statemachinediagram_meta_vertex) {
        this.statemachinediagram_meta_vertexs.add(statemachinediagram_meta_vertex);
    }
    public StateMachineDiagram_Meta_Vertex getStatemachinediagram_meta_vertex() {
        return statemachinediagram_meta_vertex;
    }

    public void setStatemachinediagram_meta_vertex(StateMachineDiagram_Meta_Vertex statemachinediagram_meta_vertex) {
        this.statemachinediagram_meta_vertex = statemachinediagram_meta_vertex;
    }

}