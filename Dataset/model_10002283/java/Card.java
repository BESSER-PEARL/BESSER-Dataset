





import java.util.List;
import java.util.ArrayList;

public class Card  {






    private List<Machine> machines;




    private List<ExtensionBoard> extensionboards;


    public Card(
    ) {
        this.machines = new ArrayList<>();
        this.extensionboards = new ArrayList<>();
    }

    public Card(
        ArrayList<Machine> machines,        ArrayList<ExtensionBoard> extensionboards    ) {
        this.machines = machines;
        this.extensionboards = extensionboards;
    }


    public List<Machine> getMachines() {
        return machines;
    }

    public void addMachine(Machine machine) {
        this.machines.add(machine);
    }
    public List<ExtensionBoard> getExtensionboards() {
        return extensionboards;
    }

    public void addExtensionboard(Extensionboard extensionboard) {
        this.extensionboards.add(extensionboard);
    }

}