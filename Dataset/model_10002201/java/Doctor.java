





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Dept;
    private String Specialization;
    private String Location;
    private int Doct_id;
    private int PhoneNo_;
    private String DocName;



    public Doctor(
        String Dept,        String Specialization,        String Location,        int Doct_id,        int PhoneNo_,        String DocName    ) {
        this.Dept = Dept;
        this.Specialization = Specialization;
        this.Location = Location;
        this.Doct_id = Doct_id;
        this.PhoneNo_ = PhoneNo_;
        this.DocName = DocName;
    }


    public String getDept() {
        return Dept;
    }

    public void setDept(String Dept) {
        this.Dept = Dept;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public int getDoct_id() {
        return Doct_id;
    }

    public void setDoct_id(int Doct_id) {
        this.Doct_id = Doct_id;
    }
    public int getPhoneno_() {
        return PhoneNo_;
    }

    public void setPhoneno_(int PhoneNo_) {
        this.PhoneNo_ = PhoneNo_;
    }
    public String getDocname() {
        return DocName;
    }

    public void setDocname(String DocName) {
        this.DocName = DocName;
    }


}