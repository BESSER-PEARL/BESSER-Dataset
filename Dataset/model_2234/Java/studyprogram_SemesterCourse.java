





import java.util.List;
import java.util.ArrayList;

public class studyprogram_SemesterCourse  {

    private String name;
    private String type;





    private studyprogram_Semester studyprogram_semester;




    private studyprogram_Semester studyprogram_semester;




    private List<studyprogram_Course> studyprogram_courses;


    public studyprogram_SemesterCourse(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
        this.studyprogram_courses = new ArrayList<>();
    }

    public studyprogram_SemesterCourse(
        String name,        String type        ArrayList<studyprogram_Course> studyprogram_courses    ) {
        this.name = name;
        this.type = type;
        this.studyprogram_courses = studyprogram_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public studyprogram_Semester getStudyprogram_semester() {
        return studyprogram_semester;
    }

    public void setStudyprogram_semester(studyprogram_Semester studyprogram_semester) {
        this.studyprogram_semester = studyprogram_semester;
    }
    public studyprogram_Semester getStudyprogram_semester() {
        return studyprogram_semester;
    }

    public void setStudyprogram_semester(studyprogram_Semester studyprogram_semester) {
        this.studyprogram_semester = studyprogram_semester;
    }
    public List<studyprogram_Course> getStudyprogram_courses() {
        return studyprogram_courses;
    }

    public void addStudyprogram_course(Studyprogram_course studyprogram_course) {
        this.studyprogram_courses.add(studyprogram_course);
    }

}