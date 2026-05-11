





import java.util.List;
import java.util.ArrayList;

public class adb_InterfaceTypeDefinition extends TypeDefinition, FormalTypeDefinition {

    private boolean protected;
    private boolean limited;
    private boolean task;
    private boolean synchro;





    private adb_InterfaceList adb_interfacelist;


    public adb_InterfaceTypeDefinition(
        boolean protected,        boolean limited,        boolean task,        boolean synchro    ) {
        super(
        );
        this.protected = protected;
        this.limited = limited;
        this.task = task;
        this.synchro = synchro;
    }


    public boolean getProtected() {
        return protected;
    }

    public void setProtected(boolean protected) {
        this.protected = protected;
    }
    public boolean getLimited() {
        return limited;
    }

    public void setLimited(boolean limited) {
        this.limited = limited;
    }
    public boolean getTask() {
        return task;
    }

    public void setTask(boolean task) {
        this.task = task;
    }
    public boolean getSynchro() {
        return synchro;
    }

    public void setSynchro(boolean synchro) {
        this.synchro = synchro;
    }

    public adb_InterfaceList getAdb_interfacelist() {
        return adb_interfacelist;
    }

    public void setAdb_interfacelist(adb_InterfaceList adb_interfacelist) {
        this.adb_interfacelist = adb_interfacelist;
    }

}