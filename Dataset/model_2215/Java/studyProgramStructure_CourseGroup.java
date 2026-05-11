





import java.util.List;
import java.util.ArrayList;

public class studyProgramStructure_CourseGroup  {

    private String status;
    private String name;





    private studyProgramStructure_Semester studyprogramstructure_semester;




    private studyProgramStructure_Semester studyprogramstructure_semester;




    private List<studyProgramStructure_Course> studyprogramstructure_courses;


    public studyProgramStructure_CourseGroup(
        String status,        String name    ) {
        this.status = status;
        this.name = name;
        this.studyprogramstructure_courses = new ArrayList<>();
    }

    public studyProgramStructure_CourseGroup(
        String status,        String name        ArrayList<studyProgramStructure_Course> studyprogramstructure_courses    ) {
        this.status = status;
        this.name = name;
        this.studyprogramstructure_courses = studyprogramstructure_courses;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public studyProgramStructure_Semester getStudyprogramstructure_semester() {
        return studyprogramstructure_semester;
    }

    public void setStudyprogramstructure_semester(studyProgramStructure_Semester studyprogramstructure_semester) {
        this.studyprogramstructure_semester = studyprogramstructure_semester;
    }
    public studyProgramStructure_Semester getStudyprogramstructure_semester() {
        return studyprogramstructure_semester;
    }

    public void setStudyprogramstructure_semester(studyProgramStructure_Semester studyprogramstructure_semester) {
        this.studyprogramstructure_semester = studyprogramstructure_semester;
    }
    public List<studyProgramStructure_Course> getStudyprogramstructure_courses() {
        return studyprogramstructure_courses;
    }

    public void addStudyprogramstructure_course(Studyprogramstructure_course studyprogramstructure_course) {
        this.studyprogramstructure_courses.add(studyprogramstructure_course);
    }

}