





import java.util.List;
import java.util.ArrayList;

public class ProcessTableModel  {

    private int numberProcesses;
    private String columnNames;
    private String processList;





    private Operating_System operating_system;




    private Process process;


    public ProcessTableModel(
        int numberProcesses,        String columnNames,        String processList    ) {
        this.numberProcesses = numberProcesses;
        this.columnNames = columnNames;
        this.processList = processList;
    }


    public int getNumberprocesses() {
        return numberProcesses;
    }

    public void setNumberprocesses(int numberProcesses) {
        this.numberProcesses = numberProcesses;
    }
    public String getColumnnames() {
        return columnNames;
    }

    public void setColumnnames(String columnNames) {
        this.columnNames = columnNames;
    }
    public String getProcesslist() {
        return processList;
    }

    public void setProcesslist(String processList) {
        this.processList = processList;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }
    public Process getProcess() {
        return process;
    }

    public void setProcess(Process process) {
        this.process = process;
    }

}