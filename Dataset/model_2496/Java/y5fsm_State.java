





import java.util.List;
import java.util.ArrayList;

public class y5fsm_State  {

    private String id;





    private y5fsm_Region y5fsm_region;


    public y5fsm_State(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public y5fsm_Region getY5fsm_region() {
        return y5fsm_region;
    }

    public void setY5fsm_region(y5fsm_Region y5fsm_region) {
        this.y5fsm_region = y5fsm_region;
    }

}