





import java.util.List;
import java.util.ArrayList;

public class ws_bundle_Bundle  {

    private String ID;





    private List<Process> processs;


    public ws_bundle_Bundle(
        String ID    ) {
        this.ID = ID;
        this.processs = new ArrayList<>();
    }

    public ws_bundle_Bundle(
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

}