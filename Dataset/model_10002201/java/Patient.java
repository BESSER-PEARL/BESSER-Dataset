





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int Patient_id;
    private int RoomNo_;
    private String Address;
    private int PhoneNo_;
    private String Name;
    private String Sex;
    private int Age;





    private Doctor doctor;




    private Receptionist receptionist;




    private Bill bill;




    private Rooms rooms;


    public Patient(
        int Patient_id,        int RoomNo_,        String Address,        int PhoneNo_,        String Name,        String Sex,        int Age    ) {
        this.Patient_id = Patient_id;
        this.RoomNo_ = RoomNo_;
        this.Address = Address;
        this.PhoneNo_ = PhoneNo_;
        this.Name = Name;
        this.Sex = Sex;
        this.Age = Age;
    }


    public int getPatient_id() {
        return Patient_id;
    }

    public void setPatient_id(int Patient_id) {
        this.Patient_id = Patient_id;
    }
    public int getRoomno_() {
        return RoomNo_;
    }

    public void setRoomno_(int RoomNo_) {
        this.RoomNo_ = RoomNo_;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getPhoneno_() {
        return PhoneNo_;
    }

    public void setPhoneno_(int PhoneNo_) {
        this.PhoneNo_ = PhoneNo_;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getSex() {
        return Sex;
    }

    public void setSex(String Sex) {
        this.Sex = Sex;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }
    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }
    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }
    public Rooms getRooms() {
        return rooms;
    }

    public void setRooms(Rooms rooms) {
        this.rooms = rooms;
    }

}