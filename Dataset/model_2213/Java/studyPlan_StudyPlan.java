





import java.util.List;
import java.util.ArrayList;

public class studyPlan_StudyPlan  {






    private List<studyPlan_SemesterPlan> studyplan_semesterplans;




    private studyPlan_SemesterPlan studyplan_semesterplan;




    private studyPlan_Student studyplan_student;




    private studyPlan_Student studyplan_student;


    public studyPlan_StudyPlan(
    ) {
        this.studyplan_semesterplans = new ArrayList<>();
    }

    public studyPlan_StudyPlan(
        ArrayList<studyPlan_SemesterPlan> studyplan_semesterplans    ) {
        this.studyplan_semesterplans = studyplan_semesterplans;
    }


    public List<studyPlan_SemesterPlan> getStudyplan_semesterplans() {
        return studyplan_semesterplans;
    }

    public void addStudyplan_semesterplan(Studyplan_semesterplan studyplan_semesterplan) {
        this.studyplan_semesterplans.add(studyplan_semesterplan);
    }
    public studyPlan_SemesterPlan getStudyplan_semesterplan() {
        return studyplan_semesterplan;
    }

    public void setStudyplan_semesterplan(studyPlan_SemesterPlan studyplan_semesterplan) {
        this.studyplan_semesterplan = studyplan_semesterplan;
    }
    public studyPlan_Student getStudyplan_student() {
        return studyplan_student;
    }

    public void setStudyplan_student(studyPlan_Student studyplan_student) {
        this.studyplan_student = studyplan_student;
    }
    public studyPlan_Student getStudyplan_student() {
        return studyplan_student;
    }

    public void setStudyplan_student(studyPlan_Student studyplan_student) {
        this.studyplan_student = studyplan_student;
    }

}