





import java.util.List;
import java.util.ArrayList;

public class Curso  {

    private String CourseNumber;
    private None Course_Teacher;
    private String CourseName;





    private Profesor profesor;




    private List<Student> students;


    public Curso(
        String CourseNumber,        None Course_Teacher,        String CourseName    ) {
        this.CourseNumber = CourseNumber;
        this.Course_Teacher = Course_Teacher;
        this.CourseName = CourseName;
        this.students = new ArrayList<>();
    }

    public Curso(
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

    public Profesor getProfesor() {
        return profesor;
    }

    public void setProfesor(Profesor profesor) {
        this.profesor = profesor;
    }
    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}