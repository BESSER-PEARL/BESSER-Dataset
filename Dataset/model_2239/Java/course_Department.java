





import java.util.List;
import java.util.ArrayList;

public class course_Department  {

    private String name;
    private String shortName;





    private course_Faculty course_faculty;




    private course_Faculty course_faculty;


    public course_Department(
        String name,        String shortName    ) {
        this.name = name;
        this.shortName = shortName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }

    public course_Faculty getCourse_faculty() {
        return course_faculty;
    }

    public void setCourse_faculty(course_Faculty course_faculty) {
        this.course_faculty = course_faculty;
    }
    public course_Faculty getCourse_faculty() {
        return course_faculty;
    }

    public void setCourse_faculty(course_Faculty course_faculty) {
        this.course_faculty = course_faculty;
    }

}