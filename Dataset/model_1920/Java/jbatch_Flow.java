





import java.util.List;
import java.util.ArrayList;

public class jbatch_Flow  {

    private String next1;
    private String id;
    private String group;
    private String transitionElements;





    private List<jbatch_Step> jbatch_steps;




    private List<jbatch_Stop> jbatch_stops;




    private jbatch_Split jbatch_split;




    private List<jbatch_Flow> jbatch_flows;




    private List<jbatch_Split> jbatch_splits;


    public jbatch_Flow(
        String next1,        String id,        String group,        String transitionElements    ) {
        this.next1 = next1;
        this.id = id;
        this.group = group;
        this.transitionElements = transitionElements;
        this.jbatch_steps = new ArrayList<>();
        this.jbatch_stops = new ArrayList<>();
        this.jbatch_flows = new ArrayList<>();
        this.jbatch_splits = new ArrayList<>();
    }

    public jbatch_Flow(
        String next1,        String id,        String group,        String transitionElements        ArrayList<jbatch_Step> jbatch_steps,        ArrayList<jbatch_Stop> jbatch_stops,        ArrayList<jbatch_Flow> jbatch_flows,        ArrayList<jbatch_Split> jbatch_splits    ) {
        this.next1 = next1;
        this.id = id;
        this.group = group;
        this.transitionElements = transitionElements;
        this.jbatch_steps = jbatch_steps;
        this.jbatch_stops = jbatch_stops;
        this.jbatch_flows = jbatch_flows;
        this.jbatch_splits = jbatch_splits;
    }

    public String getNext1() {
        return next1;
    }

    public void setNext1(String next1) {
        this.next1 = next1;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getTransitionelements() {
        return transitionElements;
    }

    public void setTransitionelements(String transitionElements) {
        this.transitionElements = transitionElements;
    }

    public List<jbatch_Step> getJbatch_steps() {
        return jbatch_steps;
    }

    public void addJbatch_step(Jbatch_step jbatch_step) {
        this.jbatch_steps.add(jbatch_step);
    }
    public List<jbatch_Stop> getJbatch_stops() {
        return jbatch_stops;
    }

    public void addJbatch_stop(Jbatch_stop jbatch_stop) {
        this.jbatch_stops.add(jbatch_stop);
    }
    public jbatch_Split getJbatch_split() {
        return jbatch_split;
    }

    public void setJbatch_split(jbatch_Split jbatch_split) {
        this.jbatch_split = jbatch_split;
    }
    public List<jbatch_Flow> getJbatch_flows() {
        return jbatch_flows;
    }

    public void addJbatch_flow(Jbatch_flow jbatch_flow) {
        this.jbatch_flows.add(jbatch_flow);
    }
    public List<jbatch_Split> getJbatch_splits() {
        return jbatch_splits;
    }

    public void addJbatch_split(Jbatch_split jbatch_split) {
        this.jbatch_splits.add(jbatch_split);
    }

}