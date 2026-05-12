





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private None students__;
    private None hod;
    private None teachers__;
    private None course;





    private List<Student> students;




    private List<Employee_Interface> employee_interfaces;


    public Department(
        None students__,        None hod,        None teachers__,        None course    ) {
        this.students__ = students__;
        this.hod = hod;
        this.teachers__ = teachers__;
        this.course = course;
        this.students = new ArrayList<>();
        this.employee_interfaces = new ArrayList<>();
    }

    public Department(
        None students__,        None hod,        None teachers__,        None course        ArrayList<Student> students,        ArrayList<Employee_Interface> employee_interfaces    ) {
        this.students__ = students__;
        this.hod = hod;
        this.teachers__ = teachers__;
        this.course = course;
        this.students = students;
        this.employee_interfaces = employee_interfaces;
    }

    public None getStudents__() {
        return students__;
    }

    public void setStudents__(None students__) {
        this.students__ = students__;
    }
    public None getHod() {
        return hod;
    }

    public void setHod(None hod) {
        this.hod = hod;
    }
    public None getTeachers__() {
        return teachers__;
    }

    public void setTeachers__(None teachers__) {
        this.teachers__ = teachers__;
    }
    public None getCourse() {
        return course;
    }

    public void setCourse(None course) {
        this.course = course;
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