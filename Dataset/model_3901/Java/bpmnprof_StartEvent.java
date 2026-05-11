





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_StartEvent extends CatchEvent {

    private String isInterrupting;



    public bpmnprof_StartEvent(
        String isInterrupting    ) {
        super(
        );
        this.isInterrupting = isInterrupting;
    }


    public String getIsinterrupting() {
        return isInterrupting;
    }

    public void setIsinterrupting(String isInterrupting) {
        this.isInterrupting = isInterrupting;
    }


}