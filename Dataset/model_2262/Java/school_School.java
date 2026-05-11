





import java.util.List;
import java.util.ArrayList;

public class school_School  {

    private String address;
    private String name;





    private List<school_Course> school_courses;




    private school_Course school_course;


    public school_School(
        String address,        String name    ) {
        this.address = address;
        this.name = name;
        this.school_courses = new ArrayList<>();
    }

    public school_School(
        String address,        String name        ArrayList<school_Course> school_courses    ) {
        this.address = address;
        this.name = name;
        this.school_courses = school_courses;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<school_Course> getSchool_courses() {
        return school_courses;
    }

    public void addSchool_course(School_course school_course) {
        this.school_courses.add(school_course);
    }
    public school_Course getSchool_course() {
        return school_course;
    }

    public void setSchool_course(school_Course school_course) {
        this.school_course = school_course;
    }

}