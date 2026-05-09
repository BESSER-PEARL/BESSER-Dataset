





import java.util.List;
import java.util.ArrayList;

public class mydsl_Transition  {

    private String name;





    private mydsl_FSM mydsl_fsm;




    private mydsl_State mydsl_state;




    private mydsl_State mydsl_state;


    public mydsl_Transition(
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
    public mydsl_State getMydsl_state() {
        return mydsl_state;
    }

    public void setMydsl_state(mydsl_State mydsl_state) {
        this.mydsl_state = mydsl_state;
    }
    public mydsl_State getMydsl_state() {
        return mydsl_state;
    }

    public void setMydsl_state(mydsl_State mydsl_state) {
        this.mydsl_state = mydsl_state;
    }

}