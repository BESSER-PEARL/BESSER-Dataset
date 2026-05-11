





import java.util.List;
import java.util.ArrayList;

public class study_Semester  {

    private int ordinal;





    private List<study_Course> study_courses;




    private study_Specialization study_specialization;




    private study_IndividualStudyPlan study_individualstudyplan;




    private study_Specialization study_specialization;


    public study_Semester(
        int ordinal    ) {
        this.ordinal = ordinal;
        this.study_courses = new ArrayList<>();
    }

    public study_Semester(
        int ordinal        ArrayList<study_Course> study_courses    ) {
        this.ordinal = ordinal;
        this.study_courses = study_courses;
    }

    public int getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(int ordinal) {
        this.ordinal = ordinal;
    }

    public List<study_Course> getStudy_courses() {
        return study_courses;
    }

    public void addStudy_course(Study_course study_course) {
        this.study_courses.add(study_course);
    }
    public study_Specialization getStudy_specialization() {
        return study_specialization;
    }

    public void setStudy_specialization(study_Specialization study_specialization) {
        this.study_specialization = study_specialization;
    }
    public study_IndividualStudyPlan getStudy_individualstudyplan() {
        return study_individualstudyplan;
    }

    public void setStudy_individualstudyplan(study_IndividualStudyPlan study_individualstudyplan) {
        this.study_individualstudyplan = study_individualstudyplan;
    }
    public study_Specialization getStudy_specialization() {
        return study_specialization;
    }

    public void setStudy_specialization(study_Specialization study_specialization) {
        this.study_specialization = study_specialization;
    }

}