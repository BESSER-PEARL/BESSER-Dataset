





import java.util.List;
import java.util.ArrayList;

public class school_Teacher  {

    private String name;





    private school_Course school_course;




    private List<school_Course> school_courses;




    private school_School school_school;




    private school_School school_school;


    public school_Teacher(
        String name    ) {
        this.name = name;
        this.school_courses = new ArrayList<>();
    }

    public school_Teacher(
        String name        ArrayList<school_Course> school_courses    ) {
        this.name = name;
        this.school_courses = school_courses;
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
    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }
    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }

}