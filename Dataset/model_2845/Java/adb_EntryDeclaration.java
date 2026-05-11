





import java.util.List;
import java.util.ArrayList;

public class adb_EntryDeclaration extends TaskItem, ProtectedOperationDeclaration {

    private String name;





    private adb_EntryBody adb_entrybody;




    private adb_OverridingIndicator adb_overridingindicator;


    public adb_EntryDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adb_EntryBody getAdb_entrybody() {
        return adb_entrybody;
    }

    public void setAdb_entrybody(adb_EntryBody adb_entrybody) {
        this.adb_entrybody = adb_entrybody;
    }
    public adb_OverridingIndicator getAdb_overridingindicator() {
        return adb_overridingindicator;
    }

    public void setAdb_overridingindicator(adb_OverridingIndicator adb_overridingindicator) {
        this.adb_overridingindicator = adb_overridingindicator;
    }

}