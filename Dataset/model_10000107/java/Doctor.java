





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Email;
    private String Address;
    private String Name;
    private String Department;
    private int DocId_;



    public Doctor(
        String Email,        String Address,        String Name,        String Department,        int DocId_    ) {
        this.Email = Email;
        this.Address = Address;
        this.Name = Name;
        this.Department = Department;
        this.DocId_ = DocId_;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String Department) {
        this.Department = Department;
    }
    public int getDocid_() {
        return DocId_;
    }

    public void setDocid_(int DocId_) {
        this.DocId_ = DocId_;
    }


}