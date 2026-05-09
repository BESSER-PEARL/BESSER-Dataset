





import java.util.List;
import java.util.ArrayList;

public class rtsc_State extends NamedElement, Vertex {

    private boolean final;
    private boolean initial;





    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private List<rtsc_Transition> rtsc_transitions;




    private List<rtsc_Transition> rtsc_transitions;




    private rtsc_Transition rtsc_transition;




    private List<rtsc_Realtimestatechart> rtsc_realtimestatecharts;




    private rtsc_Transition rtsc_transition;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;


    public rtsc_State(
        boolean final,        boolean initial    ) {
        super(
        );
        this.final = final;
        this.initial = initial;
        this.rtsc_transitions = new ArrayList<>();
        this.rtsc_transitions = new ArrayList<>();
        this.rtsc_realtimestatecharts = new ArrayList<>();
    }

    public rtsc_State(
        boolean final,        boolean initial        ArrayList<rtsc_Transition> rtsc_transitions,        ArrayList<rtsc_Transition> rtsc_transitions,        ArrayList<rtsc_Realtimestatechart> rtsc_realtimestatecharts    ) {
        this.final = final;
        this.initial = initial;
        this.rtsc_transitions = rtsc_transitions;
        this.rtsc_transitions = rtsc_transitions;
        this.rtsc_realtimestatecharts = rtsc_realtimestatecharts;
    }

    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public List<rtsc_Transition> getRtsc_transitions() {
        return rtsc_transitions;
    }

    public void addRtsc_transition(Rtsc_transition rtsc_transition) {
        this.rtsc_transitions.add(rtsc_transition);
    }
    public List<rtsc_Transition> getRtsc_transitions() {
        return rtsc_transitions;
    }

    public void addRtsc_transition(Rtsc_transition rtsc_transition) {
        this.rtsc_transitions.add(rtsc_transition);
    }
    public rtsc_Transition getRtsc_transition() {
        return rtsc_transition;
    }

    public void setRtsc_transition(rtsc_Transition rtsc_transition) {
        this.rtsc_transition = rtsc_transition;
    }
    public List<rtsc_Realtimestatechart> getRtsc_realtimestatecharts() {
        return rtsc_realtimestatecharts;
    }

    public void addRtsc_realtimestatechart(Rtsc_realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatecharts.add(rtsc_realtimestatechart);
    }
    public rtsc_Transition getRtsc_transition() {
        return rtsc_transition;
    }

    public void setRtsc_transition(rtsc_Transition rtsc_transition) {
        this.rtsc_transition = rtsc_transition;
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }

}