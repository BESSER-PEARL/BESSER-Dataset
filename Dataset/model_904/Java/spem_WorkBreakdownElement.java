





import java.util.List;
import java.util.ArrayList;

public class spem_WorkBreakdownElement extends BreakdownElement {

    private boolean isRepeatable;
    private boolean isOngoing;
    private boolean isEventDriven;



    public spem_WorkBreakdownElement(
        boolean isRepeatable,        boolean isOngoing,        boolean isEventDriven    ) {
        super(
        );
        this.isRepeatable = isRepeatable;
        this.isOngoing = isOngoing;
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
    public boolean getIseventdriven() {
        return isEventDriven;
    }

    public void setIseventdriven(boolean isEventDriven) {
        this.isEventDriven = isEventDriven;
    }


}