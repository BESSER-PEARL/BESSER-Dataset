





import java.util.List;
import java.util.ArrayList;

public class Machine  {

    private String attribute2;
    private String attribute;





    private List<Processor> processors;


    public Machine(
        String attribute2,        String attribute    ) {
        this.attribute2 = attribute2;
        this.attribute = attribute;
        this.processors = new ArrayList<>();
    }

    public Machine(
        String attribute2,        String attribute        ArrayList<Processor> processors    ) {
        this.attribute2 = attribute2;
        this.attribute = attribute;
        this.processors = processors;
    }

    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }

}