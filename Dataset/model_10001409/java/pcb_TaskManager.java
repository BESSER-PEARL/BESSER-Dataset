





import java.util.List;
import java.util.ArrayList;

public class pcb_TaskManager  {

    private None processes;





    private List<pcb_PCB> pcb_pcbs;


    public pcb_TaskManager(
        None processes    ) {
        this.processes = processes;
        this.pcb_pcbs = new ArrayList<>();
    }

    public pcb_TaskManager(
        None processes        ArrayList<pcb_PCB> pcb_pcbs    ) {
        this.processes = processes;
        this.pcb_pcbs = pcb_pcbs;
    }

    public None getProcesses() {
        return processes;
    }

    public void setProcesses(None processes) {
        this.processes = processes;
    }

    public List<pcb_PCB> getPcb_pcbs() {
        return pcb_pcbs;
    }

    public void addPcb_pcb(Pcb_pcb pcb_pcb) {
        this.pcb_pcbs.add(pcb_pcb);
    }

}