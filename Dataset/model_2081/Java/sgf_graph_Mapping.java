





import java.util.List;
import java.util.ArrayList;

public class sgf_graph_Mapping  {

    private String ID;





    private List<Process> processs;




    private Processor processor;


    public sgf_graph_Mapping(
        String ID    ) {
        this.ID = ID;
        this.processs = new ArrayList<>();
    }

    public sgf_graph_Mapping(
        String ID        ArrayList<Process> processs    ) {
        this.ID = ID;
        this.processs = processs;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<Process> getProcesss() {
        return processs;
    }

    public void addProcess(Process process) {
        this.processs.add(process);
    }
    public Processor getProcessor() {
        return processor;
    }

    public void setProcessor(Processor processor) {
        this.processor = processor;
    }

}