





import java.util.List;
import java.util.ArrayList;

public class spem_WorkBreakdownElement extends BreakdownElement {

    private boolean isEventDriven;
    private boolean isRepeatable;
    private boolean isOngoing;



    public spem_WorkBreakdownElement(
        boolean isEventDriven,        boolean isRepeatable,        boolean isOngoing    ) {
        super(
        );
        this.isEventDriven = isEventDriven;
        this.isRepeatable = isRepeatable;
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
    public boolean getIsongoing() {
        return isOngoing;
    }

    public void setIsongoing(boolean isOngoing) {
        this.isOngoing = isOngoing;
    }


}