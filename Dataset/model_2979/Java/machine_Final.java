





import java.util.List;
import java.util.ArrayList;

public class machine_Final  {

    private String name;





    private machine_State machine_state;




    private machine_Machine machine_machine;


    public machine_Final(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public machine_State getMachine_state() {
        return machine_state;
    }

    public void setMachine_state(machine_State machine_state) {
        this.machine_state = machine_state;
    }
    public machine_Machine getMachine_machine() {
        return machine_machine;
    }

    public void setMachine_machine(machine_Machine machine_machine) {
        this.machine_machine = machine_machine;
    }

}