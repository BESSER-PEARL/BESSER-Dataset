





import java.util.List;
import java.util.ArrayList;

public class studyplan_SemesterCourse  {

    private String status;





    private studyplan_Semester studyplan_semester;


    public studyplan_SemesterCourse(
        String status    ) {
        this.status = status;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public studyplan_Semester getStudyplan_semester() {
        return studyplan_semester;
    }

    public void setStudyplan_semester(studyplan_Semester studyplan_semester) {
        this.studyplan_semester = studyplan_semester;
    }

}