





import java.util.List;
import java.util.ArrayList;

public class study_Department  {

    private String name;
    private String code;





    private study_Semester study_semester;




    private List<study_Semester> study_semesters;


    public study_Department(
        String name,        String code    ) {
        this.name = name;
        this.code = code;
        this.study_semesters = new ArrayList<>();
    }

    public study_Department(
        String name,        String code        ArrayList<study_Semester> study_semesters    ) {
        this.name = name;
        this.code = code;
        this.study_semesters = study_semesters;
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

    public study_Semester getStudy_semester() {
        return study_semester;
    }

    public void setStudy_semester(study_Semester study_semester) {
        this.study_semester = study_semester;
    }
    public List<study_Semester> getStudy_semesters() {
        return study_semesters;
    }

    public void addStudy_semester(Study_semester study_semester) {
        this.study_semesters.add(study_semester);
    }

}