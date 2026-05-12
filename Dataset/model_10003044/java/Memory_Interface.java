





import java.util.List;
import java.util.ArrayList;

public class Memory_Interface  {






    private List<Machine> machines;


    public Memory_Interface(
    ) {
        this.machines = new ArrayList<>();
    }

    public Memory_Interface(
        ArrayList<Machine> machines    ) {
        this.machines = machines;
    }


    public List<Machine> getMachines() {
        return machines;
    }

    public void addMachine(Machine machine) {
        this.machines.add(machine);
    }

}