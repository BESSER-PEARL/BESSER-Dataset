





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_ChildTicket extends Ticket {

    private boolean isSchoolTrip;



    public CoachBusWithEDataType_ChildTicket(
        boolean isSchoolTrip    ) {
        super(
        );
        this.isSchoolTrip = isSchoolTrip;
    }


    public boolean getIsschooltrip() {
        return isSchoolTrip;
    }

    public void setIsschooltrip(boolean isSchoolTrip) {
        this.isSchoolTrip = isSchoolTrip;
    }


}