





import java.util.List;
import java.util.ArrayList;

public class studyplan_Specialization  {

    private String name;





    private studyplan_Specialization studyplan_specialization;




    private studyplan_Program studyplan_program;




    private List<studyplan_Semester> studyplan_semesters;


    public studyplan_Specialization(
        String name    ) {
        this.name = name;
        this.studyplan_semesters = new ArrayList<>();
    }

    public studyplan_Specialization(
        String name        ArrayList<studyplan_Semester> studyplan_semesters    ) {
        this.name = name;
        this.studyplan_semesters = studyplan_semesters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public studyplan_Specialization getStudyplan_specialization() {
        return studyplan_specialization;
    }

    public void setStudyplan_specialization(studyplan_Specialization studyplan_specialization) {
        this.studyplan_specialization = studyplan_specialization;
    }
    public studyplan_Program getStudyplan_program() {
        return studyplan_program;
    }

    public void setStudyplan_program(studyplan_Program studyplan_program) {
        this.studyplan_program = studyplan_program;
    }
    public List<studyplan_Semester> getStudyplan_semesters() {
        return studyplan_semesters;
    }

    public void addStudyplan_semester(Studyplan_semester studyplan_semester) {
        this.studyplan_semesters.add(studyplan_semester);
    }

}