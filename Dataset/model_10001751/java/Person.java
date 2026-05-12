





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String BirthDate;
    private int PersonHospitalId;
    private String Address;
    private String Gender;
    private int PersonPatientId;
    private String FirstName;
    private int Phone;
    private String MiddleName;
    private String Title;
    private String LastName;



    public Person(
        String BirthDate,        int PersonHospitalId,        String Address,        String Gender,        int PersonPatientId,        String FirstName,        int Phone,        String MiddleName,        String Title,        String LastName    ) {
        this.BirthDate = BirthDate;
        this.PersonHospitalId = PersonHospitalId;
        this.Address = Address;
        this.Gender = Gender;
        this.PersonPatientId = PersonPatientId;
        this.FirstName = FirstName;
        this.Phone = Phone;
        this.MiddleName = MiddleName;
        this.Title = Title;
        this.LastName = LastName;
    }


    public String getBirthdate() {
        return BirthDate;
    }

    public void setBirthdate(String BirthDate) {
        this.BirthDate = BirthDate;
    }
    public int getPersonhospitalid() {
        return PersonHospitalId;
    }

    public void setPersonhospitalid(int PersonHospitalId) {
        this.PersonHospitalId = PersonHospitalId;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public int getPersonpatientid() {
        return PersonPatientId;
    }

    public void setPersonpatientid(int PersonPatientId) {
        this.PersonPatientId = PersonPatientId;
    }
    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getMiddlename() {
        return MiddleName;
    }

    public void setMiddlename(String MiddleName) {
        this.MiddleName = MiddleName;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }


}