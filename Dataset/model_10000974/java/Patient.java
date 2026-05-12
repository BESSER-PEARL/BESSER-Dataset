





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String PhoneNumber;
    private String City;
    private String DateOfBirth;
    private String PId;
    private String IsPhoneNumberConfirmed;
    private String FirstName;
    private String activationcode;
    private String State;
    private String Email;
    private String ZipCode;
    private String IsEmailConfirmed;
    private String LastName;
    private int UserId;
    private int PatientId;
    private String StreetAddress;



    public Patient(
        String PhoneNumber,        String City,        String DateOfBirth,        String PId,        String IsPhoneNumberConfirmed,        String FirstName,        String activationcode,        String State,        String Email,        String ZipCode,        String IsEmailConfirmed,        String LastName,        int UserId,        int PatientId,        String StreetAddress    ) {
        this.PhoneNumber = PhoneNumber;
        this.City = City;
        this.DateOfBirth = DateOfBirth;
        this.PId = PId;
        this.IsPhoneNumberConfirmed = IsPhoneNumberConfirmed;
        this.FirstName = FirstName;
        this.activationcode = activationcode;
        this.State = State;
        this.Email = Email;
        this.ZipCode = ZipCode;
        this.IsEmailConfirmed = IsEmailConfirmed;
        this.LastName = LastName;
        this.UserId = UserId;
        this.PatientId = PatientId;
        this.StreetAddress = StreetAddress;
    }


    public String getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(String PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public String getDateofbirth() {
        return DateOfBirth;
    }

    public void setDateofbirth(String DateOfBirth) {
        this.DateOfBirth = DateOfBirth;
    }
    public String getPid() {
        return PId;
    }

    public void setPid(String PId) {
        this.PId = PId;
    }
    public String getIsphonenumberconfirmed() {
        return IsPhoneNumberConfirmed;
    }

    public void setIsphonenumberconfirmed(String IsPhoneNumberConfirmed) {
        this.IsPhoneNumberConfirmed = IsPhoneNumberConfirmed;
    }
    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public String getActivationcode() {
        return activationcode;
    }

    public void setActivationcode(String activationcode) {
        this.activationcode = activationcode;
    }
    public String getState() {
        return State;
    }

    public void setState(String State) {
        this.State = State;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getZipcode() {
        return ZipCode;
    }

    public void setZipcode(String ZipCode) {
        this.ZipCode = ZipCode;
    }
    public String getIsemailconfirmed() {
        return IsEmailConfirmed;
    }

    public void setIsemailconfirmed(String IsEmailConfirmed) {
        this.IsEmailConfirmed = IsEmailConfirmed;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }
    public int getUserid() {
        return UserId;
    }

    public void setUserid(int UserId) {
        this.UserId = UserId;
    }
    public int getPatientid() {
        return PatientId;
    }

    public void setPatientid(int PatientId) {
        this.PatientId = PatientId;
    }
    public String getStreetaddress() {
        return StreetAddress;
    }

    public void setStreetaddress(String StreetAddress) {
        this.StreetAddress = StreetAddress;
    }


}