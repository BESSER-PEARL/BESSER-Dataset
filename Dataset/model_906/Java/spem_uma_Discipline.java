





import java.util.List;
import java.util.ArrayList;

public class spem_uma_Discipline extends Category {






    private List<Process> processs;


    public spem_uma_Discipline(
    ) {
        super(
        );
        this.processs = new ArrayList<>();
    }

    public spem_uma_Discipline(
        ArrayList<Process> processs    ) {
        this.processs = processs;
    }


    public List<Process> getProcesss() {
        return processs;
    }

    public void addProcess(Process process) {
        this.processs.add(process);
    }

}