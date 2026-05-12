





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String PhoneNumber;
    private String Email;
    private String RId;
    private String DateOfBirth;
    private int UserId;
    private String ReceptionistName;
    private int ReceptionistId;



    public Receptionist(
        String PhoneNumber,        String Email,        String RId,        String DateOfBirth,        int UserId,        String ReceptionistName,        int ReceptionistId    ) {
        this.PhoneNumber = PhoneNumber;
        this.Email = Email;
        this.RId = RId;
        this.DateOfBirth = DateOfBirth;
        this.UserId = UserId;
        this.ReceptionistName = ReceptionistName;
        this.ReceptionistId = ReceptionistId;
    }


    public String getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(String PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getRid() {
        return RId;
    }

    public void setRid(String RId) {
        this.RId = RId;
    }
    public String getDateofbirth() {
        return DateOfBirth;
    }

    public void setDateofbirth(String DateOfBirth) {
        this.DateOfBirth = DateOfBirth;
    }
    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }
    public String getReceptionistname() {
        return ReceptionistName;
    }

    public void setReceptionistname(String ReceptionistName) {
        this.ReceptionistName = ReceptionistName;
    }
    public int getReceptionistid() {
        return ReceptionistId;
    }

    public void setReceptionistid(int ReceptionistId) {
        this.ReceptionistId = ReceptionistId;
    }


}