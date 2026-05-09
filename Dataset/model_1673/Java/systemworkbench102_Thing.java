





import java.util.List;
import java.util.ArrayList;

public class systemworkbench102_Thing extends NamedElement {

    private int id;





    private systemworkbench102_Workbench systemworkbench102_workbench;


    public systemworkbench102_Thing(
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

    public systemworkbench102_Workbench getSystemworkbench102_workbench() {
        return systemworkbench102_workbench;
    }

    public void setSystemworkbench102_workbench(systemworkbench102_Workbench systemworkbench102_workbench) {
        this.systemworkbench102_workbench = systemworkbench102_workbench;
    }

}