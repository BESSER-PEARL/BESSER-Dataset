





import java.util.List;
import java.util.ArrayList;

public class systemworkbench101_Thoughts extends NamedElement {






    private systemworkbench101_Workbench systemworkbench101_workbench;




    private List<systemworkbench101_Thing> systemworkbench101_things;


    public systemworkbench101_Thoughts(
    ) {
        super(
        );
        this.systemworkbench101_things = new ArrayList<>();
    }

    public systemworkbench101_Thoughts(
        ArrayList<systemworkbench101_Thing> systemworkbench101_things    ) {
        this.systemworkbench101_things = systemworkbench101_things;
    }


    public systemworkbench101_Workbench getSystemworkbench101_workbench() {
        return systemworkbench101_workbench;
    }

    public void setSystemworkbench101_workbench(systemworkbench101_Workbench systemworkbench101_workbench) {
        this.systemworkbench101_workbench = systemworkbench101_workbench;
    }
    public List<systemworkbench101_Thing> getSystemworkbench101_things() {
        return systemworkbench101_things;
    }

    public void addSystemworkbench101_thing(Systemworkbench101_thing systemworkbench101_thing) {
        this.systemworkbench101_things.add(systemworkbench101_thing);
    }

}