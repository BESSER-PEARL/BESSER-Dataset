





import java.util.List;
import java.util.ArrayList;

public class school_School  {

    private String address;
    private String name;





    private school_Course school_course;




    private List<school_Course> school_courses;




    private school_Year school_year;




    private List<school_Year> school_years;


    public school_School(
        String address,        String name    ) {
        this.address = address;
        this.name = name;
        this.school_courses = new ArrayList<>();
        this.school_years = new ArrayList<>();
    }

    public school_School(
        String address,        String name        ArrayList<school_Course> school_courses,        ArrayList<school_Year> school_years    ) {
        this.address = address;
        this.name = name;
        this.school_courses = school_courses;
        this.school_years = school_years;
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

    public school_Course getSchool_course() {
        return school_course;
    }

    public void setSchool_course(school_Course school_course) {
        this.school_course = school_course;
    }
    public List<school_Course> getSchool_courses() {
        return school_courses;
    }

    public void addSchool_course(School_course school_course) {
        this.school_courses.add(school_course);
    }
    public school_Year getSchool_year() {
        return school_year;
    }

    public void setSchool_year(school_Year school_year) {
        this.school_year = school_year;
    }
    public List<school_Year> getSchool_years() {
        return school_years;
    }

    public void addSchool_year(School_year school_year) {
        this.school_years.add(school_year);
    }

}