





import java.util.List;
import java.util.ArrayList;

public class project_Interval4  {

    private String start;
    private String end;





    private project_Booking project_booking;


    public project_Interval4(
        String start,        String end    ) {
        this.start = start;
        this.end = end;
    }


    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }

    public project_Booking getProject_booking() {
        return project_booking;
    }

    public void setProject_booking(project_Booking project_booking) {
        this.project_booking = project_booking;
    }

}