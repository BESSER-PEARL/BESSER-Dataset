





import java.util.List;
import java.util.ArrayList;

public class y3fsm_AbstractState  {

    private String id;





    private y3fsm_Region y3fsm_region;


    public y3fsm_AbstractState(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public y3fsm_Region getY3fsm_region() {
        return y3fsm_region;
    }

    public void setY3fsm_region(y3fsm_Region y3fsm_region) {
        this.y3fsm_region = y3fsm_region;
    }

}