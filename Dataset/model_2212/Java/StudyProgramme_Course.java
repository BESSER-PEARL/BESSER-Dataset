





import java.util.List;
import java.util.ArrayList;

public class StudyProgramme_Course  {

    private float credits;
    private String code;
    private String name;
    private String level;





    private StudyProgramme_Semester studyprogramme_semester;




    private StudyProgramme_Specialization studyprogramme_specialization;


    public StudyProgramme_Course(
        float credits,        String code,        String name,        String level    ) {
        this.credits = credits;
        this.code = code;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public StudyProgramme_Semester getStudyprogramme_semester() {
        return studyprogramme_semester;
    }

    public void setStudyprogramme_semester(StudyProgramme_Semester studyprogramme_semester) {
        this.studyprogramme_semester = studyprogramme_semester;
    }
    public StudyProgramme_Specialization getStudyprogramme_specialization() {
        return studyprogramme_specialization;
    }

    public void setStudyprogramme_specialization(StudyProgramme_Specialization studyprogramme_specialization) {
        this.studyprogramme_specialization = studyprogramme_specialization;
    }

}