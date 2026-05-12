





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int Sex;
    private String Name;
    private String Address;
    private int RoomNo_;
    private int TelNO;
    private int Pid;
    private int Age;





    private Receptionist receptionist;


    public Patient(
        int Sex,        String Name,        String Address,        int RoomNo_,        int TelNO,        int Pid,        int Age    ) {
        this.Sex = Sex;
        this.Name = Name;
        this.Address = Address;
        this.RoomNo_ = RoomNo_;
        this.TelNO = TelNO;
        this.Pid = Pid;
        this.Age = Age;
    }


    public int getSex() {
        return Sex;
    }

    public void setSex(int Sex) {
        this.Sex = Sex;
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
    public int getRoomno_() {
        return RoomNo_;
    }

    public void setRoomno_(int RoomNo_) {
        this.RoomNo_ = RoomNo_;
    }
    public int getTelno() {
        return TelNO;
    }

    public void setTelno(int TelNO) {
        this.TelNO = TelNO;
    }
    public int getPid() {
        return Pid;
    }

    public void setPid(int Pid) {
        this.Pid = Pid;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}