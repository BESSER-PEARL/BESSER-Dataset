





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String PatientName;
    private String Address;
    private String Sex;
    private int PatientId;
    private int RoomNo;
    private int PhoneNo;
    private int Age;



    public Patient(
        String PatientName,        String Address,        String Sex,        int PatientId,        int RoomNo,        int PhoneNo,        int Age    ) {
        this.PatientName = PatientName;
        this.Address = Address;
        this.Sex = Sex;
        this.PatientId = PatientId;
        this.RoomNo = RoomNo;
        this.PhoneNo = PhoneNo;
        this.Age = Age;
    }


    public String getPatientname() {
        return PatientName;
    }

    public void setPatientname(String PatientName) {
        this.PatientName = PatientName;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getSex() {
        return Sex;
    }

    public void setSex(String Sex) {
        this.Sex = Sex;
    }
    public int getPatientid() {
        return PatientId;
    }

    public void setPatientid(int PatientId) {
        this.PatientId = PatientId;
    }
    public int getRoomno() {
        return RoomNo;
    }

    public void setRoomno(int RoomNo) {
        this.RoomNo = RoomNo;
    }
    public int getPhoneno() {
        return PhoneNo;
    }

    public void setPhoneno(int PhoneNo) {
        this.PhoneNo = PhoneNo;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }


}