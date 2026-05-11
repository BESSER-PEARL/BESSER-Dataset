





import java.util.List;
import java.util.ArrayList;

public class coursePages_CourseInstance  {

    private String courseYear;
    private String term;





    private coursePages_Evaluations coursepages_evaluations;




    private coursePages_Course coursepages_course;




    private coursePages_CourseWork coursepages_coursework;


    public coursePages_CourseInstance(
        String courseYear,        String term    ) {
        this.courseYear = courseYear;
        this.term = term;
    }


    public String getCourseyear() {
        return courseYear;
    }

    public void setCourseyear(String courseYear) {
        this.courseYear = courseYear;
    }
    public String getTerm() {
        return term;
    }

    public void setTerm(String term) {
        this.term = term;
    }

    public coursePages_Evaluations getCoursepages_evaluations() {
        return coursepages_evaluations;
    }

    public void setCoursepages_evaluations(coursePages_Evaluations coursepages_evaluations) {
        this.coursepages_evaluations = coursepages_evaluations;
    }
    public coursePages_Course getCoursepages_course() {
        return coursepages_course;
    }

    public void setCoursepages_course(coursePages_Course coursepages_course) {
        this.coursepages_course = coursepages_course;
    }
    public coursePages_CourseWork getCoursepages_coursework() {
        return coursepages_coursework;
    }

    public void setCoursepages_coursework(coursePages_CourseWork coursepages_coursework) {
        this.coursepages_coursework = coursepages_coursework;
    }

}