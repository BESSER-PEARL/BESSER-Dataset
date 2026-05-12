





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String duration;
    private String subjects__;





    private Department department;


    public Course(
        String duration,        String subjects__    ) {
        this.duration = duration;
        this.subjects__ = subjects__;
    }


    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getSubjects__() {
        return subjects__;
    }

    public void setSubjects__(String subjects__) {
        this.subjects__ = subjects__;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}