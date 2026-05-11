





import java.util.List;
import java.util.ArrayList;

public class stateChart_Region  {

    private String name;
    private String note;





    private List<stateChart_Vertex> statechart_vertexs;




    private stateChart_StateMachine statechart_statemachine;




    private stateChart_CompositeState statechart_compositestate;


    public stateChart_Region(
        String name,        String note    ) {
        this.name = name;
        this.note = note;
        this.statechart_vertexs = new ArrayList<>();
    }

    public stateChart_Region(
        String name,        String note        ArrayList<stateChart_Vertex> statechart_vertexs    ) {
        this.name = name;
        this.note = note;
        this.statechart_vertexs = statechart_vertexs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public List<stateChart_Vertex> getStatechart_vertexs() {
        return statechart_vertexs;
    }

    public void addStatechart_vertex(Statechart_vertex statechart_vertex) {
        this.statechart_vertexs.add(statechart_vertex);
    }
    public stateChart_StateMachine getStatechart_statemachine() {
        return statechart_statemachine;
    }

    public void setStatechart_statemachine(stateChart_StateMachine statechart_statemachine) {
        this.statechart_statemachine = statechart_statemachine;
    }
    public stateChart_CompositeState getStatechart_compositestate() {
        return statechart_compositestate;
    }

    public void setStatechart_compositestate(stateChart_CompositeState statechart_compositestate) {
        this.statechart_compositestate = statechart_compositestate;
    }

}