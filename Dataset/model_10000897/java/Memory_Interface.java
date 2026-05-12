





import java.util.List;
import java.util.ArrayList;

public class Memory_Interface  {






    private List<Processor> processors;


    public Memory_Interface(
    ) {
        this.processors = new ArrayList<>();
    }

    public Memory_Interface(
        ArrayList<Processor> processors    ) {
        this.processors = processors;
    }


    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }

}