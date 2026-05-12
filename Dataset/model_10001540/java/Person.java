





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String Address;
    private String Gender;
    private int Phone;
    private int PersonHospitalId;
    private String BirthDate;
    private String FirstName;
    private int PersonPatientId;
    private String Title;
    private String LastName;
    private String MiddleName;



    public Person(
        String Address,        String Gender,        int Phone,        int PersonHospitalId,        String BirthDate,        String FirstName,        int PersonPatientId,        String Title,        String LastName,        String MiddleName    ) {
        this.Address = Address;
        this.Gender = Gender;
        this.Phone = Phone;
        this.PersonHospitalId = PersonHospitalId;
        this.BirthDate = BirthDate;
        this.FirstName = FirstName;
        this.PersonPatientId = PersonPatientId;
        this.Title = Title;
        this.LastName = LastName;
        this.MiddleName = MiddleName;
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
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public int getPersonhospitalid() {
        return PersonHospitalId;
    }

    public void setPersonhospitalid(int PersonHospitalId) {
        this.PersonHospitalId = PersonHospitalId;
    }
    public String getBirthdate() {
        return BirthDate;
    }

    public void setBirthdate(String BirthDate) {
        this.BirthDate = BirthDate;
    }
    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public int getPersonpatientid() {
        return PersonPatientId;
    }

    public void setPersonpatientid(int PersonPatientId) {
        this.PersonPatientId = PersonPatientId;
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
    public String getMiddlename() {
        return MiddleName;
    }

    public void setMiddlename(String MiddleName) {
        this.MiddleName = MiddleName;
    }


}