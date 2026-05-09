





import java.util.List;
import java.util.ArrayList;

public class uma_WorkBreakdownElement extends BreakdownElement {

    private String isEventDriven;
    private String isOngoing;
    private String isRepeatable;



    public uma_WorkBreakdownElement(
        String isEventDriven,        String isOngoing,        String isRepeatable    ) {
        super(
        );
        this.isEventDriven = isEventDriven;
        this.isOngoing = isOngoing;
        this.isRepeatable = isRepeatable;
    }


    public String getIseventdriven() {
        return isEventDriven;
    }

    public void setIseventdriven(String isEventDriven) {
        this.isEventDriven = isEventDriven;
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


}