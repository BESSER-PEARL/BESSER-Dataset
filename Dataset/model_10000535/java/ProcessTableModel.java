





import java.util.List;
import java.util.ArrayList;

public class ProcessTableModel  {

    private String processList;
    private int numberProcesses;
    private String columnNames;



    public ProcessTableModel(
        String processList,        int numberProcesses,        String columnNames    ) {
        this.processList = processList;
        this.numberProcesses = numberProcesses;
        this.columnNames = columnNames;
    }


    public String getProcesslist() {
        return processList;
    }

    public void setProcesslist(String processList) {
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


}