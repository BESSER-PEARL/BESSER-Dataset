





import java.util.List;
import java.util.ArrayList;

public class wsn_Transition  {

    private String guard;





    private wsn_State wsn_state;




    private wsn_State wsn_state;




    private wsn_Event wsn_event;


    public wsn_Transition(
        String guard    ) {
        this.guard = guard;
    }


    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }

    public wsn_State getWsn_state() {
        return wsn_state;
    }

    public void setWsn_state(wsn_State wsn_state) {
        this.wsn_state = wsn_state;
    }
    public wsn_State getWsn_state() {
        return wsn_state;
    }

    public void setWsn_state(wsn_State wsn_state) {
        this.wsn_state = wsn_state;
    }
    public wsn_Event getWsn_event() {
        return wsn_event;
    }

    public void setWsn_event(wsn_Event wsn_event) {
        this.wsn_event = wsn_event;
    }

}