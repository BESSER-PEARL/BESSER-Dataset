





import java.util.List;
import java.util.ArrayList;

public class jbatch_Decision  {

    private String id;
    private String transitionElements;
    private String ref;





    private List<jbatch_End> jbatch_ends;




    private List<jbatch_Stop> jbatch_stops;




    private List<jbatch_Next> jbatch_nexts;




    private jbatch_Properties jbatch_properties;




    private jbatch_Flow jbatch_flow;




    private List<jbatch_Fail> jbatch_fails;


    public jbatch_Decision(
        String id,        String transitionElements,        String ref    ) {
        this.id = id;
        this.transitionElements = transitionElements;
        this.ref = ref;
        this.jbatch_ends = new ArrayList<>();
        this.jbatch_stops = new ArrayList<>();
        this.jbatch_nexts = new ArrayList<>();
        this.jbatch_fails = new ArrayList<>();
    }

    public jbatch_Decision(
        String id,        String transitionElements,        String ref        ArrayList<jbatch_End> jbatch_ends,        ArrayList<jbatch_Stop> jbatch_stops,        ArrayList<jbatch_Next> jbatch_nexts,        ArrayList<jbatch_Fail> jbatch_fails    ) {
        this.id = id;
        this.transitionElements = transitionElements;
        this.ref = ref;
        this.jbatch_ends = jbatch_ends;
        this.jbatch_stops = jbatch_stops;
        this.jbatch_nexts = jbatch_nexts;
        this.jbatch_fails = jbatch_fails;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTransitionelements() {
        return transitionElements;
    }

    public void setTransitionelements(String transitionElements) {
        this.transitionElements = transitionElements;
    }
    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public List<jbatch_End> getJbatch_ends() {
        return jbatch_ends;
    }

    public void addJbatch_end(Jbatch_end jbatch_end) {
        this.jbatch_ends.add(jbatch_end);
    }
    public List<jbatch_Stop> getJbatch_stops() {
        return jbatch_stops;
    }

    public void addJbatch_stop(Jbatch_stop jbatch_stop) {
        this.jbatch_stops.add(jbatch_stop);
    }
    public List<jbatch_Next> getJbatch_nexts() {
        return jbatch_nexts;
    }

    public void addJbatch_next(Jbatch_next jbatch_next) {
        this.jbatch_nexts.add(jbatch_next);
    }
    public jbatch_Properties getJbatch_properties() {
        return jbatch_properties;
    }

    public void setJbatch_properties(jbatch_Properties jbatch_properties) {
        this.jbatch_properties = jbatch_properties;
    }
    public jbatch_Flow getJbatch_flow() {
        return jbatch_flow;
    }

    public void setJbatch_flow(jbatch_Flow jbatch_flow) {
        this.jbatch_flow = jbatch_flow;
    }
    public List<jbatch_Fail> getJbatch_fails() {
        return jbatch_fails;
    }

    public void addJbatch_fail(Jbatch_fail jbatch_fail) {
        this.jbatch_fails.add(jbatch_fail);
    }

}