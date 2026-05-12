





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String middleName;
    private String gender;
    private String title;
    private String name;
    private String homeAddress;
    private String phone;
    private String familyName;
    private String birthDate;
    private String givenName;



    public Person(
        String middleName,        String gender,        String title,        String name,        String homeAddress,        String phone,        String familyName,        String birthDate,        String givenName    ) {
        this.middleName = middleName;
        this.gender = gender;
        this.title = title;
        this.name = name;
        this.homeAddress = homeAddress;
        this.phone = phone;
        this.familyName = familyName;
        this.birthDate = birthDate;
        this.givenName = givenName;
    }


    public String getMiddlename() {
        return middleName;
    }

    public void setMiddlename(String middleName) {
        this.middleName = middleName;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHomeaddress() {
        return homeAddress;
    }

    public void setHomeaddress(String homeAddress) {
        this.homeAddress = homeAddress;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getFamilyname() {
        return familyName;
    }

    public void setFamilyname(String familyName) {
        this.familyName = familyName;
    }
    public String getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(String birthDate) {
        this.birthDate = birthDate;
    }
    public String getGivenname() {
        return givenName;
    }

    public void setGivenname(String givenName) {
        this.givenName = givenName;
    }


}