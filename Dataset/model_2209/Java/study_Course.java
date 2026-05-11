





import java.util.List;
import java.util.ArrayList;

public class study_Course  {

    private String name;
    private int level;
    private float credits;
    private String code;





    private study_Department study_department;




    private study_Department study_department;




    private study_SemesterCourse study_semestercourse;


    public study_Course(
        String name,        int level,        float credits,        String code    ) {
        this.name = name;
        this.level = level;
        this.credits = credits;
        this.code = code;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
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

    public study_Department getStudy_department() {
        return study_department;
    }

    public void setStudy_department(study_Department study_department) {
        this.study_department = study_department;
    }
    public study_Department getStudy_department() {
        return study_department;
    }

    public void setStudy_department(study_Department study_department) {
        this.study_department = study_department;
    }
    public study_SemesterCourse getStudy_semestercourse() {
        return study_semestercourse;
    }

    public void setStudy_semestercourse(study_SemesterCourse study_semestercourse) {
        this.study_semestercourse = study_semestercourse;
    }

}