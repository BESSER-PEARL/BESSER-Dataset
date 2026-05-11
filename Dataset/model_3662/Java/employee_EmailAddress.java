





import java.util.List;
import java.util.ArrayList;

public class employee_EmailAddress  {

    private String id;
    private String address;
    private String name;





    private employee_Employee employee_employee;


    public employee_EmailAddress(
        String id,        String address,        String name    ) {
        this.id = id;
        this.address = address;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}