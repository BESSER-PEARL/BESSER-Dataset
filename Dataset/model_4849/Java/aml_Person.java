





import java.util.List;
import java.util.ArrayList;

public class aml_Person  {

    private String id;
    private String nickName;
    private String department;
    private String email;
    private String lastName;
    private String description;
    private String firstName;
    private String middleName;
    private String organization;





    private aml_AmlDocument aml_amldocument;


    public aml_Person(
        String id,        String nickName,        String department,        String email,        String lastName,        String description,        String firstName,        String middleName,        String organization    ) {
        this.id = id;
        this.nickName = nickName;
        this.department = department;
        this.email = email;
        this.lastName = lastName;
        this.description = description;
        this.firstName = firstName;
        this.middleName = middleName;
        this.organization = organization;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNickname() {
        return nickName;
    }

    public void setNickname(String nickName) {
        this.nickName = nickName;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getMiddlename() {
        return middleName;
    }

    public void setMiddlename(String middleName) {
        this.middleName = middleName;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }

    public aml_AmlDocument getAml_amldocument() {
        return aml_amldocument;
    }

    public void setAml_amldocument(aml_AmlDocument aml_amldocument) {
        this.aml_amldocument = aml_amldocument;
    }

}