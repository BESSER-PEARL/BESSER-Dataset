





import java.util.List;
import java.util.ArrayList;

public class rsgf_mw_Middleware  {






    private List<Process> processs;




    private VM vm;


    public rsgf_mw_Middleware(
    ) {
        this.processs = new ArrayList<>();
    }

    public rsgf_mw_Middleware(
        ArrayList<Process> processs    ) {
        this.processs = processs;
    }


    public List<Process> getProcesss() {
        return processs;
    }

    public void addProcess(Process process) {
        this.processs.add(process);
    }
    public VM getVm() {
        return vm;
    }

    public void setVm(VM vm) {
        this.vm = vm;
    }

}