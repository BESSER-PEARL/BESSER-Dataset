





import java.util.List;
import java.util.ArrayList;

public class employee_EmailAddress  {

    private String name;
    private String address;
    private int id;





    private employee_Employee employee_employee;


    public employee_EmailAddress(
        String name,        String address,        int id    ) {
        this.name = name;
        this.address = address;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}