





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Name;
    private String Department;
    private String Email;
    private String Address;
    private int DocId_;



    public Doctor(
        String Name,        String Department,        String Email,        String Address,        int DocId_    ) {
        this.Name = Name;
        this.Department = Department;
        this.Email = Email;
        this.Address = Address;
        this.DocId_ = DocId_;
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
    public int getDocid_() {
        return DocId_;
    }

    public void setDocid_(int DocId_) {
        this.DocId_ = DocId_;
    }


}