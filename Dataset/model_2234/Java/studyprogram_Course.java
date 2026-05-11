





import java.util.List;
import java.util.ArrayList;

public class studyprogram_Course  {

    private String semester;
    private String name;
    private String credits;





    private studyprogram_Department studyprogram_department;




    private studyprogram_Department studyprogram_department;


    public studyprogram_Course(
        String semester,        String name,        String credits    ) {
        this.semester = semester;
        this.name = name;
        this.credits = credits;
    }


    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCredits() {
        return credits;
    }

    public void setCredits(String credits) {
        this.credits = credits;
    }

    public studyprogram_Department getStudyprogram_department() {
        return studyprogram_department;
    }

    public void setStudyprogram_department(studyprogram_Department studyprogram_department) {
        this.studyprogram_department = studyprogram_department;
    }
    public studyprogram_Department getStudyprogram_department() {
        return studyprogram_department;
    }

    public void setStudyprogram_department(studyprogram_Department studyprogram_department) {
        this.studyprogram_department = studyprogram_department;
    }

}