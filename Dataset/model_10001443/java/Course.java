





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private None subjects__;
    private String duration;





    private Department department;


    public Course(
        None subjects__,        String duration    ) {
        this.subjects__ = subjects__;
        this.duration = duration;
    }


    public None getSubjects__() {
        return subjects__;
    }

    public void setSubjects__(None subjects__) {
        this.subjects__ = subjects__;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}