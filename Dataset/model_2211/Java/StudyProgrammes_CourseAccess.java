





import java.util.List;
import java.util.ArrayList;

public class StudyProgrammes_CourseAccess  {

    private String access;





    private StudyProgrammes_Course studyprogrammes_course;




    private StudyProgrammes_Semester studyprogrammes_semester;


    public StudyProgrammes_CourseAccess(
        String access    ) {
        this.access = access;
    }


    public String getAccess() {
        return access;
    }

    public void setAccess(String access) {
        this.access = access;
    }

    public StudyProgrammes_Course getStudyprogrammes_course() {
        return studyprogrammes_course;
    }

    public void setStudyprogrammes_course(StudyProgrammes_Course studyprogrammes_course) {
        this.studyprogrammes_course = studyprogrammes_course;
    }
    public StudyProgrammes_Semester getStudyprogrammes_semester() {
        return studyprogrammes_semester;
    }

    public void setStudyprogrammes_semester(StudyProgrammes_Semester studyprogrammes_semester) {
        this.studyprogrammes_semester = studyprogrammes_semester;
    }

}