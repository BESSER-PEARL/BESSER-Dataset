





import java.util.List;
import java.util.ArrayList;

public class Package2_EmployeeSalary  {

    private String attribute;
    private String attribute2;





    private Package2_Employee package2_employee;


    public Package2_EmployeeSalary(
        String attribute,        String attribute2    ) {
        this.attribute = attribute;
        this.attribute2 = attribute2;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }

    public Package2_Employee getPackage2_employee() {
        return package2_employee;
    }

    public void setPackage2_employee(Package2_Employee package2_employee) {
        this.package2_employee = package2_employee;
    }

}