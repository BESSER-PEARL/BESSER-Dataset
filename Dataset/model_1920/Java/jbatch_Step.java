





import java.util.List;
import java.util.ArrayList;

public class jbatch_Step  {

    private String next1;
    private String startLimit;
    private String allowStartIfComplete;
    private String transitionElements;
    private String id;





    private List<jbatch_Stop> jbatch_stops;


    public jbatch_Step(
        String next1,        String startLimit,        String allowStartIfComplete,        String transitionElements,        String id    ) {
        this.next1 = next1;
        this.startLimit = startLimit;
        this.allowStartIfComplete = allowStartIfComplete;
        this.transitionElements = transitionElements;
        this.id = id;
        this.jbatch_stops = new ArrayList<>();
    }

    public jbatch_Step(
        String next1,        String startLimit,        String allowStartIfComplete,        String transitionElements,        String id        ArrayList<jbatch_Stop> jbatch_stops    ) {
        this.next1 = next1;
        this.startLimit = startLimit;
        this.allowStartIfComplete = allowStartIfComplete;
        this.transitionElements = transitionElements;
        this.id = id;
        this.jbatch_stops = jbatch_stops;
    }

    public String getNext1() {
        return next1;
    }

    public void setNext1(String next1) {
        this.next1 = next1;
    }
    public String getStartlimit() {
        return startLimit;
    }

    public void setStartlimit(String startLimit) {
        this.startLimit = startLimit;
    }
    public String getAllowstartifcomplete() {
        return allowStartIfComplete;
    }

    public void setAllowstartifcomplete(String allowStartIfComplete) {
        this.allowStartIfComplete = allowStartIfComplete;
    }
    public String getTransitionelements() {
        return transitionElements;
    }

    public void setTransitionelements(String transitionElements) {
        this.transitionElements = transitionElements;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<jbatch_Stop> getJbatch_stops() {
        return jbatch_stops;
    }

    public void addJbatch_stop(Jbatch_stop jbatch_stop) {
        this.jbatch_stops.add(jbatch_stop);
    }

}