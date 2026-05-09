





import java.util.List;
import java.util.ArrayList;

public class kfsm_Action  {

    private String id;





    private kfsm_State kfsm_state;


    public kfsm_Action(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public kfsm_State getKfsm_state() {
        return kfsm_state;
    }

    public void setKfsm_state(kfsm_State kfsm_state) {
        this.kfsm_state = kfsm_state;
    }

}