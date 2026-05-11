





import java.util.List;
import java.util.ArrayList;

public class studyplan_Department  {

    private String name;





    private studyplan_Program studyplan_program;




    private List<studyplan_Program> studyplan_programs;


    public studyplan_Department(
        String name    ) {
        this.name = name;
        this.studyplan_programs = new ArrayList<>();
    }

    public studyplan_Department(
        String name        ArrayList<studyplan_Program> studyplan_programs    ) {
        this.name = name;
        this.studyplan_programs = studyplan_programs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public studyplan_Program getStudyplan_program() {
        return studyplan_program;
    }

    public void setStudyplan_program(studyplan_Program studyplan_program) {
        this.studyplan_program = studyplan_program;
    }
    public List<studyplan_Program> getStudyplan_programs() {
        return studyplan_programs;
    }

    public void addStudyplan_program(Studyplan_program studyplan_program) {
        this.studyplan_programs.add(studyplan_program);
    }

}