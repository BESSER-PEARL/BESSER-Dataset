





import java.util.List;
import java.util.ArrayList;

public class Faculty  {






    private List<Student> students;




    private List<Employee_Interface> employee_interfaces;


    public Faculty(
    ) {
        this.students = new ArrayList<>();
        this.employee_interfaces = new ArrayList<>();
    }

    public Faculty(
        ArrayList<Student> students,        ArrayList<Employee_Interface> employee_interfaces    ) {
        this.students = students;
        this.employee_interfaces = employee_interfaces;
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