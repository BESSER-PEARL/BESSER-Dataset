





import java.util.List;
import java.util.ArrayList;

public class scheduleOfCourse_Lesson  {

    private String end;
    private String start;





    private scheduleOfCourse_Shift scheduleofcourse_shift;


    public scheduleOfCourse_Lesson(
        String end,        String start    ) {
        this.end = end;
        this.start = start;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public scheduleOfCourse_Shift getScheduleofcourse_shift() {
        return scheduleofcourse_shift;
    }

    public void setScheduleofcourse_shift(scheduleOfCourse_Shift scheduleofcourse_shift) {
        this.scheduleofcourse_shift = scheduleofcourse_shift;
    }

}