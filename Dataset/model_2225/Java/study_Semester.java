





import java.util.List;
import java.util.ArrayList;

public class study_Semester  {

    private String fallOrSpring;
    private int semesterNumber;





    private study_Specialization study_specialization;




    private study_StudyPlan study_studyplan;


    public study_Semester(
        String fallOrSpring,        int semesterNumber    ) {
        this.fallOrSpring = fallOrSpring;
        this.semesterNumber = semesterNumber;
    }


    public String getFallorspring() {
        return fallOrSpring;
    }

    public void setFallorspring(String fallOrSpring) {
        this.fallOrSpring = fallOrSpring;
    }
    public int getSemesternumber() {
        return semesterNumber;
    }

    public void setSemesternumber(int semesterNumber) {
        this.semesterNumber = semesterNumber;
    }

    public study_Specialization getStudy_specialization() {
        return study_specialization;
    }

    public void setStudy_specialization(study_Specialization study_specialization) {
        this.study_specialization = study_specialization;
    }
    public study_StudyPlan getStudy_studyplan() {
        return study_studyplan;
    }

    public void setStudy_studyplan(study_StudyPlan study_studyplan) {
        this.study_studyplan = study_studyplan;
    }

}