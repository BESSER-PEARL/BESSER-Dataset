




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class employee_EmploymentPeriod  {

    private LocalDate startDate;
    private LocalDate endDate;
    private String id;





    private employee_Employee employee_employee;


    public employee_EmploymentPeriod(
        LocalDate startDate,        LocalDate endDate,        String id    ) {
        this.startDate = startDate;
        this.endDate = endDate;
        this.id = id;
    }


    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}