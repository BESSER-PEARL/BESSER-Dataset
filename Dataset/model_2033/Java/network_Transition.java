





import java.util.List;
import java.util.ArrayList;

public class network_Transition  {

    private String Event;





    private network_Statemachine network_statemachine;




    private network_Channel network_channel;




    private network_State network_state;




    private network_State network_state;


    public network_Transition(
        String Event    ) {
        this.Event = Event;
    }


    public String getEvent() {
        return Event;
    }

    public void setEvent(String Event) {
        this.Event = Event;
    }

    public network_Statemachine getNetwork_statemachine() {
        return network_statemachine;
    }

    public void setNetwork_statemachine(network_Statemachine network_statemachine) {
        this.network_statemachine = network_statemachine;
    }
    public network_Channel getNetwork_channel() {
        return network_channel;
    }

    public void setNetwork_channel(network_Channel network_channel) {
        this.network_channel = network_channel;
    }
    public network_State getNetwork_state() {
        return network_state;
    }

    public void setNetwork_state(network_State network_state) {
        this.network_state = network_state;
    }
    public network_State getNetwork_state() {
        return network_state;
    }

    public void setNetwork_state(network_State network_state) {
        this.network_state = network_state;
    }

}