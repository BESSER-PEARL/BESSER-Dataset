





import java.util.List;
import java.util.ArrayList;

public class systemworkbench101_PatternCatalog  {

    private int id;





    private List<systemworkbench101_Function> systemworkbench101_functions;




    private systemworkbench101_Workbench systemworkbench101_workbench;


    public systemworkbench101_PatternCatalog(
        int id    ) {
        this.id = id;
        this.systemworkbench101_functions = new ArrayList<>();
    }

    public systemworkbench101_PatternCatalog(
        int id        ArrayList<systemworkbench101_Function> systemworkbench101_functions    ) {
        this.id = id;
        this.systemworkbench101_functions = systemworkbench101_functions;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<systemworkbench101_Function> getSystemworkbench101_functions() {
        return systemworkbench101_functions;
    }

    public void addSystemworkbench101_function(Systemworkbench101_function systemworkbench101_function) {
        this.systemworkbench101_functions.add(systemworkbench101_function);
    }
    public systemworkbench101_Workbench getSystemworkbench101_workbench() {
        return systemworkbench101_workbench;
    }

    public void setSystemworkbench101_workbench(systemworkbench101_Workbench systemworkbench101_workbench) {
        this.systemworkbench101_workbench = systemworkbench101_workbench;
    }

}