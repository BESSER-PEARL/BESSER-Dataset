





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private None course;
    private None teachers__;
    private None hod;
    private None students__;





    private List<Student> students;




    private List<Employee_Interface> employee_interfaces;


    public Department(
        None course,        None teachers__,        None hod,        None students__    ) {
        this.course = course;
        this.teachers__ = teachers__;
        this.hod = hod;
        this.students__ = students__;
        this.students = new ArrayList<>();
        this.employee_interfaces = new ArrayList<>();
    }

    public Department(
        None course,        None teachers__,        None hod,        None students__        ArrayList<Student> students,        ArrayList<Employee_Interface> employee_interfaces    ) {
        this.course = course;
        this.teachers__ = teachers__;
        this.hod = hod;
        this.students__ = students__;
        this.students = students;
        this.employee_interfaces = employee_interfaces;
    }

    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
    }
    public None getTeachers__() {
        return teachers__;
    }

    public void setTeachers__(None teachers__) {
        this.teachers__ = teachers__;
    }
    public None getHod() {
        return hod;
    }

    public void setHod(None hod) {
        this.hod = hod;
    }
    public None getStudents__() {
        return students__;
    }

    public void setStudents__(None students__) {
        this.students__ = students__;
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