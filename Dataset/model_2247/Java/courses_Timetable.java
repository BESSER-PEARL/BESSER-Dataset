





import java.util.List;
import java.util.ArrayList;

public class courses_Timetable  {






    private courses_CourseInstance courses_courseinstance;




    private List<courses_CourseHour> courses_coursehours;


    public courses_Timetable(
    ) {
        this.courses_coursehours = new ArrayList<>();
    }

    public courses_Timetable(
        ArrayList<courses_CourseHour> courses_coursehours    ) {
        this.courses_coursehours = courses_coursehours;
    }


    public courses_CourseInstance getCourses_courseinstance() {
        return courses_courseinstance;
    }

    public void setCourses_courseinstance(courses_CourseInstance courses_courseinstance) {
        this.courses_courseinstance = courses_courseinstance;
    }
    public List<courses_CourseHour> getCourses_coursehours() {
        return courses_coursehours;
    }

    public void addCourses_coursehour(Courses_coursehour courses_coursehour) {
        this.courses_coursehours.add(courses_coursehour);
    }

}