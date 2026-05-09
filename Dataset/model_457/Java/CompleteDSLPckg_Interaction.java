





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Interaction extends Behavior, InteractionFragment {






    private List<CompleteDSLPckg_Lifeline> completedslpckg_lifelines;




    private List<CompleteDSLPckg_InteractionFragment> completedslpckg_interactionfragments;




    private CompleteDSLPckg_InteractionUse completedslpckg_interactionuse;




    private List<CompleteDSLPckg_Gate> completedslpckg_gates;




    private CompleteDSLPckg_Lifeline completedslpckg_lifeline;




    private List<CompleteDSLPckg_Action> completedslpckg_actions;


    public CompleteDSLPckg_Interaction(
    ) {
        super(
        );
        this.completedslpckg_lifelines = new ArrayList<>();
        this.completedslpckg_interactionfragments = new ArrayList<>();
        this.completedslpckg_gates = new ArrayList<>();
        this.completedslpckg_actions = new ArrayList<>();
    }

    public CompleteDSLPckg_Interaction(
        ArrayList<CompleteDSLPckg_Lifeline> completedslpckg_lifelines,        ArrayList<CompleteDSLPckg_InteractionFragment> completedslpckg_interactionfragments,        ArrayList<CompleteDSLPckg_Gate> completedslpckg_gates,        ArrayList<CompleteDSLPckg_Action> completedslpckg_actions    ) {
        this.completedslpckg_lifelines = completedslpckg_lifelines;
        this.completedslpckg_interactionfragments = completedslpckg_interactionfragments;
        this.completedslpckg_gates = completedslpckg_gates;
        this.completedslpckg_actions = completedslpckg_actions;
    }


    public List<CompleteDSLPckg_Lifeline> getCompletedslpckg_lifelines() {
        return completedslpckg_lifelines;
    }

    public void addCompletedslpckg_lifeline(Completedslpckg_lifeline completedslpckg_lifeline) {
        this.completedslpckg_lifelines.add(completedslpckg_lifeline);
    }
    public List<CompleteDSLPckg_InteractionFragment> getCompletedslpckg_interactionfragments() {
        return completedslpckg_interactionfragments;
    }

    public void addCompletedslpckg_interactionfragment(Completedslpckg_interactionfragment completedslpckg_interactionfragment) {
        this.completedslpckg_interactionfragments.add(completedslpckg_interactionfragment);
    }
    public CompleteDSLPckg_InteractionUse getCompletedslpckg_interactionuse() {
        return completedslpckg_interactionuse;
    }

    public void setCompletedslpckg_interactionuse(CompleteDSLPckg_InteractionUse completedslpckg_interactionuse) {
        this.completedslpckg_interactionuse = completedslpckg_interactionuse;
    }
    public List<CompleteDSLPckg_Gate> getCompletedslpckg_gates() {
        return completedslpckg_gates;
    }

    public void addCompletedslpckg_gate(Completedslpckg_gate completedslpckg_gate) {
        this.completedslpckg_gates.add(completedslpckg_gate);
    }
    public CompleteDSLPckg_Lifeline getCompletedslpckg_lifeline() {
        return completedslpckg_lifeline;
    }

    public void setCompletedslpckg_lifeline(CompleteDSLPckg_Lifeline completedslpckg_lifeline) {
        this.completedslpckg_lifeline = completedslpckg_lifeline;
    }
    public List<CompleteDSLPckg_Action> getCompletedslpckg_actions() {
        return completedslpckg_actions;
    }

    public void addCompletedslpckg_action(Completedslpckg_action completedslpckg_action) {
        this.completedslpckg_actions.add(completedslpckg_action);
    }

}