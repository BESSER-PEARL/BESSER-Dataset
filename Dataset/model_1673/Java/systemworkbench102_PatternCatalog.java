





import java.util.List;
import java.util.ArrayList;

public class systemworkbench102_PatternCatalog  {

    private int id;





    private List<systemworkbench102_Function> systemworkbench102_functions;




    private systemworkbench102_Workbench systemworkbench102_workbench;


    public systemworkbench102_PatternCatalog(
        int id    ) {
        this.id = id;
        this.systemworkbench102_functions = new ArrayList<>();
    }

    public systemworkbench102_PatternCatalog(
        int id        ArrayList<systemworkbench102_Function> systemworkbench102_functions    ) {
        this.id = id;
        this.systemworkbench102_functions = systemworkbench102_functions;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<systemworkbench102_Function> getSystemworkbench102_functions() {
        return systemworkbench102_functions;
    }

    public void addSystemworkbench102_function(Systemworkbench102_function systemworkbench102_function) {
        this.systemworkbench102_functions.add(systemworkbench102_function);
    }
    public systemworkbench102_Workbench getSystemworkbench102_workbench() {
        return systemworkbench102_workbench;
    }

    public void setSystemworkbench102_workbench(systemworkbench102_Workbench systemworkbench102_workbench) {
        this.systemworkbench102_workbench = systemworkbench102_workbench;
    }

}