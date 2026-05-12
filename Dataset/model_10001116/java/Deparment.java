





import java.util.List;
import java.util.ArrayList;

public class Deparment  {

    private int Id;
    private int PhNo;
    private String Name;





    private Doctor doctor;


    public Deparment(
        int Id,        int PhNo,        String Name    ) {
        this.Id = Id;
        this.PhNo = PhNo;
        this.Name = Name;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public int getPhno() {
        return PhNo;
    }

    public void setPhno(int PhNo) {
        this.PhNo = PhNo;
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