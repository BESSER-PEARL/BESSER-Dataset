





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Department;
    private int PhoneNumber;
    private String DocID;
    private String Address;
    private int Specialization;
    private String Name;



    public Doctor(
        String Department,        int PhoneNumber,        String DocID,        String Address,        int Specialization,        String Name    ) {
        this.Department = Department;
        this.PhoneNumber = PhoneNumber;
        this.DocID = DocID;
        this.Address = Address;
        this.Specialization = Specialization;
        this.Name = Name;
    }


    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String Department) {
        this.Department = Department;
    }
    public int getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(int PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }
    public String getDocid() {
        return DocID;
    }

    public void setDocid(String DocID) {
        this.DocID = DocID;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(int Specialization) {
        this.Specialization = Specialization;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}