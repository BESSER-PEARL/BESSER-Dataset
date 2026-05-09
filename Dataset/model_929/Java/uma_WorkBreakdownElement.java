





import java.util.List;
import java.util.ArrayList;

public class uma_WorkBreakdownElement extends BreakdownElement {

    private String isRepeatable;
    private String isOngoing;
    private String isEventDriven;



    public uma_WorkBreakdownElement(
        String isRepeatable,        String isOngoing,        String isEventDriven    ) {
        super(
        );
        this.isRepeatable = isRepeatable;
        this.isOngoing = isOngoing;
        this.isEventDriven = isEventDriven;
    }


    public String getIsrepeatable() {
        return isRepeatable;
    }

    public void setIsrepeatable(String isRepeatable) {
        this.isRepeatable = isRepeatable;
    }
    public String getIsongoing() {
        return isOngoing;
    }

    public void setIsongoing(String isOngoing) {
        this.isOngoing = isOngoing;
    }
    public String getIseventdriven() {
        return isEventDriven;
    }

    public void setIseventdriven(String isEventDriven) {
        this.isEventDriven = isEventDriven;
    }


}