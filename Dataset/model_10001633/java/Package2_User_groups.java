





import java.util.List;
import java.util.ArrayList;

public class Package2_User_groups  {

    private String attribute;
    private String attribute3;
    private String attribute2;





    private List<Package2_Employee> package2_employees;


    public Package2_User_groups(
        String attribute,        String attribute3,        String attribute2    ) {
        this.attribute = attribute;
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
        this.package2_employees = new ArrayList<>();
    }

    public Package2_User_groups(
        String attribute,        String attribute3,        String attribute2        ArrayList<Package2_Employee> package2_employees    ) {
        this.attribute = attribute;
        this.attribute3 = attribute3;
        this.attribute2 = attribute2;
        this.package2_employees = package2_employees;
    }

    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
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

    public List<Package2_Employee> getPackage2_employees() {
        return package2_employees;
    }

    public void addPackage2_employee(Package2_employee package2_employee) {
        this.package2_employees.add(package2_employee);
    }

}