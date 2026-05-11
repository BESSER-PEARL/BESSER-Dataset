





import java.util.List;
import java.util.ArrayList;

public class synccharts_Transition extends Action {

    private boolean isHistory;
    private int priority;
    private String type;



    public synccharts_Transition(
        boolean isHistory,        int priority,        String type    ) {
        super(
        );
        this.isHistory = isHistory;
        this.priority = priority;
        this.type = type;
    }


    public boolean getIshistory() {
        return isHistory;
    }

    public void setIshistory(boolean isHistory) {
        this.isHistory = isHistory;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}