





import java.util.List;
import java.util.ArrayList;

public class workbench101_Thing extends NamedElement {

    private int id;





    private workbench101_Thoughts workbench101_thoughts;




    private workbench101_Workbench workbench101_workbench;


    public workbench101_Thing(
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

    public workbench101_Thoughts getWorkbench101_thoughts() {
        return workbench101_thoughts;
    }

    public void setWorkbench101_thoughts(workbench101_Thoughts workbench101_thoughts) {
        this.workbench101_thoughts = workbench101_thoughts;
    }
    public workbench101_Workbench getWorkbench101_workbench() {
        return workbench101_workbench;
    }

    public void setWorkbench101_workbench(workbench101_Workbench workbench101_workbench) {
        this.workbench101_workbench = workbench101_workbench;
    }

}