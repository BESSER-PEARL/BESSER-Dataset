





import java.util.List;
import java.util.ArrayList;

public class network_Channel extends AbstractElement {

    private String Type;





    private network_Network network_network;




    private network_Transition network_transition;


    public network_Channel(
        String Type    ) {
        super(
        );
        this.Type = Type;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public network_Network getNetwork_network() {
        return network_network;
    }

    public void setNetwork_network(network_Network network_network) {
        this.network_network = network_network;
    }
    public network_Transition getNetwork_transition() {
        return network_transition;
    }

    public void setNetwork_transition(network_Transition network_transition) {
        this.network_transition = network_transition;
    }

}