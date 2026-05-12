





import java.util.List;
import java.util.ArrayList;

public class Access_Information  {






    private Department department;




    private Student student;




    private Employee_Interface employee_interface;


    public Access_Information(
    ) {
    }



    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }
    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public Employee_Interface getEmployee_interface() {
        return employee_interface;
    }

    public void setEmployee_interface(Employee_Interface employee_interface) {
        this.employee_interface = employee_interface;
    }

}