





import java.util.List;
import java.util.ArrayList;

public class company_Person  {

    private boolean isUnemployed;
    private String lastname;
    private String name;
    private int salary;
    private String gender;
    private int age;





    private company_Company company_company;




    private company_Company company_company;


    public company_Person(
        boolean isUnemployed,        String lastname,        String name,        int salary,        String gender,        int age    ) {
        this.isUnemployed = isUnemployed;
        this.lastname = lastname;
        this.name = name;
        this.salary = salary;
        this.gender = gender;
        this.age = age;
    }


    public boolean getIsunemployed() {
        return isUnemployed;
    }

    public void setIsunemployed(boolean isUnemployed) {
        this.isUnemployed = isUnemployed;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}