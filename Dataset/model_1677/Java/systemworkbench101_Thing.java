





import java.util.List;
import java.util.ArrayList;

public class systemworkbench101_Thing extends NamedElement {

    private int id;





    private systemworkbench101_Workbench systemworkbench101_workbench;


    public systemworkbench101_Thing(
        int id    ) {
        super(
        );
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public systemworkbench101_Workbench getSystemworkbench101_workbench() {
        return systemworkbench101_workbench;
    }

    public void setSystemworkbench101_workbench(systemworkbench101_Workbench systemworkbench101_workbench) {
        this.systemworkbench101_workbench = systemworkbench101_workbench;
    }

}