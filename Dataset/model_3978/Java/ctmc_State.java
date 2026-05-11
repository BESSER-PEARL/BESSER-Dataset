





import java.util.List;
import java.util.ArrayList;

public class ctmc_State extends IDBase {

    private float exitRate;
    private String name;





    private ctmc_Transition ctmc_transition;




    private ctmc_CTMC ctmc_ctmc;




    private ctmc_CTMC ctmc_ctmc;




    private ctmc_Label ctmc_label;




    private List<ctmc_Transition> ctmc_transitions;




    private List<ctmc_Transition> ctmc_transitions;




    private ctmc_Transition ctmc_transition;




    private List<ctmc_Label> ctmc_labels;


    public ctmc_State(
        float exitRate,        String name    ) {
        super(
        );
        this.exitRate = exitRate;
        this.name = name;
        this.ctmc_transitions = new ArrayList<>();
        this.ctmc_transitions = new ArrayList<>();
        this.ctmc_labels = new ArrayList<>();
    }

    public ctmc_State(
        float exitRate,        String name        ArrayList<ctmc_Transition> ctmc_transitions,        ArrayList<ctmc_Transition> ctmc_transitions,        ArrayList<ctmc_Label> ctmc_labels    ) {
        this.exitRate = exitRate;
        this.name = name;
        this.ctmc_transitions = ctmc_transitions;
        this.ctmc_transitions = ctmc_transitions;
        this.ctmc_labels = ctmc_labels;
    }

    public float getExitrate() {
        return exitRate;
    }

    public void setExitrate(float exitRate) {
        this.exitRate = exitRate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ctmc_Transition getCtmc_transition() {
        return ctmc_transition;
    }

    public void setCtmc_transition(ctmc_Transition ctmc_transition) {
        this.ctmc_transition = ctmc_transition;
    }
    public ctmc_CTMC getCtmc_ctmc() {
        return ctmc_ctmc;
    }

    public void setCtmc_ctmc(ctmc_CTMC ctmc_ctmc) {
        this.ctmc_ctmc = ctmc_ctmc;
    }
    public ctmc_CTMC getCtmc_ctmc() {
        return ctmc_ctmc;
    }

    public void setCtmc_ctmc(ctmc_CTMC ctmc_ctmc) {
        this.ctmc_ctmc = ctmc_ctmc;
    }
    public ctmc_Label getCtmc_label() {
        return ctmc_label;
    }

    public void setCtmc_label(ctmc_Label ctmc_label) {
        this.ctmc_label = ctmc_label;
    }
    public List<ctmc_Transition> getCtmc_transitions() {
        return ctmc_transitions;
    }

    public void addCtmc_transition(Ctmc_transition ctmc_transition) {
        this.ctmc_transitions.add(ctmc_transition);
    }
    public List<ctmc_Transition> getCtmc_transitions() {
        return ctmc_transitions;
    }

    public void addCtmc_transition(Ctmc_transition ctmc_transition) {
        this.ctmc_transitions.add(ctmc_transition);
    }
    public ctmc_Transition getCtmc_transition() {
        return ctmc_transition;
    }

    public void setCtmc_transition(ctmc_Transition ctmc_transition) {
        this.ctmc_transition = ctmc_transition;
    }
    public List<ctmc_Label> getCtmc_labels() {
        return ctmc_labels;
    }

    public void addCtmc_label(Ctmc_label ctmc_label) {
        this.ctmc_labels.add(ctmc_label);
    }

}