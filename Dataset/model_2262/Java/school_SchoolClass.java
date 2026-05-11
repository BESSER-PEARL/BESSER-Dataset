





import java.util.List;
import java.util.ArrayList;

public class school_SchoolClass  {

    private String code;





    private school_Teacher school_teacher;




    private school_Course school_course;




    private List<school_Course> school_courses;




    private school_Teacher school_teacher;


    public school_SchoolClass(
        String code    ) {
        this.code = code;
        this.school_courses = new ArrayList<>();
    }

    public school_SchoolClass(
        String code        ArrayList<school_Course> school_courses    ) {
        this.code = code;
        this.school_courses = school_courses;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public school_Teacher getSchool_teacher() {
        return school_teacher;
    }

    public void setSchool_teacher(school_Teacher school_teacher) {
        this.school_teacher = school_teacher;
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
    public school_Teacher getSchool_teacher() {
        return school_teacher;
    }

    public void setSchool_teacher(school_Teacher school_teacher) {
        this.school_teacher = school_teacher;
    }

}