





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int TelNo;
    private int Rno;
    private int Name;
    private String Sex;
    private String Address;
    private int Age;
    private int id;



    public Patient(
        int TelNo,        int Rno,        int Name,        String Sex,        String Address,        int Age,        int id    ) {
        this.TelNo = TelNo;
        this.Rno = Rno;
        this.Name = Name;
        this.Sex = Sex;
        this.Address = Address;
        this.Age = Age;
        this.id = id;
    }


    public int getTelno() {
        return TelNo;
    }

    public void setTelno(int TelNo) {
        this.TelNo = TelNo;
    }
    public int getRno() {
        return Rno;
    }

    public void setRno(int Rno) {
        this.Rno = Rno;
    }
    public int getName() {
        return Name;
    }

    public void setName(int Name) {
        this.Name = Name;
    }
    public String getSex() {
        return Sex;
    }

    public void setSex(String Sex) {
        this.Sex = Sex;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}