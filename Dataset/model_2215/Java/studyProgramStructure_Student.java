





import java.util.List;
import java.util.ArrayList;

public class studyProgramStructure_Student  {

    private String name;





    private studyProgramStructure_University studyprogramstructure_university;




    private studyProgramStructure_Program studyprogramstructure_program;




    private List<studyProgramStructure_Specialization> studyprogramstructure_specializations;


    public studyProgramStructure_Student(
        String name    ) {
        this.name = name;
        this.studyprogramstructure_specializations = new ArrayList<>();
    }

    public studyProgramStructure_Student(
        String name        ArrayList<studyProgramStructure_Specialization> studyprogramstructure_specializations    ) {
        this.name = name;
        this.studyprogramstructure_specializations = studyprogramstructure_specializations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public studyProgramStructure_University getStudyprogramstructure_university() {
        return studyprogramstructure_university;
    }

    public void setStudyprogramstructure_university(studyProgramStructure_University studyprogramstructure_university) {
        this.studyprogramstructure_university = studyprogramstructure_university;
    }
    public studyProgramStructure_Program getStudyprogramstructure_program() {
        return studyprogramstructure_program;
    }

    public void setStudyprogramstructure_program(studyProgramStructure_Program studyprogramstructure_program) {
        this.studyprogramstructure_program = studyprogramstructure_program;
    }
    public List<studyProgramStructure_Specialization> getStudyprogramstructure_specializations() {
        return studyprogramstructure_specializations;
    }

    public void addStudyprogramstructure_specialization(Studyprogramstructure_specialization studyprogramstructure_specialization) {
        this.studyprogramstructure_specializations.add(studyprogramstructure_specialization);
    }

}