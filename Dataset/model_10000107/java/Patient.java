





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String Address;
    private String Name;
    private int Id;
    private int PhNo_;
    private int Age;
    private int WardNo;





    private Doctor doctor;


    public Patient(
        String Address,        String Name,        int Id,        int PhNo_,        int Age,        int WardNo    ) {
        this.Address = Address;
        this.Name = Name;
        this.Id = Id;
        this.PhNo_ = PhNo_;
        this.Age = Age;
        this.WardNo = WardNo;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
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
    public int getWardno() {
        return WardNo;
    }

    public void setWardno(int WardNo) {
        this.WardNo = WardNo;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}