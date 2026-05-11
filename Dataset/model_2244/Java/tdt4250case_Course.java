





import java.util.List;
import java.util.ArrayList;

public class tdt4250case_Course  {

    private String name;
    private String code;
    private String content;
    private float credits;





    private List<tdt4250case_Course> tdt4250case_courses;




    private tdt4250case_Course tdt4250case_course;


    public tdt4250case_Course(
        String name,        String code,        String content,        float credits    ) {
        this.name = name;
        this.code = code;
        this.content = content;
        this.credits = credits;
        this.tdt4250case_courses = new ArrayList<>();
    }

    public tdt4250case_Course(
        String name,        String code,        String content,        float credits        ArrayList<tdt4250case_Course> tdt4250case_courses    ) {
        this.name = name;
        this.code = code;
        this.content = content;
        this.credits = credits;
        this.tdt4250case_courses = tdt4250case_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }

    public List<tdt4250case_Course> getTdt4250case_courses() {
        return tdt4250case_courses;
    }

    public void addTdt4250case_course(Tdt4250case_course tdt4250case_course) {
        this.tdt4250case_courses.add(tdt4250case_course);
    }
    public tdt4250case_Course getTdt4250case_course() {
        return tdt4250case_course;
    }

    public void setTdt4250case_course(tdt4250case_Course tdt4250case_course) {
        this.tdt4250case_course = tdt4250case_course;
    }

}