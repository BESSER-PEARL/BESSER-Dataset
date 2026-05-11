





import java.util.List;
import java.util.ArrayList;

public class person_PersonType  {

    private String age;
    private String name;
    private String email;
    private String country;





    private person_CompanyType person_companytype;


    public person_PersonType(
        String age,        String name,        String email,        String country    ) {
        this.age = age;
        this.name = name;
        this.email = email;
        this.country = country;
    }


    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public person_CompanyType getPerson_companytype() {
        return person_companytype;
    }

    public void setPerson_companytype(person_CompanyType person_companytype) {
        this.person_companytype = person_companytype;
    }

}