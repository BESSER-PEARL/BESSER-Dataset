





import java.util.List;
import java.util.ArrayList;

public class adb_TaskNames extends AbortStatement {






    private List<adb_Name> adb_names;


    public adb_TaskNames(
    ) {
        super(
        );
        this.adb_names = new ArrayList<>();
    }

    public adb_TaskNames(
        ArrayList<adb_Name> adb_names    ) {
        this.adb_names = adb_names;
    }


    public List<adb_Name> getAdb_names() {
        return adb_names;
    }

    public void addAdb_name(Adb_name adb_name) {
        this.adb_names.add(adb_name);
    }

}