





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private None course;
    private String name;





    private FacultyInfo facultyinfo;


    public Department(
        None course,        String name    ) {
        this.course = course;
        this.name = name;
    }


    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FacultyInfo getFacultyinfo() {
        return facultyinfo;
    }

    public void setFacultyinfo(FacultyInfo facultyinfo) {
        this.facultyinfo = facultyinfo;
    }

}