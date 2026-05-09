





import java.util.List;
import java.util.ArrayList;

public class eTJ_ResourceAttributes extends ExportAttribute {

    private boolean workingHours;
    private boolean none;
    private boolean booking;
    private boolean all;
    private boolean vacation;



    public eTJ_ResourceAttributes(
        boolean workingHours,        boolean none,        boolean booking,        boolean all,        boolean vacation    ) {
        super(
        );
        this.workingHours = workingHours;
        this.none = none;
        this.booking = booking;
        this.all = all;
        this.vacation = vacation;
    }


    public boolean getWorkinghours() {
        return workingHours;
    }

    public void setWorkinghours(boolean workingHours) {
        this.workingHours = workingHours;
    }
    public boolean getNone() {
        return none;
    }

    public void setNone(boolean none) {
        this.none = none;
    }
    public boolean getBooking() {
        return booking;
    }

    public void setBooking(boolean booking) {
        this.booking = booking;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public boolean getVacation() {
        return vacation;
    }

    public void setVacation(boolean vacation) {
        this.vacation = vacation;
    }


}