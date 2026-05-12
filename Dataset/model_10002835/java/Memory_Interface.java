





import java.util.List;
import java.util.ArrayList;

public class Memory_Interface  {






    private List<Processor> processors;




    private List<Machine> machines;


    public Memory_Interface(
    ) {
        this.processors = new ArrayList<>();
        this.machines = new ArrayList<>();
    }

    public Memory_Interface(
        ArrayList<Processor> processors,        ArrayList<Machine> machines    ) {
        this.processors = processors;
        this.machines = machines;
    }


    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }
    public List<Machine> getMachines() {
        return machines;
    }

    public void addMachine(Machine machine) {
        this.machines.add(machine);
    }

}