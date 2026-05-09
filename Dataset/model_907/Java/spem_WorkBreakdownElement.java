





import java.util.List;
import java.util.ArrayList;

public class spem_WorkBreakdownElement extends BreakdownElement {

    private boolean isOngoing;
    private boolean isEventDriven;
    private boolean isRepeatable;



    public spem_WorkBreakdownElement(
        boolean isOngoing,        boolean isEventDriven,        boolean isRepeatable    ) {
        super(
        );
        this.isOngoing = isOngoing;
        this.isEventDriven = isEventDriven;
        this.isRepeatable = isRepeatable;
    }


    public boolean getIsongoing() {
        return isOngoing;
    }

    public void setIsongoing(boolean isOngoing) {
        this.isOngoing = isOngoing;
    }
    public boolean getIseventdriven() {
        return isEventDriven;
    }

    public void setIseventdriven(boolean isEventDriven) {
        this.isEventDriven = isEventDriven;
    }
    public boolean getIsrepeatable() {
        return isRepeatable;
    }

    public void setIsrepeatable(boolean isRepeatable) {
        this.isRepeatable = isRepeatable;
    }


}