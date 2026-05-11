





import java.util.List;
import java.util.ArrayList;

public class studyplan_Semester  {

    private int year;
    private String semesterType;





    private List<studyplan_Course> studyplan_courses;




    private studyplan_FieldOfStudy studyplan_fieldofstudy;




    private studyplan_Specialization studyplan_specialization;




    private studyplan_StudyPlan studyplan_studyplan;




    private studyplan_CourseGroup studyplan_coursegroup;


    public studyplan_Semester(
        int year,        String semesterType    ) {
        this.year = year;
        this.semesterType = semesterType;
        this.studyplan_courses = new ArrayList<>();
    }

    public studyplan_Semester(
        int year,        String semesterType        ArrayList<studyplan_Course> studyplan_courses    ) {
        this.year = year;
        this.semesterType = semesterType;
        this.studyplan_courses = studyplan_courses;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getSemestertype() {
        return semesterType;
    }

    public void setSemestertype(String semesterType) {
        this.semesterType = semesterType;
    }

    public List<studyplan_Course> getStudyplan_courses() {
        return studyplan_courses;
    }

    public void addStudyplan_course(Studyplan_course studyplan_course) {
        this.studyplan_courses.add(studyplan_course);
    }
    public studyplan_FieldOfStudy getStudyplan_fieldofstudy() {
        return studyplan_fieldofstudy;
    }

    public void setStudyplan_fieldofstudy(studyplan_FieldOfStudy studyplan_fieldofstudy) {
        this.studyplan_fieldofstudy = studyplan_fieldofstudy;
    }
    public studyplan_Specialization getStudyplan_specialization() {
        return studyplan_specialization;
    }

    public void setStudyplan_specialization(studyplan_Specialization studyplan_specialization) {
        this.studyplan_specialization = studyplan_specialization;
    }
    public studyplan_StudyPlan getStudyplan_studyplan() {
        return studyplan_studyplan;
    }

    public void setStudyplan_studyplan(studyplan_StudyPlan studyplan_studyplan) {
        this.studyplan_studyplan = studyplan_studyplan;
    }
    public studyplan_CourseGroup getStudyplan_coursegroup() {
        return studyplan_coursegroup;
    }

    public void setStudyplan_coursegroup(studyplan_CourseGroup studyplan_coursegroup) {
        this.studyplan_coursegroup = studyplan_coursegroup;
    }

}