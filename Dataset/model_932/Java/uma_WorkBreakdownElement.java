





import java.util.List;
import java.util.ArrayList;

public class uma_WorkBreakdownElement extends BreakdownElement {

    private String isOngoing;
    private String isRepeatable;
    private String isEventDriven;





    private uma_WorkOrder uma_workorder;




    private List<uma_WorkOrder> uma_workorders;


    public uma_WorkBreakdownElement(
        String isOngoing,        String isRepeatable,        String isEventDriven    ) {
        super(
        );
        this.isOngoing = isOngoing;
        this.isRepeatable = isRepeatable;
        this.isEventDriven = isEventDriven;
        this.uma_workorders = new ArrayList<>();
    }

    public uma_WorkBreakdownElement(
        String isOngoing,        String isRepeatable,        String isEventDriven        ArrayList<uma_WorkOrder> uma_workorders    ) {
        this.isOngoing = isOngoing;
        this.isRepeatable = isRepeatable;
        this.isEventDriven = isEventDriven;
        this.uma_workorders = uma_workorders;
    }

    public String getIsongoing() {
        return isOngoing;
    }

    public void setIsongoing(String isOngoing) {
        this.isOngoing = isOngoing;
    }
    public String getIsrepeatable() {
        return isRepeatable;
    }

    public void setIsrepeatable(String isRepeatable) {
        this.isRepeatable = isRepeatable;
    }
    public String getIseventdriven() {
        return isEventDriven;
    }

    public void setIseventdriven(String isEventDriven) {
        this.isEventDriven = isEventDriven;
    }

    public uma_WorkOrder getUma_workorder() {
        return uma_workorder;
    }

    public void setUma_workorder(uma_WorkOrder uma_workorder) {
        this.uma_workorder = uma_workorder;
    }
    public List<uma_WorkOrder> getUma_workorders() {
        return uma_workorders;
    }

    public void addUma_workorder(Uma_workorder uma_workorder) {
        this.uma_workorders.add(uma_workorder);
    }

}