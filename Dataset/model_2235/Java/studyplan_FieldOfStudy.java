





import java.util.List;
import java.util.ArrayList;

public class studyplan_FieldOfStudy  {

    private String fieldName;





    private studyplan_StudyPlan studyplan_studyplan;




    private studyplan_Specialization studyplan_specialization;


    public studyplan_FieldOfStudy(
        String fieldName    ) {
        this.fieldName = fieldName;
    }


    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }

    public studyplan_StudyPlan getStudyplan_studyplan() {
        return studyplan_studyplan;
    }

    public void setStudyplan_studyplan(studyplan_StudyPlan studyplan_studyplan) {
        this.studyplan_studyplan = studyplan_studyplan;
    }
    public studyplan_Specialization getStudyplan_specialization() {
        return studyplan_specialization;
    }

    public void setStudyplan_specialization(studyplan_Specialization studyplan_specialization) {
        this.studyplan_specialization = studyplan_specialization;
    }

}