





import java.util.List;
import java.util.ArrayList;

public class studyPlan_Course  {

    private String codename;
    private float credits;
    private String name;
    private int level;





    private studyPlan_SemesterPlan studyplan_semesterplan;




    private studyPlan_SemesterProgramme studyplan_semesterprogramme;




    private studyPlan_SemesterProgramme studyplan_semesterprogramme;


    public studyPlan_Course(
        String codename,        float credits,        String name,        int level    ) {
        this.codename = codename;
        this.credits = credits;
        this.name = name;
        this.level = level;
    }


    public String getCodename() {
        return codename;
    }

    public void setCodename(String codename) {
        this.codename = codename;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public studyPlan_SemesterPlan getStudyplan_semesterplan() {
        return studyplan_semesterplan;
    }

    public void setStudyplan_semesterplan(studyPlan_SemesterPlan studyplan_semesterplan) {
        this.studyplan_semesterplan = studyplan_semesterplan;
    }
    public studyPlan_SemesterProgramme getStudyplan_semesterprogramme() {
        return studyplan_semesterprogramme;
    }

    public void setStudyplan_semesterprogramme(studyPlan_SemesterProgramme studyplan_semesterprogramme) {
        this.studyplan_semesterprogramme = studyplan_semesterprogramme;
    }
    public studyPlan_SemesterProgramme getStudyplan_semesterprogramme() {
        return studyplan_semesterprogramme;
    }

    public void setStudyplan_semesterprogramme(studyPlan_SemesterProgramme studyplan_semesterprogramme) {
        this.studyplan_semesterprogramme = studyplan_semesterprogramme;
    }

}