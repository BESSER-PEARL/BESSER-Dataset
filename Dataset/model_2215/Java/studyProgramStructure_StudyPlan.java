





import java.util.List;
import java.util.ArrayList;

public class studyProgramStructure_StudyPlan  {






    private List<studyProgramStructure_Semester> studyprogramstructure_semesters;




    private studyProgramStructure_Student studyprogramstructure_student;




    private studyProgramStructure_Student studyprogramstructure_student;


    public studyProgramStructure_StudyPlan(
    ) {
        this.studyprogramstructure_semesters = new ArrayList<>();
    }

    public studyProgramStructure_StudyPlan(
        ArrayList<studyProgramStructure_Semester> studyprogramstructure_semesters    ) {
        this.studyprogramstructure_semesters = studyprogramstructure_semesters;
    }


    public List<studyProgramStructure_Semester> getStudyprogramstructure_semesters() {
        return studyprogramstructure_semesters;
    }

    public void addStudyprogramstructure_semester(Studyprogramstructure_semester studyprogramstructure_semester) {
        this.studyprogramstructure_semesters.add(studyprogramstructure_semester);
    }
    public studyProgramStructure_Student getStudyprogramstructure_student() {
        return studyprogramstructure_student;
    }

    public void setStudyprogramstructure_student(studyProgramStructure_Student studyprogramstructure_student) {
        this.studyprogramstructure_student = studyprogramstructure_student;
    }
    public studyProgramStructure_Student getStudyprogramstructure_student() {
        return studyprogramstructure_student;
    }

    public void setStudyprogramstructure_student(studyProgramStructure_Student studyprogramstructure_student) {
        this.studyprogramstructure_student = studyprogramstructure_student;
    }

}