





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String CourseNumber;
    private None Course_Teacher;
    private String CourseName;





    private List<Student> students;




    private Teacher teacher;


    public Course(
        String CourseNumber,        None Course_Teacher,        String CourseName    ) {
        this.CourseNumber = CourseNumber;
        this.Course_Teacher = Course_Teacher;
        this.CourseName = CourseName;
        this.students = new ArrayList<>();
    }

    public Course(
        String CourseNumber,        None Course_Teacher,        String CourseName        ArrayList<Student> students    ) {
        this.CourseNumber = CourseNumber;
        this.Course_Teacher = Course_Teacher;
        this.CourseName = CourseName;
        this.students = students;
    }

    public String getCoursenumber() {
        return CourseNumber;
    }

    public void setCoursenumber(String CourseNumber) {
        this.CourseNumber = CourseNumber;
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