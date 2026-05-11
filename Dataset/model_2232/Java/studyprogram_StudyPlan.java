





import java.util.List;
import java.util.ArrayList;

public class studyprogram_StudyPlan  {

    private String name;





    private List<studyprogram_StudyPlan> studyprogram_studyplans;




    private studyprogram_Program studyprogram_program;




    private studyprogram_Program studyprogram_program;




    private studyprogram_StudyPlan studyprogram_studyplan;


    public studyprogram_StudyPlan(
        String name    ) {
        this.name = name;
        this.studyprogram_studyplans = new ArrayList<>();
    }

    public studyprogram_StudyPlan(
        String name        ArrayList<studyprogram_StudyPlan> studyprogram_studyplans    ) {
        this.name = name;
        this.studyprogram_studyplans = studyprogram_studyplans;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studyprogram_StudyPlan> getStudyprogram_studyplans() {
        return studyprogram_studyplans;
    }

    public void addStudyprogram_studyplan(Studyprogram_studyplan studyprogram_studyplan) {
        this.studyprogram_studyplans.add(studyprogram_studyplan);
    }
    public studyprogram_Program getStudyprogram_program() {
        return studyprogram_program;
    }

    public void setStudyprogram_program(studyprogram_Program studyprogram_program) {
        this.studyprogram_program = studyprogram_program;
    }
    public studyprogram_Program getStudyprogram_program() {
        return studyprogram_program;
    }

    public void setStudyprogram_program(studyprogram_Program studyprogram_program) {
        this.studyprogram_program = studyprogram_program;
    }
    public studyprogram_StudyPlan getStudyprogram_studyplan() {
        return studyprogram_studyplan;
    }

    public void setStudyprogram_studyplan(studyprogram_StudyPlan studyprogram_studyplan) {
        this.studyprogram_studyplan = studyprogram_studyplan;
    }

}