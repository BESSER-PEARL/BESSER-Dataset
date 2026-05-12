





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private None Course_Teacher;
    private String CourseName;
    private String CourseNumber;





    private List<Student> students;




    private Teacher teacher;


    public Course(
        None Course_Teacher,        String CourseName,        String CourseNumber    ) {
        this.Course_Teacher = Course_Teacher;
        this.CourseName = CourseName;
        this.CourseNumber = CourseNumber;
        this.students = new ArrayList<>();
    }

    public Course(
        None Course_Teacher,        String CourseName,        String CourseNumber        ArrayList<Student> students    ) {
        this.Course_Teacher = Course_Teacher;
        this.CourseName = CourseName;
        this.CourseNumber = CourseNumber;
        this.students = students;
    }

    public None getCourse_teacher() {
        return Course_Teacher;
    }

    public void setCourse_teacher(None Course_Teacher) {
        this.Course_Teacher = Course_Teacher;
    }
    public String getCoursename() {
        return CourseName;
    }

    public void setCoursename(String CourseName) {
        this.CourseName = CourseName;
    }
    public String getCoursenumber() {
        return CourseNumber;
    }

    public void setCoursenumber(String CourseNumber) {
        this.CourseNumber = CourseNumber;
    }

    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public Teacher getTeacher() {
        return teacher;
    }

    public void setTeacher(Teacher teacher) {
        this.teacher = teacher;
    }

}