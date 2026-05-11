





import java.util.List;
import java.util.ArrayList;

public class z2fsm_AbstractState  {

    private String id;





    private z2fsm_Region z2fsm_region;


    public z2fsm_AbstractState(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public z2fsm_Region getZ2fsm_region() {
        return z2fsm_region;
    }

    public void setZ2fsm_region(z2fsm_Region z2fsm_region) {
        this.z2fsm_region = z2fsm_region;
    }

}