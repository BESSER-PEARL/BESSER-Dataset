





import java.util.List;
import java.util.ArrayList;

public class studyPlan_StudyProgramme  {

    private String codename;
    private int lengthInYears;
    private String name;





    private studyPlan_University studyplan_university;




    private studyPlan_University studyplan_university;


    public studyPlan_StudyProgramme(
        String codename,        int lengthInYears,        String name    ) {
        this.codename = codename;
        this.lengthInYears = lengthInYears;
        this.name = name;
    }


    public String getCodename() {
        return codename;
    }

    public void setCodename(String codename) {
        this.codename = codename;
    }
    public int getLengthinyears() {
        return lengthInYears;
    }

    public void setLengthinyears(int lengthInYears) {
        this.lengthInYears = lengthInYears;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public studyPlan_University getStudyplan_university() {
        return studyplan_university;
    }

    public void setStudyplan_university(studyPlan_University studyplan_university) {
        this.studyplan_university = studyplan_university;
    }
    public studyPlan_University getStudyplan_university() {
        return studyplan_university;
    }

    public void setStudyplan_university(studyPlan_University studyplan_university) {
        this.studyplan_university = studyplan_university;
    }

}