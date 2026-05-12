





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String Skills___Requirement;
    private String Email;
    private String Date;
    private String Applied_Position;
    private String Position_Type;
    private String Name;
    private String Phone;
    private String Address;





    private Applicant applicant;




    private Admin admin;


    public Registration(
        String Skills___Requirement,        String Email,        String Date,        String Applied_Position,        String Position_Type,        String Name,        String Phone,        String Address    ) {
        this.Skills___Requirement = Skills___Requirement;
        this.Email = Email;
        this.Date = Date;
        this.Applied_Position = Applied_Position;
        this.Position_Type = Position_Type;
        this.Name = Name;
        this.Phone = Phone;
        this.Address = Address;
    }


    public String getSkills___requirement() {
        return Skills___Requirement;
    }

    public void setSkills___requirement(String Skills___Requirement) {
        this.Skills___Requirement = Skills___Requirement;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getApplied_position() {
        return Applied_Position;
    }

    public void setApplied_position(String Applied_Position) {
        this.Applied_Position = Applied_Position;
    }
    public String getPosition_type() {
        return Position_Type;
    }

    public void setPosition_type(String Position_Type) {
        this.Position_Type = Position_Type;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Applicant getApplicant() {
        return applicant;
    }

    public void setApplicant(Applicant applicant) {
        this.applicant = applicant;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}