





import java.util.List;
import java.util.ArrayList;

public class project_ResourceAttributes extends ExportAttribute {

    private boolean vacation;
    private boolean none;
    private boolean all;
    private boolean workingHours;
    private boolean booking;



    public project_ResourceAttributes(
        boolean vacation,        boolean none,        boolean all,        boolean workingHours,        boolean booking    ) {
        super(
        );
        this.vacation = vacation;
        this.none = none;
        this.all = all;
        this.workingHours = workingHours;
        this.booking = booking;
    }


    public boolean getVacation() {
        return vacation;
    }

    public void setVacation(boolean vacation) {
        this.vacation = vacation;
    }
    public boolean getNone() {
        return none;
    }

    public void setNone(boolean none) {
        this.none = none;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public boolean getWorkinghours() {
        return workingHours;
    }

    public void setWorkinghours(boolean workingHours) {
        this.workingHours = workingHours;
    }
    public boolean getBooking() {
        return booking;
    }

    public void setBooking(boolean booking) {
        this.booking = booking;
    }


}