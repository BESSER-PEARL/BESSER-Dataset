





import java.util.List;
import java.util.ArrayList;

public class Package_Users  {

    private int firstname;
    private int id;
    private int lastname;
    private int password;
    private int email;





    private Package_Employee package_employee;


    public Package_Users(
        int firstname,        int id,        int lastname,        int password,        int email    ) {
        this.firstname = firstname;
        this.id = id;
        this.lastname = lastname;
        this.password = password;
        this.email = email;
    }


    public int getFirstname() {
        return firstname;
    }

    public void setFirstname(int firstname) {
        this.firstname = firstname;
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

    public Package_Employee getPackage_employee() {
        return package_employee;
    }

    public void setPackage_employee(Package_Employee package_employee) {
        this.package_employee = package_employee;
    }

}