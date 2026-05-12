





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String Address;
    private int WardNo;
    private String Name;
    private int PhNo_;
    private int Age;
    private int Id;





    private Doctor doctor;


    public Patient(
        String Address,        int WardNo,        String Name,        int PhNo_,        int Age,        int Id    ) {
        this.Address = Address;
        this.WardNo = WardNo;
        this.Name = Name;
        this.PhNo_ = PhNo_;
        this.Age = Age;
        this.Id = Id;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
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
    public int getPhno_() {
        return PhNo_;
    }

    public void setPhno_(int PhNo_) {
        this.PhNo_ = PhNo_;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}