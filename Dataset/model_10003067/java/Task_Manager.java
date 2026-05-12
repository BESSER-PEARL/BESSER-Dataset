





import java.util.List;
import java.util.ArrayList;

public class Task_Manager  {

    private None amountofFreeMemory;
    private None scrollPane;
    private None numberOfProcesses;
    private None contactTable;
    private None amountofUsedMemory;





    private Process process;




    private Operating_System operating_system;


    public Task_Manager(
        None amountofFreeMemory,        None scrollPane,        None numberOfProcesses,        None contactTable,        None amountofUsedMemory    ) {
        this.amountofFreeMemory = amountofFreeMemory;
        this.scrollPane = scrollPane;
        this.numberOfProcesses = numberOfProcesses;
        this.contactTable = contactTable;
        this.amountofUsedMemory = amountofUsedMemory;
    }


    public None getAmountoffreememory() {
        return amountofFreeMemory;
    }

    public void setAmountoffreememory(None amountofFreeMemory) {
        this.amountofFreeMemory = amountofFreeMemory;
    }
    public None getScrollpane() {
        return scrollPane;
    }

    public void setScrollpane(None scrollPane) {
        this.scrollPane = scrollPane;
    }
    public None getNumberofprocesses() {
        return numberOfProcesses;
    }

    public void setNumberofprocesses(None numberOfProcesses) {
        this.numberOfProcesses = numberOfProcesses;
    }
    public None getContacttable() {
        return contactTable;
    }

    public void setContacttable(None contactTable) {
        this.contactTable = contactTable;
    }
    public None getAmountofusedmemory() {
        return amountofUsedMemory;
    }

    public void setAmountofusedmemory(None amountofUsedMemory) {
        this.amountofUsedMemory = amountofUsedMemory;
    }

    public Process getProcess() {
        return process;
    }

    public void setProcess(Process process) {
        this.process = process;
    }
    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}