





import java.util.List;
import java.util.ArrayList;

public class stm_Transition  {






    private stm_Event stm_event;




    private stm_Command stm_command;


    public stm_Transition(
    ) {
    }



    public stm_Event getStm_event() {
        return stm_event;
    }

    public void setStm_event(stm_Event stm_event) {
        this.stm_event = stm_event;
    }
    public stm_Command getStm_command() {
        return stm_command;
    }

    public void setStm_command(stm_Command stm_command) {
        this.stm_command = stm_command;
    }

}