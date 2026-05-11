





import java.util.List;
import java.util.ArrayList;

public class adb_TaskDefinition  {






    private List<adb_TaskItem> adb_taskitems;




    private adb_TaskDeclaration adb_taskdeclaration;


    public adb_TaskDefinition(
    ) {
        this.adb_taskitems = new ArrayList<>();
    }

    public adb_TaskDefinition(
        ArrayList<adb_TaskItem> adb_taskitems    ) {
        this.adb_taskitems = adb_taskitems;
    }


    public List<adb_TaskItem> getAdb_taskitems() {
        return adb_taskitems;
    }

    public void addAdb_taskitem(Adb_taskitem adb_taskitem) {
        this.adb_taskitems.add(adb_taskitem);
    }
    public adb_TaskDeclaration getAdb_taskdeclaration() {
        return adb_taskdeclaration;
    }

    public void setAdb_taskdeclaration(adb_TaskDeclaration adb_taskdeclaration) {
        this.adb_taskdeclaration = adb_taskdeclaration;
    }

}