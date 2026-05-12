





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String name;
    private None course;





    private FacultyInfo facultyinfo;


    public Department(
        String name,        None course    ) {
        this.name = name;
        this.course = course;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
    }

    public FacultyInfo getFacultyinfo() {
        return facultyinfo;
    }

    public void setFacultyinfo(FacultyInfo facultyinfo) {
        this.facultyinfo = facultyinfo;
    }

}