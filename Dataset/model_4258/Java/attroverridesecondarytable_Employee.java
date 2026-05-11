





import java.util.List;
import java.util.ArrayList;

public class attroverridesecondarytable_Employee extends Person {

    private String employeeNumber;





    private attroverridesecondarytable_Address attroverridesecondarytable_address;


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

    public attroverridesecondarytable_Address getAttroverridesecondarytable_address() {
        return attroverridesecondarytable_address;
    }

    public void setAttroverridesecondarytable_address(attroverridesecondarytable_Address attroverridesecondarytable_address) {
        this.attroverridesecondarytable_address = attroverridesecondarytable_address;
    }

}