





import java.util.List;
import java.util.ArrayList;

public class minifsm_State  {

    private String name;





    private minifsm_Machine minifsm_machine;


    public minifsm_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public minifsm_Machine getMinifsm_machine() {
        return minifsm_machine;
    }

    public void setMinifsm_machine(minifsm_Machine minifsm_machine) {
        this.minifsm_machine = minifsm_machine;
    }

}