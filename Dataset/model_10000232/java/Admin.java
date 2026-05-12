





import java.util.List;
import java.util.ArrayList;

public class Admin  {






    private List<Employee_Interface> employee_interfaces;




    private List<Student> students;


    public Admin(
    ) {
        this.employee_interfaces = new ArrayList<>();
        this.students = new ArrayList<>();
    }

    public Admin(
        ArrayList<Employee_Interface> employee_interfaces,        ArrayList<Student> students    ) {
        this.employee_interfaces = employee_interfaces;
        this.students = students;
    }


    public List<Employee_Interface> getEmployee_interfaces() {
        return employee_interfaces;
    }

    public void addEmployee_interface(Employee_interface employee_interface) {
        this.employee_interfaces.add(employee_interface);
    }
    public List<Student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }

}