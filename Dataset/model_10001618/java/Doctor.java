





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Department;
    private int Phone;
    private String Name;
    private int DocID;
    private String Specialization;
    private String Address;



    public Doctor(
        String Department,        int Phone,        String Name,        int DocID,        String Specialization,        String Address    ) {
        this.Department = Department;
        this.Phone = Phone;
        this.Name = Name;
        this.DocID = DocID;
        this.Specialization = Specialization;
        this.Address = Address;
    }


    public String getDepartment() {
        return Department;
    }

    public void setDepartment(String Department) {
        this.Department = Department;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getDocid() {
        return DocID;
    }

    public void setDocid(int DocID) {
        this.DocID = DocID;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}