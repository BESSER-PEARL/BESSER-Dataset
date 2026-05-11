





import java.util.List;
import java.util.ArrayList;

public class adb_FormalDerivedTypeDefinition extends FormalTypeDefinition {

    private String absract;
    private boolean limited;
    private boolean synchronized;





    private adb_Name adb_name;




    private adb_InterfaceList adb_interfacelist;


    public adb_FormalDerivedTypeDefinition(
        String absract,        boolean limited,        boolean synchronized    ) {
        super(
        );
        this.absract = absract;
        this.limited = limited;
        this.synchronized = synchronized;
    }


    public String getAbsract() {
        return absract;
    }

    public void setAbsract(String absract) {
        this.absract = absract;
    }
    public boolean getLimited() {
        return limited;
    }

    public void setLimited(boolean limited) {
        this.limited = limited;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }

    public adb_Name getAdb_name() {
        return adb_name;
    }

    public void setAdb_name(adb_Name adb_name) {
        this.adb_name = adb_name;
    }
    public adb_InterfaceList getAdb_interfacelist() {
        return adb_interfacelist;
    }

    public void setAdb_interfacelist(adb_InterfaceList adb_interfacelist) {
        this.adb_interfacelist = adb_interfacelist;
    }

}