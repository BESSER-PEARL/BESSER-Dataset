





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int PatID;
    private int Age;
    private int RoomNo;
    private String Address;
    private String Gender;
    private int TelNo;
    private String Name;





    private Doctor doctor;


    public Patient(
        int PatID,        int Age,        int RoomNo,        String Address,        String Gender,        int TelNo,        String Name    ) {
        this.PatID = PatID;
        this.Age = Age;
        this.RoomNo = RoomNo;
        this.Address = Address;
        this.Gender = Gender;
        this.TelNo = TelNo;
        this.Name = Name;
    }


    public int getPatid() {
        return PatID;
    }

    public void setPatid(int PatID) {
        this.PatID = PatID;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public int getRoomno() {
        return RoomNo;
    }

    public void setRoomno(int RoomNo) {
        this.RoomNo = RoomNo;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public int getTelno() {
        return TelNo;
    }

    public void setTelno(int TelNo) {
        this.TelNo = TelNo;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}