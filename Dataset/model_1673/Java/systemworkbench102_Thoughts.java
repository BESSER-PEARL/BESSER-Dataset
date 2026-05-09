





import java.util.List;
import java.util.ArrayList;

public class systemworkbench102_Thoughts extends NamedElement {






    private List<systemworkbench102_Thing> systemworkbench102_things;




    private systemworkbench102_Workbench systemworkbench102_workbench;


    public systemworkbench102_Thoughts(
    ) {
        super(
        );
        this.systemworkbench102_things = new ArrayList<>();
    }

    public systemworkbench102_Thoughts(
        ArrayList<systemworkbench102_Thing> systemworkbench102_things    ) {
        this.systemworkbench102_things = systemworkbench102_things;
    }


    public List<systemworkbench102_Thing> getSystemworkbench102_things() {
        return systemworkbench102_things;
    }

    public void addSystemworkbench102_thing(Systemworkbench102_thing systemworkbench102_thing) {
        this.systemworkbench102_things.add(systemworkbench102_thing);
    }
    public systemworkbench102_Workbench getSystemworkbench102_workbench() {
        return systemworkbench102_workbench;
    }

    public void setSystemworkbench102_workbench(systemworkbench102_Workbench systemworkbench102_workbench) {
        this.systemworkbench102_workbench = systemworkbench102_workbench;
    }

}