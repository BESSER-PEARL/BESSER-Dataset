





import java.util.List;
import java.util.ArrayList;

public class tdt4250case_CourseWork  {

    private String type;
    private int hours;





    private tdt4250case_Course tdt4250case_course;


    public tdt4250case_CourseWork(
        String type,        int hours    ) {
        this.type = type;
        this.hours = hours;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getHours() {
        return hours;
    }

    public void setHours(int hours) {
        this.hours = hours;
    }

    public tdt4250case_Course getTdt4250case_course() {
        return tdt4250case_course;
    }

    public void setTdt4250case_course(tdt4250case_Course tdt4250case_course) {
        this.tdt4250case_course = tdt4250case_course;
    }

}