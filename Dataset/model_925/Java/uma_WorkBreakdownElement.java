





import java.util.List;
import java.util.ArrayList;

public class uma_WorkBreakdownElement extends BreakdownElement {

    private String isRepeatable;
    private String isEventDriven;
    private String isOngoing;



    public uma_WorkBreakdownElement(
        String isRepeatable,        String isEventDriven,        String isOngoing    ) {
        super(
        );
        this.isRepeatable = isRepeatable;
        this.isEventDriven = isEventDriven;
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
    public String getIsongoing() {
        return isOngoing;
    }

    public void setIsongoing(String isOngoing) {
        this.isOngoing = isOngoing;
    }


}