





import java.util.List;
import java.util.ArrayList;

public class machine_Head  {

    private String name;





    private machine_Machine machine_machine;


    public machine_Head(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public machine_Machine getMachine_machine() {
        return machine_machine;
    }

    public void setMachine_machine(machine_Machine machine_machine) {
        this.machine_machine = machine_machine;
    }

}