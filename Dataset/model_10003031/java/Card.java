





import java.util.List;
import java.util.ArrayList;

public class Card  {






    private List<ExtensionBoard> extensionboards;




    private List<Machine> machines;


    public Card(
    ) {
        this.extensionboards = new ArrayList<>();
        this.machines = new ArrayList<>();
    }

    public Card(
        ArrayList<ExtensionBoard> extensionboards,        ArrayList<Machine> machines    ) {
        this.extensionboards = extensionboards;
        this.machines = machines;
    }


    public List<ExtensionBoard> getExtensionboards() {
        return extensionboards;
    }

    public void addExtensionboard(Extensionboard extensionboard) {
        this.extensionboards.add(extensionboard);
    }
    public List<Machine> getMachines() {
        return machines;
    }

    public void addMachine(Machine machine) {
        this.machines.add(machine);
    }

}