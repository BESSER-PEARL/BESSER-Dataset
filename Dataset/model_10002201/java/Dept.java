





import java.util.List;
import java.util.ArrayList;

public class Dept  {

    private String Name;
    private int Id;
    private int Doc_id;





    private Doctor doctor;


    public Dept(
        String Name,        int Id,        int Doc_id    ) {
        this.Name = Name;
        this.Id = Id;
        this.Doc_id = Doc_id;
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
    public int getDoc_id() {
        return Doc_id;
    }

    public void setDoc_id(int Doc_id) {
        this.Doc_id = Doc_id;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}