





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_AdultTicket extends Ticket {

    private boolean isElderlyDiscount;



    public CoachBusWithEDataType_AdultTicket(
        boolean isElderlyDiscount    ) {
        super(
        );
        this.isElderlyDiscount = isElderlyDiscount;
    }


    public boolean getIselderlydiscount() {
        return isElderlyDiscount;
    }

    public void setIselderlydiscount(boolean isElderlyDiscount) {
        this.isElderlyDiscount = isElderlyDiscount;
    }


}