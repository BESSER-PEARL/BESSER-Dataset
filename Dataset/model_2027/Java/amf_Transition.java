





import java.util.List;
import java.util.ArrayList;

public class amf_Transition  {

    private String event;





    private amf_State amf_state;




    private amf_Statemachine amf_statemachine;




    private amf_Channel amf_channel;




    private amf_State amf_state;


    public amf_Transition(
        String event    ) {
        this.event = event;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public amf_State getAmf_state() {
        return amf_state;
    }

    public void setAmf_state(amf_State amf_state) {
        this.amf_state = amf_state;
    }
    public amf_Statemachine getAmf_statemachine() {
        return amf_statemachine;
    }

    public void setAmf_statemachine(amf_Statemachine amf_statemachine) {
        this.amf_statemachine = amf_statemachine;
    }
    public amf_Channel getAmf_channel() {
        return amf_channel;
    }

    public void setAmf_channel(amf_Channel amf_channel) {
        this.amf_channel = amf_channel;
    }
    public amf_State getAmf_state() {
        return amf_state;
    }

    public void setAmf_state(amf_State amf_state) {
        this.amf_state = amf_state;
    }

}