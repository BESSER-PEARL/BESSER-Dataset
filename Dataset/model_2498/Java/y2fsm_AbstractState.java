





import java.util.List;
import java.util.ArrayList;

public class y2fsm_AbstractState  {

    private String id;





    private y2fsm_Region y2fsm_region;


    public y2fsm_AbstractState(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public y2fsm_Region getY2fsm_region() {
        return y2fsm_region;
    }

    public void setY2fsm_region(y2fsm_Region y2fsm_region) {
        this.y2fsm_region = y2fsm_region;
    }

}