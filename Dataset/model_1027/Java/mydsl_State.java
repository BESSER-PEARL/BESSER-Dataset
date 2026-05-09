





import java.util.List;
import java.util.ArrayList;

public class mydsl_State  {

    private String name;





    private mydsl_FSM mydsl_fsm;


    public mydsl_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mydsl_FSM getMydsl_fsm() {
        return mydsl_fsm;
    }

    public void setMydsl_fsm(mydsl_FSM mydsl_fsm) {
        this.mydsl_fsm = mydsl_fsm;
    }

}