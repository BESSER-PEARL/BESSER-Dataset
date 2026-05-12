





import java.util.List;
import java.util.ArrayList;

public class Memory_Interface  {






    private List<Machine> machines;




    private List<Processor> processors;


    public Memory_Interface(
    ) {
        this.machines = new ArrayList<>();
        this.processors = new ArrayList<>();
    }

    public Memory_Interface(
        ArrayList<Machine> machines,        ArrayList<Processor> processors    ) {
        this.machines = machines;
        this.processors = processors;
    }


    public List<Machine> getMachines() {
        return machines;
    }

    public void addMachine(Machine machine) {
        this.machines.add(machine);
    }
    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }

}