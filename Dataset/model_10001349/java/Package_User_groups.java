





import java.util.List;
import java.util.ArrayList;

public class Package_User_groups  {

    private String attribute3;
    private String attribute2;
    private String attribute;





    private List<Package_Employee> package_employees;


    public Package_User_groups(
        String attribute3,        String attribute2,        String attribute    ) {
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
        this.attribute = attribute;
        this.package_employees = new ArrayList<>();
    }

    public Package_User_groups(
        String attribute3,        String attribute2,        String attribute        ArrayList<Package_Employee> package_employees    ) {
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
        this.attribute = attribute;
        this.package_employees = package_employees;
    }

    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public List<Package_Employee> getPackage_employees() {
        return package_employees;
    }

    public void addPackage_employee(Package_employee package_employee) {
        this.package_employees.add(package_employee);
    }

}