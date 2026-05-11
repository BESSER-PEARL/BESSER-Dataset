





import java.util.List;
import java.util.ArrayList;

public class studyprograms_CourseAccess  {

    private String Access;





    private List<studyprograms_Course> studyprograms_courses;




    private studyprograms_Semester studyprograms_semester;


    public studyprograms_CourseAccess(
        String Access    ) {
        this.Access = Access;
        this.studyprograms_courses = new ArrayList<>();
    }

    public studyprograms_CourseAccess(
        String Access        ArrayList<studyprograms_Course> studyprograms_courses    ) {
        this.Access = Access;
        this.studyprograms_courses = studyprograms_courses;
    }

    public String getAccess() {
        return Access;
    }

    public void setAccess(String Access) {
        this.Access = Access;
    }

    public List<studyprograms_Course> getStudyprograms_courses() {
        return studyprograms_courses;
    }

    public void addStudyprograms_course(Studyprograms_course studyprograms_course) {
        this.studyprograms_courses.add(studyprograms_course);
    }
    public studyprograms_Semester getStudyprograms_semester() {
        return studyprograms_semester;
    }

    public void setStudyprograms_semester(studyprograms_Semester studyprograms_semester) {
        this.studyprograms_semester = studyprograms_semester;
    }

}