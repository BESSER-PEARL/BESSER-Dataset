





import java.util.List;
import java.util.ArrayList;

public class study_CourseRelationship  {

    private int numExamAttempts;
    private String grade;





    private study_IndividualStudyPlan study_individualstudyplan;




    private study_IndividualStudyPlan study_individualstudyplan;




    private study_Course study_course;


    public study_CourseRelationship(
        int numExamAttempts,        String grade    ) {
        this.numExamAttempts = numExamAttempts;
        this.grade = grade;
    }


    public int getNumexamattempts() {
        return numExamAttempts;
    }

    public void setNumexamattempts(int numExamAttempts) {
        this.numExamAttempts = numExamAttempts;
    }
    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }

    public study_IndividualStudyPlan getStudy_individualstudyplan() {
        return study_individualstudyplan;
    }

    public void setStudy_individualstudyplan(study_IndividualStudyPlan study_individualstudyplan) {
        this.study_individualstudyplan = study_individualstudyplan;
    }
    public study_IndividualStudyPlan getStudy_individualstudyplan() {
        return study_individualstudyplan;
    }

    public void setStudy_individualstudyplan(study_IndividualStudyPlan study_individualstudyplan) {
        this.study_individualstudyplan = study_individualstudyplan;
    }
    public study_Course getStudy_course() {
        return study_course;
    }

    public void setStudy_course(study_Course study_course) {
        this.study_course = study_course;
    }

}