





import java.util.List;
import java.util.ArrayList;

public class z5fsm_AbstractState  {

    private String id;





    private z5fsm_AbstractState z5fsm_abstractstate;




    private z5fsm_Region z5fsm_region;


    public z5fsm_AbstractState(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public z5fsm_AbstractState getZ5fsm_abstractstate() {
        return z5fsm_abstractstate;
    }

    public void setZ5fsm_abstractstate(z5fsm_AbstractState z5fsm_abstractstate) {
        this.z5fsm_abstractstate = z5fsm_abstractstate;
    }
    public z5fsm_Region getZ5fsm_region() {
        return z5fsm_region;
    }

    public void setZ5fsm_region(z5fsm_Region z5fsm_region) {
        this.z5fsm_region = z5fsm_region;
    }

}