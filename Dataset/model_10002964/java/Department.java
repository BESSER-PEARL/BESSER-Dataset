





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private None teachers__;
    private String courseID;
    private None course;
    private None students__;
    private String CourseName;





    private List<Student> students;




    private List<Employee_Interface> employee_interfaces;


    public Department(
        None teachers__,        String courseID,        None course,        None students__,        String CourseName    ) {
        this.teachers__ = teachers__;
        this.courseID = courseID;
        this.course = course;
        this.students__ = students__;
        this.CourseName = CourseName;
        this.students = new ArrayList<>();
        this.employee_interfaces = new ArrayList<>();
    }

    public Department(
        None teachers__,        String courseID,        None course,        None students__,        String CourseName        ArrayList<Student> students,        ArrayList<Employee_Interface> employee_interfaces    ) {
        this.teachers__ = teachers__;
        this.courseID = courseID;
        this.course = course;
        this.students__ = students__;
        this.CourseName = CourseName;
        this.students = students;
        this.employee_interfaces = employee_interfaces;
    }

    public None getTeachers__() {
        return teachers__;
    }

    public void setTeachers__(None teachers__) {
        this.teachers__ = teachers__;
    }
    public String getCourseid() {
        return courseID;
    }

    public void setCourseid(String courseID) {
        this.courseID = courseID;
    }
    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
    }
    public None getStudents__() {
        return students__;
    }

    public void setStudents__(None students__) {
        this.students__ = students__;
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
    public List<Employee_Interface> getEmployee_interfaces() {
        return employee_interfaces;
    }

    public void addEmployee_interface(Employee_interface employee_interface) {
        this.employee_interfaces.add(employee_interface);
    }

}