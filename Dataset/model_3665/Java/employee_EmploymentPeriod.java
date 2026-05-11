




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class employee_EmploymentPeriod  {

    private LocalDate endDate;
    private LocalDate startDate;
    private int id;





    private employee_Employee employee_employee;


    public employee_EmploymentPeriod(
        LocalDate endDate,        LocalDate startDate,        int id    ) {
        this.endDate = endDate;
        this.startDate = startDate;
        this.id = id;
    }


    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}