





import java.util.List;
import java.util.ArrayList;

public class employee_JobTitle  {

    private String title;





    private employee_Employee employee_employee;


    public employee_JobTitle(
        String title    ) {
        this.title = title;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}