





import java.util.List;
import java.util.ArrayList;

public class course_Course  {

    private String name;
    private String content;
    private String code;
    private float credits;





    private course_Department course_department;




    private course_Course course_course;




    private course_Department course_department;




    private List<course_Course> course_courses;


    public course_Course(
        String name,        String content,        String code,        float credits    ) {
        this.name = name;
        this.content = content;
        this.code = code;
        this.credits = credits;
        this.course_courses = new ArrayList<>();
    }

    public course_Course(
        String name,        String content,        String code,        float credits        ArrayList<course_Course> course_courses    ) {
        this.name = name;
        this.content = content;
        this.code = code;
        this.credits = credits;
        this.course_courses = course_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }

    public course_Department getCourse_department() {
        return course_department;
    }

    public void setCourse_department(course_Department course_department) {
        this.course_department = course_department;
    }
    public course_Course getCourse_course() {
        return course_course;
    }

    public void setCourse_course(course_Course course_course) {
        this.course_course = course_course;
    }
    public course_Department getCourse_department() {
        return course_department;
    }

    public void setCourse_department(course_Department course_department) {
        this.course_department = course_department;
    }
    public List<course_Course> getCourse_courses() {
        return course_courses;
    }

    public void addCourse_course(Course_course course_course) {
        this.course_courses.add(course_course);
    }

}