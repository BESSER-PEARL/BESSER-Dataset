





import java.util.List;
import java.util.ArrayList;

public class umlknes_Activity  {

    private boolean isReadOnly;
    private boolean isSingleExecution;



    public umlknes_Activity(
        boolean isReadOnly,        boolean isSingleExecution    ) {
        this.isReadOnly = isReadOnly;
        this.isSingleExecution = isSingleExecution;
    }


    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public boolean getIssingleexecution() {
        return isSingleExecution;
    }

    public void setIssingleexecution(boolean isSingleExecution) {
        this.isSingleExecution = isSingleExecution;
    }


}