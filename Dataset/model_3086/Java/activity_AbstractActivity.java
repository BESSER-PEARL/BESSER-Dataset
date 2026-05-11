





import java.util.List;
import java.util.ArrayList;

public class activity_AbstractActivity extends AbstractBehavior, TraceableElement {

    private boolean isReadOnly;
    private boolean isSingleExecution;



    public activity_AbstractActivity(
        boolean isReadOnly,        boolean isSingleExecution    ) {
        super(
        );
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