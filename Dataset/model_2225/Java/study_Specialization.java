





import java.util.List;
import java.util.ArrayList;

public class study_Specialization  {

    private String name;





    private study_StudyPlan study_studyplan;


    public study_Specialization(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public study_StudyPlan getStudy_studyplan() {
        return study_studyplan;
    }

    public void setStudy_studyplan(study_StudyPlan study_studyplan) {
        this.study_studyplan = study_studyplan;
    }

}