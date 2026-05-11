





import java.util.List;
import java.util.ArrayList;

public class study_Course  {

    private float credits;
    private int level;
    private String name;
    private String code;





    private study_SemesterCourse study_semestercourse;


    public study_Course(
        float credits,        int level,        String name,        String code    ) {
        this.credits = credits;
        this.level = level;
        this.name = name;
        this.code = code;
    }


    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public study_SemesterCourse getStudy_semestercourse() {
        return study_semestercourse;
    }

    public void setStudy_semestercourse(study_SemesterCourse study_semestercourse) {
        this.study_semestercourse = study_semestercourse;
    }

}