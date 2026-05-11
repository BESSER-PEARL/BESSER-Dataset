





import java.util.List;
import java.util.ArrayList;

public class tdt4250case_Studyprogram  {

    private String code;





    private tdt4250case_Course tdt4250case_course;




    private List<tdt4250case_Course> tdt4250case_courses;


    public tdt4250case_Studyprogram(
        String code    ) {
        this.code = code;
        this.tdt4250case_courses = new ArrayList<>();
    }

    public tdt4250case_Studyprogram(
        String code        ArrayList<tdt4250case_Course> tdt4250case_courses    ) {
        this.code = code;
        this.tdt4250case_courses = tdt4250case_courses;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public tdt4250case_Course getTdt4250case_course() {
        return tdt4250case_course;
    }

    public void setTdt4250case_course(tdt4250case_Course tdt4250case_course) {
        this.tdt4250case_course = tdt4250case_course;
    }
    public List<tdt4250case_Course> getTdt4250case_courses() {
        return tdt4250case_courses;
    }

    public void addTdt4250case_course(Tdt4250case_course tdt4250case_course) {
        this.tdt4250case_courses.add(tdt4250case_course);
    }

}