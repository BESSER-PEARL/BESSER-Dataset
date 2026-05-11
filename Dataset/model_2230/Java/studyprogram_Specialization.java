





import java.util.List;
import java.util.ArrayList;

public class studyprogram_Specialization  {

    private String name;





    private List<studyprogram_Semester> studyprogram_semesters;




    private studyprogram_Program studyprogram_program;




    private List<studyprogram_Specialization> studyprogram_specializations;


    public studyprogram_Specialization(
        String name    ) {
        this.name = name;
        this.studyprogram_semesters = new ArrayList<>();
        this.studyprogram_specializations = new ArrayList<>();
    }

    public studyprogram_Specialization(
        String name        ArrayList<studyprogram_Semester> studyprogram_semesters,        ArrayList<studyprogram_Specialization> studyprogram_specializations    ) {
        this.name = name;
        this.studyprogram_semesters = studyprogram_semesters;
        this.studyprogram_specializations = studyprogram_specializations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studyprogram_Semester> getStudyprogram_semesters() {
        return studyprogram_semesters;
    }

    public void addStudyprogram_semester(Studyprogram_semester studyprogram_semester) {
        this.studyprogram_semesters.add(studyprogram_semester);
    }
    public studyprogram_Program getStudyprogram_program() {
        return studyprogram_program;
    }

    public void setStudyprogram_program(studyprogram_Program studyprogram_program) {
        this.studyprogram_program = studyprogram_program;
    }
    public List<studyprogram_Specialization> getStudyprogram_specializations() {
        return studyprogram_specializations;
    }

    public void addStudyprogram_specialization(Studyprogram_specialization studyprogram_specialization) {
        this.studyprogram_specializations.add(studyprogram_specialization);
    }

}