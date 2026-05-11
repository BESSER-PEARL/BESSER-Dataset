





import java.util.List;
import java.util.ArrayList;

public class bz321765_EmployeePK  {

    private String id;
    private String firstName;
    private String lastName;





    private bz321765_Employee bz321765_employee;


    public bz321765_EmployeePK(
        String id,        String firstName,        String lastName    ) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public bz321765_Employee getBz321765_employee() {
        return bz321765_employee;
    }

    public void setBz321765_employee(bz321765_Employee bz321765_employee) {
        this.bz321765_employee = bz321765_employee;
    }

}