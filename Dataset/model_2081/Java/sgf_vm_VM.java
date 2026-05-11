





import java.util.List;
import java.util.ArrayList;

public class sgf_vm_VM  {

    private String ID;
    private String protocol;





    private List<Processor> processors;


    public sgf_vm_VM(
        String ID,        String protocol    ) {
        this.ID = ID;
        this.protocol = protocol;
        this.processors = new ArrayList<>();
    }

    public sgf_vm_VM(
        String ID,        String protocol        ArrayList<Processor> processors    ) {
        this.ID = ID;
        this.protocol = protocol;
        this.processors = processors;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }

    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }

}