





import java.util.List;
import java.util.ArrayList;

public class Task_Manager  {

    private None numberOfProcesses;
    private None amountofFreeMemory;
    private None contactTable;
    private None scrollPane;
    private None amountofUsedMemory;



    public Task_Manager(
        None numberOfProcesses,        None amountofFreeMemory,        None contactTable,        None scrollPane,        None amountofUsedMemory    ) {
        this.numberOfProcesses = numberOfProcesses;
        this.amountofFreeMemory = amountofFreeMemory;
        this.contactTable = contactTable;
        this.scrollPane = scrollPane;
        this.amountofUsedMemory = amountofUsedMemory;
    }


    public None getNumberofprocesses() {
        return numberOfProcesses;
    }

    public void setNumberofprocesses(None numberOfProcesses) {
        this.numberOfProcesses = numberOfProcesses;
    }
    public None getAmountoffreememory() {
        return amountofFreeMemory;
    }

    public void setAmountoffreememory(None amountofFreeMemory) {
        this.amountofFreeMemory = amountofFreeMemory;
    }
    public None getContacttable() {
        return contactTable;
    }

    public void setContacttable(None contactTable) {
        this.contactTable = contactTable;
    }
    public None getScrollpane() {
        return scrollPane;
    }

    public void setScrollpane(None scrollPane) {
        this.scrollPane = scrollPane;
    }
    public None getAmountofusedmemory() {
        return amountofUsedMemory;
    }

    public void setAmountofusedmemory(None amountofUsedMemory) {
        this.amountofUsedMemory = amountofUsedMemory;
    }


}