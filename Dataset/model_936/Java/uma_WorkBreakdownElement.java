





import java.util.List;
import java.util.ArrayList;

public class uma_WorkBreakdownElement extends BreakdownElement {

    private String isOngoing;
    private String isEventDriven;
    private String isRepeatable;
    private String group2;



    public uma_WorkBreakdownElement(
        String isOngoing,        String isEventDriven,        String isRepeatable,        String group2    ) {
        super(
        );
        this.isOngoing = isOngoing;
        this.isEventDriven = isEventDriven;
        this.isRepeatable = isRepeatable;
        this.group2 = group2;
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
    public String getIsrepeatable() {
        return isRepeatable;
    }

    public void setIsrepeatable(String isRepeatable) {
        this.isRepeatable = isRepeatable;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }


}