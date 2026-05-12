





import java.util.List;
import java.util.ArrayList;

public class Machine  {






    private List<Processor> processors;




    private Machine machine;


    public Machine(
    ) {
        this.processors = new ArrayList<>();
    }

    public Machine(
        ArrayList<Processor> processors    ) {
        this.processors = processors;
    }


    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }
    public Machine getMachine() {
        return machine;
    }

    public void setMachine(Machine machine) {
        this.machine = machine;
    }

}