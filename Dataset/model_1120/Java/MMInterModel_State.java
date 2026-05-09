





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_State extends Element {

    private String duringBehaviour;
    private String stateConfiguration;
    private String entryBehaviour;
    private int stateNumber;
    private String stateMachine;
    private String exitBehaviour;





    private List<MMInterModel_Transition> mmintermodel_transitions;




    private List<MMInterModel_Transition> mmintermodel_transitions;




    private MMInterModel_Transition mmintermodel_transition;




    private MMInterModel_Transition mmintermodel_transition;


    public MMInterModel_State(
        String duringBehaviour,        String stateConfiguration,        String entryBehaviour,        int stateNumber,        String stateMachine,        String exitBehaviour    ) {
        super(
        );
        this.duringBehaviour = duringBehaviour;
        this.stateConfiguration = stateConfiguration;
        this.entryBehaviour = entryBehaviour;
        this.stateNumber = stateNumber;
        this.stateMachine = stateMachine;
        this.exitBehaviour = exitBehaviour;
        this.mmintermodel_transitions = new ArrayList<>();
        this.mmintermodel_transitions = new ArrayList<>();
    }

    public MMInterModel_State(
        String duringBehaviour,        String stateConfiguration,        String entryBehaviour,        int stateNumber,        String stateMachine,        String exitBehaviour        ArrayList<MMInterModel_Transition> mmintermodel_transitions,        ArrayList<MMInterModel_Transition> mmintermodel_transitions    ) {
        this.duringBehaviour = duringBehaviour;
        this.stateConfiguration = stateConfiguration;
        this.entryBehaviour = entryBehaviour;
        this.stateNumber = stateNumber;
        this.stateMachine = stateMachine;
        this.exitBehaviour = exitBehaviour;
        this.mmintermodel_transitions = mmintermodel_transitions;
        this.mmintermodel_transitions = mmintermodel_transitions;
    }

    public String getDuringbehaviour() {
        return duringBehaviour;
    }

    public void setDuringbehaviour(String duringBehaviour) {
        this.duringBehaviour = duringBehaviour;
    }
    public String getStateconfiguration() {
        return stateConfiguration;
    }

    public void setStateconfiguration(String stateConfiguration) {
        this.stateConfiguration = stateConfiguration;
    }
    public String getEntrybehaviour() {
        return entryBehaviour;
    }

    public void setEntrybehaviour(String entryBehaviour) {
        this.entryBehaviour = entryBehaviour;
    }
    public int getStatenumber() {
        return stateNumber;
    }

    public void setStatenumber(int stateNumber) {
        this.stateNumber = stateNumber;
    }
    public String getStatemachine() {
        return stateMachine;
    }

    public void setStatemachine(String stateMachine) {
        this.stateMachine = stateMachine;
    }
    public String getExitbehaviour() {
        return exitBehaviour;
    }

    public void setExitbehaviour(String exitBehaviour) {
        this.exitBehaviour = exitBehaviour;
    }

    public List<MMInterModel_Transition> getMmintermodel_transitions() {
        return mmintermodel_transitions;
    }

    public void addMmintermodel_transition(Mmintermodel_transition mmintermodel_transition) {
        this.mmintermodel_transitions.add(mmintermodel_transition);
    }
    public List<MMInterModel_Transition> getMmintermodel_transitions() {
        return mmintermodel_transitions;
    }

    public void addMmintermodel_transition(Mmintermodel_transition mmintermodel_transition) {
        this.mmintermodel_transitions.add(mmintermodel_transition);
    }
    public MMInterModel_Transition getMmintermodel_transition() {
        return mmintermodel_transition;
    }

    public void setMmintermodel_transition(MMInterModel_Transition mmintermodel_transition) {
        this.mmintermodel_transition = mmintermodel_transition;
    }
    public MMInterModel_Transition getMmintermodel_transition() {
        return mmintermodel_transition;
    }

    public void setMmintermodel_transition(MMInterModel_Transition mmintermodel_transition) {
        this.mmintermodel_transition = mmintermodel_transition;
    }

}