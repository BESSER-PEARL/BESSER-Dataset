





import java.util.List;
import java.util.ArrayList;

public class ActivitiesProv_Activity  {

    private boolean isSingleExecution;
    private boolean isReadOnly;



    public ActivitiesProv_Activity(
        boolean isSingleExecution,        boolean isReadOnly    ) {
        this.isSingleExecution = isSingleExecution;
        this.isReadOnly = isReadOnly;
    }


    public boolean getIssingleexecution() {
        return isSingleExecution;
    }

    public void setIssingleexecution(boolean isSingleExecution) {
        this.isSingleExecution = isSingleExecution;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }


}