





import java.util.List;
import java.util.ArrayList;

public class internalsm_StateMachine  {

    private int priority;
    private String context;



    public internalsm_StateMachine(
        int priority,        String context    ) {
        this.priority = priority;
        this.context = context;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }


}