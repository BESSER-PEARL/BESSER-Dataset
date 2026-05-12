





import java.util.List;
import java.util.ArrayList;

public class Card  {






    private List<Machine> machines;


    public Card(
    ) {
        this.machines = new ArrayList<>();
    }

    public Card(
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