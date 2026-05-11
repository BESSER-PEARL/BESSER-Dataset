





import java.util.List;
import java.util.ArrayList;

public class studyplan_Specialization  {

    private String specName;





    private studyplan_Specialization studyplan_specialization;




    private studyplan_CourseGroup studyplan_coursegroup;


    public studyplan_Specialization(
        String specName    ) {
        this.specName = specName;
    }


    public String getSpecname() {
        return specName;
    }

    public void setSpecname(String specName) {
        this.specName = specName;
    }

    public studyplan_Specialization getStudyplan_specialization() {
        return studyplan_specialization;
    }

    public void setStudyplan_specialization(studyplan_Specialization studyplan_specialization) {
        this.studyplan_specialization = studyplan_specialization;
    }
    public studyplan_CourseGroup getStudyplan_coursegroup() {
        return studyplan_coursegroup;
    }

    public void setStudyplan_coursegroup(studyplan_CourseGroup studyplan_coursegroup) {
        this.studyplan_coursegroup = studyplan_coursegroup;
    }

}