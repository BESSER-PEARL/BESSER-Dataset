





import java.util.List;
import java.util.ArrayList;

public class Package_Users  {

    private int firstname;
    private int email;
    private int id;
    private int password;
    private int lastname;





    private Package_Employee package_employee;


    public Package_Users(
        int firstname,        int email,        int id,        int password,        int lastname    ) {
        this.firstname = firstname;
        this.email = email;
        this.id = id;
        this.password = password;
        this.lastname = lastname;
    }


    public int getFirstname() {
        return firstname;
    }

    public void setFirstname(int firstname) {
        this.firstname = firstname;
    }
    public int getEmail() {
        return email;
    }

    public void setEmail(int email) {
        this.email = email;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }
    public int getLastname() {
        return lastname;
    }

    public void setLastname(int lastname) {
        this.lastname = lastname;
    }

    public Package_Employee getPackage_employee() {
        return package_employee;
    }

    public void setPackage_employee(Package_Employee package_employee) {
        this.package_employee = package_employee;
    }

}