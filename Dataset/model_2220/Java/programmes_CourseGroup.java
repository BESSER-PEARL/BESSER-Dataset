





import java.util.List;
import java.util.ArrayList;

public class programmes_CourseGroup  {

    private String coursesType;
    private String name;





    private List<programmes_Course> programmes_courses;




    private programmes_Programme programmes_programme;


    public programmes_CourseGroup(
        String coursesType,        String name    ) {
        this.coursesType = coursesType;
        this.name = name;
        this.programmes_courses = new ArrayList<>();
    }

    public programmes_CourseGroup(
        String coursesType,        String name        ArrayList<programmes_Course> programmes_courses    ) {
        this.coursesType = coursesType;
        this.name = name;
        this.programmes_courses = programmes_courses;
    }

    public String getCoursestype() {
        return coursesType;
    }

    public void setCoursestype(String coursesType) {
        this.coursesType = coursesType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<programmes_Course> getProgrammes_courses() {
        return programmes_courses;
    }

    public void addProgrammes_course(Programmes_course programmes_course) {
        this.programmes_courses.add(programmes_course);
    }
    public programmes_Programme getProgrammes_programme() {
        return programmes_programme;
    }

    public void setProgrammes_programme(programmes_Programme programmes_programme) {
        this.programmes_programme = programmes_programme;
    }

}