





import java.util.List;
import java.util.ArrayList;

public class CourseCalendar  {

    private int endTime;
    private int startTime;





    private Courses courses;


    public CourseCalendar(
        int endTime,        int startTime    ) {
        this.endTime = endTime;
        this.startTime = startTime;
    }


    public int getEndtime() {
        return endTime;
    }

    public void setEndtime(int endTime) {
        this.endTime = endTime;
    }
    public int getStarttime() {
        return startTime;
    }

    public void setStarttime(int startTime) {
        this.startTime = startTime;
    }

    public Courses getCourses() {
        return courses;
    }

    public void setCourses(Courses courses) {
        this.courses = courses;
    }

}