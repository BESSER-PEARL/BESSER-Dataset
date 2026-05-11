





import java.util.List;
import java.util.ArrayList;

public class attroverridesecondarytable_Employee extends Person {

    private String employeeNumber;



    public attroverridesecondarytable_Employee(
        String employeeNumber    ) {
        super(
        );
        this.employeeNumber = employeeNumber;
    }


    public String getEmployeenumber() {
        return employeeNumber;
    }

    public void setEmployeenumber(String employeeNumber) {
        this.employeeNumber = employeeNumber;
    }


}