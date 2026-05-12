





import java.util.List;
import java.util.ArrayList;

public class Courses  {

    private int credithour;
    private int coursecode;
    private String _attr;
    private String courseName;
    private int courseId;





    private List<Student> students;




    private List<student> students;


    public Courses(
        int credithour,        int coursecode,        String _attr,        String courseName,        int courseId    ) {
        this.credithour = credithour;
        this.coursecode = coursecode;
        this._attr = _attr;
        this.courseName = courseName;
        this.courseId = courseId;
        this.students = new ArrayList<>();
        this.students = new ArrayList<>();
    }

    public Courses(
        int credithour,        int coursecode,        String _attr,        String courseName,        int courseId        ArrayList<Student> students,        ArrayList<student> students    ) {
        this.credithour = credithour;
        this.coursecode = coursecode;
        this._attr = _attr;
        this.courseName = courseName;
        this.courseId = courseId;
        this.students = students;
        this.students = students;
    }

    public int getCredithour() {
        return credithour;
    }

    public void setCredithour(int credithour) {
        this.credithour = credithour;
    }
    public int getCoursecode() {
        return coursecode;
    }

    public void setCoursecode(int coursecode) {
        this.coursecode = coursecode;
    }
    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }
    public String getCoursename() {
        return courseName;
    }

    public void setCoursename(String courseName) {
        this.courseName = courseName;
    }
    public int getCourseid() {
        return courseId;
    }

    public void setCourseid(int courseId) {
        this.courseId = courseId;
    }

    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}