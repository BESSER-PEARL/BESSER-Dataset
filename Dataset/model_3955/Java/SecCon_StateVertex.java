





import java.util.List;
import java.util.ArrayList;

public class SecCon_StateVertex extends NamedElement {






    private List<SecCon_Transition> seccon_transitions;




    private SecCon_StateMachineScenario seccon_statemachinescenario;




    private List<SecCon_Transition> seccon_transitions;


    public SecCon_StateVertex(
    ) {
        super(
        );
        this.seccon_transitions = new ArrayList<>();
        this.seccon_transitions = new ArrayList<>();
    }

    public SecCon_StateVertex(
        ArrayList<SecCon_Transition> seccon_transitions,        ArrayList<SecCon_Transition> seccon_transitions    ) {
        this.seccon_transitions = seccon_transitions;
        this.seccon_transitions = seccon_transitions;
    }


    public List<SecCon_Transition> getSeccon_transitions() {
        return seccon_transitions;
    }

    public void addSeccon_transition(Seccon_transition seccon_transition) {
        this.seccon_transitions.add(seccon_transition);
    }
    public SecCon_StateMachineScenario getSeccon_statemachinescenario() {
        return seccon_statemachinescenario;
    }

    public void setSeccon_statemachinescenario(SecCon_StateMachineScenario seccon_statemachinescenario) {
        this.seccon_statemachinescenario = seccon_statemachinescenario;
    }
    public List<SecCon_Transition> getSeccon_transitions() {
        return seccon_transitions;
    }

    public void addSeccon_transition(Seccon_transition seccon_transition) {
        this.seccon_transitions.add(seccon_transition);
    }

}