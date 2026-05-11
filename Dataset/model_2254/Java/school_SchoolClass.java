





import java.util.List;
import java.util.ArrayList;

public class school_SchoolClass  {

    private String code;





    private school_Teacher school_teacher;




    private List<school_Course> school_courses;




    private school_Teacher school_teacher;




    private school_Student school_student;




    private List<school_Student> school_students;




    private school_Course school_course;




    private List<school_Course> school_courses;


    public school_SchoolClass(
        String code    ) {
        this.code = code;
        this.school_courses = new ArrayList<>();
        this.school_students = new ArrayList<>();
        this.school_courses = new ArrayList<>();
    }

    public school_SchoolClass(
        String code        ArrayList<school_Course> school_courses,        ArrayList<school_Student> school_students,        ArrayList<school_Course> school_courses    ) {
        this.code = code;
        this.school_courses = school_courses;
        this.school_students = school_students;
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
    public school_Student getSchool_student() {
        return school_student;
    }

    public void setSchool_student(school_Student school_student) {
        this.school_student = school_student;
    }
    public List<school_Student> getSchool_students() {
        return school_students;
    }

    public void addSchool_student(School_student school_student) {
        this.school_students.add(school_student);
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

}