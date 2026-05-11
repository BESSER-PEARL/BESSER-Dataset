





import java.util.List;
import java.util.ArrayList;

public class studyplan_Program  {

    private String name;
    private String code;





    private List<studyplan_Specialization> studyplan_specializations;




    private studyplan_Department studyplan_department;




    private studyplan_Department studyplan_department;




    private List<studyplan_Semester> studyplan_semesters;


    public studyplan_Program(
        String name,        String code    ) {
        this.name = name;
        this.code = code;
        this.studyplan_specializations = new ArrayList<>();
        this.studyplan_semesters = new ArrayList<>();
    }

    public studyplan_Program(
        String name,        String code        ArrayList<studyplan_Specialization> studyplan_specializations,        ArrayList<studyplan_Semester> studyplan_semesters    ) {
        this.name = name;
        this.code = code;
        this.studyplan_specializations = studyplan_specializations;
        this.studyplan_semesters = studyplan_semesters;
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

    public List<studyplan_Specialization> getStudyplan_specializations() {
        return studyplan_specializations;
    }

    public void addStudyplan_specialization(Studyplan_specialization studyplan_specialization) {
        this.studyplan_specializations.add(studyplan_specialization);
    }
    public studyplan_Department getStudyplan_department() {
        return studyplan_department;
    }

    public void setStudyplan_department(studyplan_Department studyplan_department) {
        this.studyplan_department = studyplan_department;
    }
    public studyplan_Department getStudyplan_department() {
        return studyplan_department;
    }

    public void setStudyplan_department(studyplan_Department studyplan_department) {
        this.studyplan_department = studyplan_department;
    }
    public List<studyplan_Semester> getStudyplan_semesters() {
        return studyplan_semesters;
    }

    public void addStudyplan_semester(Studyplan_semester studyplan_semester) {
        this.studyplan_semesters.add(studyplan_semester);
    }

}