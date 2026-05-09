





import java.util.List;
import java.util.ArrayList;

public class uma_WorkBreakdownElement extends BreakdownElement {

    private String group2;
    private String isOngoing;
    private String isRepeatable;
    private String isEventDriven;



    public uma_WorkBreakdownElement(
        String group2,        String isOngoing,        String isRepeatable,        String isEventDriven    ) {
        super(
        );
        this.group2 = group2;
        this.isOngoing = isOngoing;
        this.isRepeatable = isRepeatable;
        this.isEventDriven = isEventDriven;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
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


}