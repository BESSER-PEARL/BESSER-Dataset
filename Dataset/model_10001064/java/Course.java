





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String CourseNumber;
    private String CourseName;
    private None Course_Teacher;





    private Teacher teacher;




    private List<Student> students;


    public Course(
        String CourseNumber,        String CourseName,        None Course_Teacher    ) {
        this.CourseNumber = CourseNumber;
        this.CourseName = CourseName;
        this.Course_Teacher = Course_Teacher;
        this.students = new ArrayList<>();
    }

    public Course(
        String CourseNumber,        String CourseName,        None Course_Teacher        ArrayList<Student> students    ) {
        this.CourseNumber = CourseNumber;
        this.CourseName = CourseName;
        this.Course_Teacher = Course_Teacher;
        this.students = students;
    }

    public String getCoursenumber() {
        return CourseNumber;
    }

    public void setCoursenumber(String CourseNumber) {
        this.CourseNumber = CourseNumber;
    }
    public String getCoursename() {
        return CourseName;
    }

    public void setCoursename(String CourseName) {
        this.CourseName = CourseName;
    }
    public None getCourse_teacher() {
        return Course_Teacher;
    }

    public void setCourse_teacher(None Course_Teacher) {
        this.Course_Teacher = Course_Teacher;
    }

    public Teacher getTeacher() {
        return teacher;
    }

    public void setTeacher(Teacher teacher) {
        this.teacher = teacher;
    }
    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}