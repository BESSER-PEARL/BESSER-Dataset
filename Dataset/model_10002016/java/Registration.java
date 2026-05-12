





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String Date;
    private String Skills___Requirement;
    private String Phone;
    private String Position_Type;
    private String Email;
    private String Applied_Position;
    private String Address;
    private String Name;





    private Admin admin;


    public Registration(
        String Date,        String Skills___Requirement,        String Phone,        String Position_Type,        String Email,        String Applied_Position,        String Address,        String Name    ) {
        this.Date = Date;
        this.Skills___Requirement = Skills___Requirement;
        this.Phone = Phone;
        this.Position_Type = Position_Type;
        this.Email = Email;
        this.Applied_Position = Applied_Position;
        this.Address = Address;
        this.Name = Name;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getSkills___requirement() {
        return Skills___Requirement;
    }

    public void setSkills___requirement(String Skills___Requirement) {
        this.Skills___Requirement = Skills___Requirement;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getPosition_type() {
        return Position_Type;
    }

    public void setPosition_type(String Position_Type) {
        this.Position_Type = Position_Type;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getApplied_position() {
        return Applied_Position;
    }

    public void setApplied_position(String Applied_Position) {
        this.Applied_Position = Applied_Position;
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

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}