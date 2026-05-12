





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String PhoneNo;
    private int DepartmentID;
    private String Specialization;
    private String Name;
    private String Address;
    private String attribute;
    private int DoctorID;



    public Doctor(
        String PhoneNo,        int DepartmentID,        String Specialization,        String Name,        String Address,        String attribute,        int DoctorID    ) {
        this.PhoneNo = PhoneNo;
        this.DepartmentID = DepartmentID;
        this.Specialization = Specialization;
        this.Name = Name;
        this.Address = Address;
        this.attribute = attribute;
        this.DoctorID = DoctorID;
    }


    public String getPhoneno() {
        return PhoneNo;
    }

    public void setPhoneno(String PhoneNo) {
        this.PhoneNo = PhoneNo;
    }
    public int getDepartmentid() {
        return DepartmentID;
    }

    public void setDepartmentid(int DepartmentID) {
        this.DepartmentID = DepartmentID;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getDoctorid() {
        return DoctorID;
    }

    public void setDoctorid(int DoctorID) {
        this.DoctorID = DoctorID;
    }


}