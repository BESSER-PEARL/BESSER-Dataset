





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int WardNo;
    private String Name;
    private String Gender;
    private String Age;
    private String Address;
    private int PatientID;





    private Doctor doctor;


    public Patient(
        int WardNo,        String Name,        String Gender,        String Age,        String Address,        int PatientID    ) {
        this.WardNo = WardNo;
        this.Name = Name;
        this.Gender = Gender;
        this.Age = Age;
        this.Address = Address;
        this.PatientID = PatientID;
    }


    public int getWardno() {
        return WardNo;
    }

    public void setWardno(int WardNo) {
        this.WardNo = WardNo;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public String getAge() {
        return Age;
    }

    public void setAge(String Age) {
        this.Age = Age;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getPatientid() {
        return PatientID;
    }

    public void setPatientid(int PatientID) {
        this.PatientID = PatientID;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}