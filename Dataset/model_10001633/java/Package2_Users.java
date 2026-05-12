





import java.util.List;
import java.util.ArrayList;

public class Package2_Users  {

    private int lastname;
    private int password;
    private int id;
    private int email;
    private int firstname;





    private Package2_Employee package2_employee;


    public Package2_Users(
        int lastname,        int password,        int id,        int email,        int firstname    ) {
        this.lastname = lastname;
        this.password = password;
        this.id = id;
        this.email = email;
        this.firstname = firstname;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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

    public Package2_Employee getPackage2_employee() {
        return package2_employee;
    }

    public void setPackage2_employee(Package2_Employee package2_employee) {
        this.package2_employee = package2_employee;
    }

}