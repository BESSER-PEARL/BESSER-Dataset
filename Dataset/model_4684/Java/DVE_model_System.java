





import java.util.List;
import java.util.ArrayList;

public class DVE_model_System extends CompositeDeclaration {






    private List<Process> processs;




    private SystemProperties systemproperties;


    public DVE_model_System(
    ) {
        super(
        );
        this.processs = new ArrayList<>();
    }

    public DVE_model_System(
        ArrayList<Process> processs    ) {
        this.processs = processs;
    }


    public List<Process> getProcesss() {
        return processs;
    }

    public void addProcess(Process process) {
        this.processs.add(process);
    }
    public SystemProperties getSystemproperties() {
        return systemproperties;
    }

    public void setSystemproperties(SystemProperties systemproperties) {
        this.systemproperties = systemproperties;
    }

}