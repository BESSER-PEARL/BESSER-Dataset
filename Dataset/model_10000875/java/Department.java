





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String dept_name;
    private int dept_id;





    private List<student> students;




    private List<course> courses;


    public Department(
        String dept_name,        int dept_id    ) {
        this.dept_name = dept_name;
        this.dept_id = dept_id;
        this.students = new ArrayList<>();
        this.courses = new ArrayList<>();
    }

    public Department(
        String dept_name,        int dept_id        ArrayList<student> students,        ArrayList<course> courses    ) {
        this.dept_name = dept_name;
        this.dept_id = dept_id;
        this.students = students;
        this.courses = courses;
    }

    public String getDept_name() {
        return dept_name;
    }

    public void setDept_name(String dept_name) {
        this.dept_name = dept_name;
    }
    public int getDept_id() {
        return dept_id;
    }

    public void setDept_id(int dept_id) {
        this.dept_id = dept_id;
    }

    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<course> getCourses() {
        return courses;
    }

    public void addCourse(Course course) {
        this.courses.add(course);
    }

}