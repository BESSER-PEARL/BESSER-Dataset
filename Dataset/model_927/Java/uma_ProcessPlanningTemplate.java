





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessPlanningTemplate extends Process {






    private List<uma_Process> uma_processs;


    public uma_ProcessPlanningTemplate(
    ) {
        super(
        );
        this.uma_processs = new ArrayList<>();
    }

    public uma_ProcessPlanningTemplate(
        ArrayList<uma_Process> uma_processs    ) {
        this.uma_processs = uma_processs;
    }


    public List<uma_Process> getUma_processs() {
        return uma_processs;
    }

    public void addUma_process(Uma_process uma_process) {
        this.uma_processs.add(uma_process);
    }

}