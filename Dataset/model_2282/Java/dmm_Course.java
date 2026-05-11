





import java.util.List;
import java.util.ArrayList;

public class dmm_Course  {

    private String courseType;
    private String name;
    private int courseNumber;





    private dmm_Professor dmm_professor;




    private List<dmm_Course> dmm_courses;




    private dmm_Student dmm_student;


    public dmm_Course(
        String courseType,        String name,        int courseNumber    ) {
        this.courseType = courseType;
        this.name = name;
        this.courseNumber = courseNumber;
        this.dmm_courses = new ArrayList<>();
    }

    public dmm_Course(
        String courseType,        String name,        int courseNumber        ArrayList<dmm_Course> dmm_courses    ) {
        this.courseType = courseType;
        this.name = name;
        this.courseNumber = courseNumber;
        this.dmm_courses = dmm_courses;
    }

    public String getCoursetype() {
        return courseType;
    }

    public void setCoursetype(String courseType) {
        this.courseType = courseType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCoursenumber() {
        return courseNumber;
    }

    public void setCoursenumber(int courseNumber) {
        this.courseNumber = courseNumber;
    }

    public dmm_Professor getDmm_professor() {
        return dmm_professor;
    }

    public void setDmm_professor(dmm_Professor dmm_professor) {
        this.dmm_professor = dmm_professor;
    }
    public List<dmm_Course> getDmm_courses() {
        return dmm_courses;
    }

    public void addDmm_course(Dmm_course dmm_course) {
        this.dmm_courses.add(dmm_course);
    }
    public dmm_Student getDmm_student() {
        return dmm_student;
    }

    public void setDmm_student(dmm_Student dmm_student) {
        this.dmm_student = dmm_student;
    }

}