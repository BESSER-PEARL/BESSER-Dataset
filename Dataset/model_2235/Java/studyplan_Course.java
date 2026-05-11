





import java.util.List;
import java.util.ArrayList;

public class studyplan_Course  {

    private int courseCode;
    private String status;
    private String courseName;
    private float credit;





    private studyplan_CourseGroup studyplan_coursegroup;




    private studyplan_CourseGroup studyplan_coursegroup;




    private studyplan_StudyPlan studyplan_studyplan;


    public studyplan_Course(
        int courseCode,        String status,        String courseName,        float credit    ) {
        this.courseCode = courseCode;
        this.status = status;
        this.courseName = courseName;
        this.credit = credit;
    }


    public int getCoursecode() {
        return courseCode;
    }

    public void setCoursecode(int courseCode) {
        this.courseCode = courseCode;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }
    public float getCredit() {
        return credit;
    }

    public void setCredit(float credit) {
        this.credit = credit;
    }

    public studyplan_CourseGroup getStudyplan_coursegroup() {
        return studyplan_coursegroup;
    }

    public void setStudyplan_coursegroup(studyplan_CourseGroup studyplan_coursegroup) {
        this.studyplan_coursegroup = studyplan_coursegroup;
    }
    public studyplan_CourseGroup getStudyplan_coursegroup() {
        return studyplan_coursegroup;
    }

    public void setStudyplan_coursegroup(studyplan_CourseGroup studyplan_coursegroup) {
        this.studyplan_coursegroup = studyplan_coursegroup;
    }
    public studyplan_StudyPlan getStudyplan_studyplan() {
        return studyplan_studyplan;
    }

    public void setStudyplan_studyplan(studyplan_StudyPlan studyplan_studyplan) {
        this.studyplan_studyplan = studyplan_studyplan;
    }

}