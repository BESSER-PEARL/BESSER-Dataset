





import java.util.List;
import java.util.ArrayList;

public class workflow_IWorkflowNode extends IWorkflowElement {

    private boolean isStart;
    private boolean isFinish;



    public workflow_IWorkflowNode(
        boolean isStart,        boolean isFinish    ) {
        super(
        );
        this.isStart = isStart;
        this.isFinish = isFinish;
    }


    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }
    public boolean getIsfinish() {
        return isFinish;
    }

    public void setIsfinish(boolean isFinish) {
        this.isFinish = isFinish;
    }


}