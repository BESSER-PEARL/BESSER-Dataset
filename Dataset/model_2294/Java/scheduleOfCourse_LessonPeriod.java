





import java.util.List;
import java.util.ArrayList;

public class scheduleOfCourse_LessonPeriod  {

    private String end;
    private String start;



    public scheduleOfCourse_LessonPeriod(
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


}