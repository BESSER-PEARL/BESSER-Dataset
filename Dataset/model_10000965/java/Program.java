





import java.util.List;
import java.util.ArrayList;

public class Program  {

    private String name;





    private List<Processor> processors;


    public Program(
        String name    ) {
        this.name = name;
        this.processors = new ArrayList<>();
    }

    public Program(
        String name        ArrayList<Processor> processors    ) {
        this.name = name;
        this.processors = processors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }

}