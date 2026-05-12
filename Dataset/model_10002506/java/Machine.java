





import java.util.List;
import java.util.ArrayList;

public class Machine  {






    private List<Processor> processors;




    private Processor processor;




    private Processor processor;


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
    public Processor getProcessor() {
        return processor;
    }

    public void setProcessor(Processor processor) {
        this.processor = processor;
    }
    public Processor getProcessor() {
        return processor;
    }

    public void setProcessor(Processor processor) {
        this.processor = processor;
    }

}