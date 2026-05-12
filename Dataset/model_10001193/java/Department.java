





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private int dept_id;
    private String dept_name;





    private List<course> courses;




    private List<student> students;


    public Department(
        int dept_id,        String dept_name    ) {
        this.dept_id = dept_id;
        this.dept_name = dept_name;
        this.courses = new ArrayList<>();
        this.students = new ArrayList<>();
    }

    public Department(
        int dept_id,        String dept_name        ArrayList<course> courses,        ArrayList<student> students    ) {
        this.dept_id = dept_id;
        this.dept_name = dept_name;
        this.courses = courses;
        this.students = students;
    }

    public int getDept_id() {
        return dept_id;
    }

    public void setDept_id(int dept_id) {
        this.dept_id = dept_id;
    }
    public String getDept_name() {
        return dept_name;
    }

    public void setDept_name(String dept_name) {
        this.dept_name = dept_name;
    }

    public List<course> getCourses() {
        return courses;
    }

    public void addCourse(Course course) {
        this.courses.add(course);
    }
    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}