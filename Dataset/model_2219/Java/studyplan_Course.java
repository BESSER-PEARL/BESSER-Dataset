





import java.util.List;
import java.util.ArrayList;

public class studyplan_Course  {

    private String name;
    private float credits;
    private String code;





    private studyplan_Department studyplan_department;




    private studyplan_SemesterCourse studyplan_semestercourse;




    private studyplan_Department studyplan_department;


    public studyplan_Course(
        String name,        float credits,        String code    ) {
        this.name = name;
        this.credits = credits;
        this.code = code;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public studyplan_Department getStudyplan_department() {
        return studyplan_department;
    }

    public void setStudyplan_department(studyplan_Department studyplan_department) {
        this.studyplan_department = studyplan_department;
    }
    public studyplan_SemesterCourse getStudyplan_semestercourse() {
        return studyplan_semestercourse;
    }

    public void setStudyplan_semestercourse(studyplan_SemesterCourse studyplan_semestercourse) {
        this.studyplan_semestercourse = studyplan_semestercourse;
    }
    public studyplan_Department getStudyplan_department() {
        return studyplan_department;
    }

    public void setStudyplan_department(studyplan_Department studyplan_department) {
        this.studyplan_department = studyplan_department;
    }

}