





import java.util.List;
import java.util.ArrayList;

public class stateChart_Transient  {

    private String name;
    private String trigger;
    private String effect;
    private int priority;
    private String guard;





    private stateChart_Vertex statechart_vertex;




    private stateChart_Vertex statechart_vertex;




    private stateChart_Region statechart_region;


    public stateChart_Transient(
        String name,        String trigger,        String effect,        int priority,        String guard    ) {
        this.name = name;
        this.trigger = trigger;
        this.effect = effect;
        this.priority = priority;
        this.guard = guard;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }

    public stateChart_Vertex getStatechart_vertex() {
        return statechart_vertex;
    }

    public void setStatechart_vertex(stateChart_Vertex statechart_vertex) {
        this.statechart_vertex = statechart_vertex;
    }
    public stateChart_Vertex getStatechart_vertex() {
        return statechart_vertex;
    }

    public void setStatechart_vertex(stateChart_Vertex statechart_vertex) {
        this.statechart_vertex = statechart_vertex;
    }
    public stateChart_Region getStatechart_region() {
        return statechart_region;
    }

    public void setStatechart_region(stateChart_Region statechart_region) {
        this.statechart_region = statechart_region;
    }

}