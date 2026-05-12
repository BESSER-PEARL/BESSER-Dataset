





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int Age;
    private String Address;
    private int PhoneNo;
    private int Patientid;
    private String PatientName;
    private String Sex;
    private int RoomNo;



    public Patient(
        int Age,        String Address,        int PhoneNo,        int Patientid,        String PatientName,        String Sex,        int RoomNo    ) {
        this.Age = Age;
        this.Address = Address;
        this.PhoneNo = PhoneNo;
        this.Patientid = Patientid;
        this.PatientName = PatientName;
        this.Sex = Sex;
        this.RoomNo = RoomNo;
    }


    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getPhoneno() {
        return PhoneNo;
    }

    public void setPhoneno(int PhoneNo) {
        this.PhoneNo = PhoneNo;
    }
    public int getPatientid() {
        return Patientid;
    }

    public void setPatientid(int Patientid) {
        this.Patientid = Patientid;
    }
    public String getPatientname() {
        return PatientName;
    }

    public void setPatientname(String PatientName) {
        this.PatientName = PatientName;
    }
    public String getSex() {
        return Sex;
    }

    public void setSex(String Sex) {
        this.Sex = Sex;
    }
    public int getRoomno() {
        return RoomNo;
    }

    public void setRoomno(int RoomNo) {
        this.RoomNo = RoomNo;
    }


}