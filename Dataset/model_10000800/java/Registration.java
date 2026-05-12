





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String Date;
    private String Position_Type;
    private String Skills___Requirement;
    private String Email;
    private String Address;
    private String Name;
    private String Applied_Position;
    private String Phone;





    private Applicant applicant;




    private Admin admin;




    private New_Employee new_employee;


    public Registration(
        String Date,        String Position_Type,        String Skills___Requirement,        String Email,        String Address,        String Name,        String Applied_Position,        String Phone    ) {
        this.Date = Date;
        this.Position_Type = Position_Type;
        this.Skills___Requirement = Skills___Requirement;
        this.Email = Email;
        this.Address = Address;
        this.Name = Name;
        this.Applied_Position = Applied_Position;
        this.Phone = Phone;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getPosition_type() {
        return Position_Type;
    }

    public void setPosition_type(String Position_Type) {
        this.Position_Type = Position_Type;
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
    public String getApplied_position() {
        return Applied_Position;
    }

    public void setApplied_position(String Applied_Position) {
        this.Applied_Position = Applied_Position;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
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
    public New_Employee getNew_employee() {
        return new_employee;
    }

    public void setNew_employee(New_Employee new_employee) {
        this.new_employee = new_employee;
    }

}