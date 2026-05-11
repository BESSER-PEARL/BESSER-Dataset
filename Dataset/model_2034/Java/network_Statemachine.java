





import java.util.List;
import java.util.ArrayList;

public class network_Statemachine extends AbstractElement {






    private network_State network_state;




    private List<network_Transition> network_transitions;




    private List<network_State> network_states;




    private network_Network network_network;


    public network_Statemachine(
    ) {
        super(
        );
        this.network_transitions = new ArrayList<>();
        this.network_states = new ArrayList<>();
    }

    public network_Statemachine(
        ArrayList<network_Transition> network_transitions,        ArrayList<network_State> network_states    ) {
        this.network_transitions = network_transitions;
        this.network_states = network_states;
    }


    public network_State getNetwork_state() {
        return network_state;
    }

    public void setNetwork_state(network_State network_state) {
        this.network_state = network_state;
    }
    public List<network_Transition> getNetwork_transitions() {
        return network_transitions;
    }

    public void addNetwork_transition(Network_transition network_transition) {
        this.network_transitions.add(network_transition);
    }
    public List<network_State> getNetwork_states() {
        return network_states;
    }

    public void addNetwork_state(Network_state network_state) {
        this.network_states.add(network_state);
    }
    public network_Network getNetwork_network() {
        return network_network;
    }

    public void setNetwork_network(network_Network network_network) {
        this.network_network = network_network;
    }

}