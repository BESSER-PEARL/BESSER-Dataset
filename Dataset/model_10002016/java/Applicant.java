





import java.util.List;
import java.util.ArrayList;

public class Applicant  {

    private String Applied_Position;
    private String Password;
    private String Date_of_Birth;
    private String Address;
    private String Phone;
    private String Email;
    private String First_Name;
    private String Last_Name;





    private Login login;




    private Registration registration;




    private Position position;




    private New_Employee new_employee;


    public Applicant(
        String Applied_Position,        String Password,        String Date_of_Birth,        String Address,        String Phone,        String Email,        String First_Name,        String Last_Name    ) {
        this.Applied_Position = Applied_Position;
        this.Password = Password;
        this.Date_of_Birth = Date_of_Birth;
        this.Address = Address;
        this.Phone = Phone;
        this.Email = Email;
        this.First_Name = First_Name;
        this.Last_Name = Last_Name;
    }


    public String getApplied_position() {
        return Applied_Position;
    }

    public void setApplied_position(String Applied_Position) {
        this.Applied_Position = Applied_Position;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getDate_of_birth() {
        return Date_of_Birth;
    }

    public void setDate_of_birth(String Date_of_Birth) {
        this.Date_of_Birth = Date_of_Birth;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getFirst_name() {
        return First_Name;
    }

    public void setFirst_name(String First_Name) {
        this.First_Name = First_Name;
    }
    public String getLast_name() {
        return Last_Name;
    }

    public void setLast_name(String Last_Name) {
        this.Last_Name = Last_Name;
    }

    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }
    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }
    public Position getPosition() {
        return position;
    }

    public void setPosition(Position position) {
        this.position = position;
    }
    public New_Employee getNew_employee() {
        return new_employee;
    }

    public void setNew_employee(New_Employee new_employee) {
        this.new_employee = new_employee;
    }

}