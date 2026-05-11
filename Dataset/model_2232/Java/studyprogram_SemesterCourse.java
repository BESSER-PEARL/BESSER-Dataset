





import java.util.List;
import java.util.ArrayList;

public class studyprogram_SemesterCourse  {

    private String type;
    private String name;





    private studyprogram_Course studyprogram_course;




    private studyprogram_Semester studyprogram_semester;




    private studyprogram_Semester studyprogram_semester;


    public studyprogram_SemesterCourse(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public studyprogram_Course getStudyprogram_course() {
        return studyprogram_course;
    }

    public void setStudyprogram_course(studyprogram_Course studyprogram_course) {
        this.studyprogram_course = studyprogram_course;
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

}