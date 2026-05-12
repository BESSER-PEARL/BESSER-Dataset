





import java.util.List;
import java.util.ArrayList;

public class Access_Information  {






    private Employee_Interface employee_interface;




    private Student student;




    private Department department;


    public Access_Information(
    ) {
    }



    public Employee_Interface getEmployee_interface() {
        return employee_interface;
    }

    public void setEmployee_interface(Employee_Interface employee_interface) {
        this.employee_interface = employee_interface;
    }
    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}