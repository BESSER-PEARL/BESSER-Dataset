




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class reservationsystem_Person  {

    private String phone;
    private String email;
    private int id;
    private String name;
    private String middleName;
    private String FamilyName;
    private String addr;
    private String citizenship;
    private String passportId;
    private String residence;
    private LocalDate birthDate;
    private int gender;



    public reservationsystem_Person(
        String phone,        String email,        int id,        String name,        String middleName,        String FamilyName,        String addr,        String citizenship,        String passportId,        String residence,        LocalDate birthDate,        int gender    ) {
        this.phone = phone;
        this.email = email;
        this.id = id;
        this.name = name;
        this.middleName = middleName;
        this.FamilyName = FamilyName;
        this.addr = addr;
        this.citizenship = citizenship;
        this.passportId = passportId;
        this.residence = residence;
        this.birthDate = birthDate;
        this.gender = gender;
    }


    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMiddlename() {
        return middleName;
    }

    public void setMiddlename(String middleName) {
        this.middleName = middleName;
    }
    public String getFamilyname() {
        return FamilyName;
    }

    public void setFamilyname(String FamilyName) {
        this.FamilyName = FamilyName;
    }
    public String getAddr() {
        return addr;
    }

    public void setAddr(String addr) {
        this.addr = addr;
    }
    public String getCitizenship() {
        return citizenship;
    }

    public void setCitizenship(String citizenship) {
        this.citizenship = citizenship;
    }
    public String getPassportid() {
        return passportId;
    }

    public void setPassportid(String passportId) {
        this.passportId = passportId;
    }
    public String getResidence() {
        return residence;
    }

    public void setResidence(String residence) {
        this.residence = residence;
    }
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
    public int getGender() {
        return gender;
    }

    public void setGender(int gender) {
        this.gender = gender;
    }


}