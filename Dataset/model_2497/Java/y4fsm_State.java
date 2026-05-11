





import java.util.List;
import java.util.ArrayList;

public class y4fsm_State  {

    private String id;





    private y4fsm_Region y4fsm_region;


    public y4fsm_State(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public y4fsm_Region getY4fsm_region() {
        return y4fsm_region;
    }

    public void setY4fsm_region(y4fsm_Region y4fsm_region) {
        this.y4fsm_region = y4fsm_region;
    }

}