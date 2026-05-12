





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String ID;
    private String Name;





    private Admin admin;




    private Department department;




    private Access_Information access_information;


    public Student(
        String ID,        String Name    ) {
        this.ID = ID;
        this.Name = Name;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }
    public Access_Information getAccess_information() {
        return access_information;
    }

    public void setAccess_information(Access_Information access_information) {
        this.access_information = access_information;
    }

}