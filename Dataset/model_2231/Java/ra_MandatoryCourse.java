





import java.util.List;
import java.util.ArrayList;

public class ra_MandatoryCourse  {

    private boolean mandatory;
    private float credit;





    private ra_Course ra_course;




    private ra_Semester ra_semester;




    private ra_StudyPlan ra_studyplan;




    private ra_Semester ra_semester;




    private ra_Course ra_course;


    public ra_MandatoryCourse(
        boolean mandatory,        float credit    ) {
        this.mandatory = mandatory;
        this.credit = credit;
    }


    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public float getCredit() {
        return credit;
    }

    public void setCredit(float credit) {
        this.credit = credit;
    }

    public ra_Course getRa_course() {
        return ra_course;
    }

    public void setRa_course(ra_Course ra_course) {
        this.ra_course = ra_course;
    }
    public ra_Semester getRa_semester() {
        return ra_semester;
    }

    public void setRa_semester(ra_Semester ra_semester) {
        this.ra_semester = ra_semester;
    }
    public ra_StudyPlan getRa_studyplan() {
        return ra_studyplan;
    }

    public void setRa_studyplan(ra_StudyPlan ra_studyplan) {
        this.ra_studyplan = ra_studyplan;
    }
    public ra_Semester getRa_semester() {
        return ra_semester;
    }

    public void setRa_semester(ra_Semester ra_semester) {
        this.ra_semester = ra_semester;
    }
    public ra_Course getRa_course() {
        return ra_course;
    }

    public void setRa_course(ra_Course ra_course) {
        this.ra_course = ra_course;
    }

}