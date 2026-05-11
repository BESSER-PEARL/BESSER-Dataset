





import java.util.List;
import java.util.ArrayList;

public class StudyProgrammes_Course  {

    private float credits;
    private String name;
    private String code;
    private String availableSemesters;





    private StudyProgrammes_Department studyprogrammes_department;


    public StudyProgrammes_Course(
        float credits,        String name,        String code,        String availableSemesters    ) {
        this.credits = credits;
        this.name = name;
        this.code = code;
        this.availableSemesters = availableSemesters;
    }


    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
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
    public String getAvailablesemesters() {
        return availableSemesters;
    }

    public void setAvailablesemesters(String availableSemesters) {
        this.availableSemesters = availableSemesters;
    }

    public StudyProgrammes_Department getStudyprogrammes_department() {
        return studyprogrammes_department;
    }

    public void setStudyprogrammes_department(StudyProgrammes_Department studyprogrammes_department) {
        this.studyprogrammes_department = studyprogrammes_department;
    }

}