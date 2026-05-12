





import java.util.List;
import java.util.ArrayList;

public class Package_Users  {

    private int password;
    private int email;
    private int id;
    private int lastname;
    private int firstname;





    private Package_Employee package_employee;


    public Package_Users(
        int password,        int email,        int id,        int lastname,        int firstname    ) {
        this.password = password;
        this.email = email;
        this.id = id;
        this.lastname = lastname;
        this.firstname = firstname;
    }


    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
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
    public int getLastname() {
        return lastname;
    }

    public void setLastname(int lastname) {
        this.lastname = lastname;
    }
    public int getFirstname() {
        return firstname;
    }

    public void setFirstname(int firstname) {
        this.firstname = firstname;
    }

    public Package_Employee getPackage_employee() {
        return package_employee;
    }

    public void setPackage_employee(Package_Employee package_employee) {
        this.package_employee = package_employee;
    }

}