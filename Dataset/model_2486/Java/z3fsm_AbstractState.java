





import java.util.List;
import java.util.ArrayList;

public class z3fsm_AbstractState  {

    private String id;





    private z3fsm_Region z3fsm_region;


    public z3fsm_AbstractState(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public z3fsm_Region getZ3fsm_region() {
        return z3fsm_region;
    }

    public void setZ3fsm_region(z3fsm_Region z3fsm_region) {
        this.z3fsm_region = z3fsm_region;
    }

}