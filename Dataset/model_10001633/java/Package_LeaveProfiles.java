





import java.util.List;
import java.util.ArrayList;

public class Package_LeaveProfiles  {

    private String attribute;
    private String attribute2;





    private Package_Employee package_employee;


    public Package_LeaveProfiles(
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

    public Package_Employee getPackage_employee() {
        return package_employee;
    }

    public void setPackage_employee(Package_Employee package_employee) {
        this.package_employee = package_employee;
    }

}