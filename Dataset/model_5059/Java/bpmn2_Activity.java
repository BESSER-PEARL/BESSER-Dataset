





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Activity extends FlowNode {

    private boolean isForCompensation;
    private int startQuantity;
    private int completionQuantity;



    public bpmn2_Activity(
        boolean isForCompensation,        int startQuantity,        int completionQuantity    ) {
        super(
        );
        this.isForCompensation = isForCompensation;
        this.startQuantity = startQuantity;
        this.completionQuantity = completionQuantity;
    }


    public boolean getIsforcompensation() {
        return isForCompensation;
    }

    public void setIsforcompensation(boolean isForCompensation) {
        this.isForCompensation = isForCompensation;
    }
    public int getStartquantity() {
        return startQuantity;
    }

    public void setStartquantity(int startQuantity) {
        this.startQuantity = startQuantity;
    }
    public int getCompletionquantity() {
        return completionQuantity;
    }

    public void setCompletionquantity(int completionQuantity) {
        this.completionQuantity = completionQuantity;
    }


}