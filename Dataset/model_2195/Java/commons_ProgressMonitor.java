





import java.util.List;
import java.util.ArrayList;

public class commons_ProgressMonitor  {

    private String taskName;
    private boolean canceled;



    public commons_ProgressMonitor(
        String taskName,        boolean canceled    ) {
        this.taskName = taskName;
        this.canceled = canceled;
    }


    public String getTaskname() {
        return taskName;
    }

    public void setTaskname(String taskName) {
        this.taskName = taskName;
    }
    public boolean getCanceled() {
        return canceled;
    }

    public void setCanceled(boolean canceled) {
        this.canceled = canceled;
    }


}