





import java.util.List;
import java.util.ArrayList;

public class studyprogram_Specialisation  {

    private String name;





    private studyprogram_StudyPlan studyprogram_studyplan;




    private List<studyprogram_Year> studyprogram_years;




    private studyprogram_StudyPlan studyprogram_studyplan;


    public studyprogram_Specialisation(
        String name    ) {
        this.name = name;
        this.studyprogram_years = new ArrayList<>();
    }

    public studyprogram_Specialisation(
        String name        ArrayList<studyprogram_Year> studyprogram_years    ) {
        this.name = name;
        this.studyprogram_years = studyprogram_years;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public studyprogram_StudyPlan getStudyprogram_studyplan() {
        return studyprogram_studyplan;
    }

    public void setStudyprogram_studyplan(studyprogram_StudyPlan studyprogram_studyplan) {
        this.studyprogram_studyplan = studyprogram_studyplan;
    }
    public List<studyprogram_Year> getStudyprogram_years() {
        return studyprogram_years;
    }

    public void addStudyprogram_year(Studyprogram_year studyprogram_year) {
        this.studyprogram_years.add(studyprogram_year);
    }
    public studyprogram_StudyPlan getStudyprogram_studyplan() {
        return studyprogram_studyplan;
    }

    public void setStudyprogram_studyplan(studyprogram_StudyPlan studyprogram_studyplan) {
        this.studyprogram_studyplan = studyprogram_studyplan;
    }

}