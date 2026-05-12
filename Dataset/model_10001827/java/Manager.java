





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String allowance;
    private String employeeList;



    public Manager(
        String allowance,        String employeeList    ) {
        this.allowance = allowance;
        this.employeeList = employeeList;
    }


    public String getAllowance() {
        return allowance;
    }

    public void setAllowance(String allowance) {
        this.allowance = allowance;
    }
    public String getEmployeelist() {
        return employeeList;
    }

    public void setEmployeelist(String employeeList) {
        this.employeeList = employeeList;
    }


}