





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String ContactNo;
    private String Name;
    private String Email;
    private int DoctorID;



    public Doctor(
        String ContactNo,        String Name,        String Email,        int DoctorID    ) {
        this.ContactNo = ContactNo;
        this.Name = Name;
        this.Email = Email;
        this.DoctorID = DoctorID;
    }


    public String getContactno() {
        return ContactNo;
    }

    public void setContactno(String ContactNo) {
        this.ContactNo = ContactNo;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getDoctorid() {
        return DoctorID;
    }

    public void setDoctorid(int DoctorID) {
        this.DoctorID = DoctorID;
    }


}