





import java.util.List;
import java.util.ArrayList;

public class company_Person extends NamedElement {

    private String fullName;
    private String firstName;
    private int age;





    private company_Department company_department;




    private company_Person company_person;


    public company_Person(
        String fullName,        String firstName,        int age    ) {
        super(
        );
        this.fullName = fullName;
        this.firstName = firstName;
        this.age = age;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public company_Department getCompany_department() {
        return company_department;
    }

    public void setCompany_department(company_Department company_department) {
        this.company_department = company_department;
    }
    public company_Person getCompany_person() {
        return company_person;
    }

    public void setCompany_person(company_Person company_person) {
        this.company_person = company_person;
    }

}