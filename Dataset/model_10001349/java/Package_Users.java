





import java.util.List;
import java.util.ArrayList;

public class Package_Users  {

    private int password;
    private int lastname;
    private int email;
    private int firstname;
    private int id;





    private Package_Employee package_employee;


    public Package_Users(
        int password,        int lastname,        int email,        int firstname,        int id    ) {
        this.password = password;
        this.lastname = lastname;
        this.email = email;
        this.firstname = firstname;
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
    public int getEmail() {
        return email;
    }

    public void setEmail(int email) {
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

    public Package_Employee getPackage_employee() {
        return package_employee;
    }

    public void setPackage_employee(Package_Employee package_employee) {
        this.package_employee = package_employee;
    }

}