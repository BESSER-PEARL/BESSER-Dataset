





import java.util.List;
import java.util.ArrayList;

public class ce_Employee  {

    private String address;
    private String department;
    private String name;



    public ce_Employee(
        String address,        String department,        String name    ) {
        this.address = address;
        this.department = department;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}