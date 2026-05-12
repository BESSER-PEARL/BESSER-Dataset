





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private None teachers__;
    private String hod;
    private None course;
    private None students__;





    private List<Student> students;




    private List<Employee_Interface> employee_interfaces;


    public Department(
        None teachers__,        String hod,        None course,        None students__    ) {
        this.teachers__ = teachers__;
        this.hod = hod;
        this.course = course;
        this.students__ = students__;
        this.students = new ArrayList<>();
        this.employee_interfaces = new ArrayList<>();
    }

    public Department(
        None teachers__,        String hod,        None course,        None students__        ArrayList<Student> students,        ArrayList<Employee_Interface> employee_interfaces    ) {
        this.teachers__ = teachers__;
        this.hod = hod;
        this.course = course;
        this.students__ = students__;
        this.students = students;
        this.employee_interfaces = employee_interfaces;
    }

    public None getTeachers__() {
        return teachers__;
    }

    public void setTeachers__(None teachers__) {
        this.teachers__ = teachers__;
    }
    public String getHod() {
        return hod;
    }

    public void setHod(String hod) {
        this.hod = hod;
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