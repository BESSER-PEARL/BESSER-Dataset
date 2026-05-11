





import java.util.List;
import java.util.ArrayList;

public class CompanyLanguage_Company  {

    private String name;





    private List<CompanyLanguage_Admin> companylanguage_admins;




    private List<CompanyLanguage_Employee> companylanguage_employees;




    private List<CompanyLanguage_CEO> companylanguage_ceos;


    public CompanyLanguage_Company(
        String name    ) {
        this.name = name;
        this.companylanguage_admins = new ArrayList<>();
        this.companylanguage_employees = new ArrayList<>();
        this.companylanguage_ceos = new ArrayList<>();
    }

    public CompanyLanguage_Company(
        String name        ArrayList<CompanyLanguage_Admin> companylanguage_admins,        ArrayList<CompanyLanguage_Employee> companylanguage_employees,        ArrayList<CompanyLanguage_CEO> companylanguage_ceos    ) {
        this.name = name;
        this.companylanguage_admins = companylanguage_admins;
        this.companylanguage_employees = companylanguage_employees;
        this.companylanguage_ceos = companylanguage_ceos;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<CompanyLanguage_Admin> getCompanylanguage_admins() {
        return companylanguage_admins;
    }

    public void addCompanylanguage_admin(Companylanguage_admin companylanguage_admin) {
        this.companylanguage_admins.add(companylanguage_admin);
    }
    public List<CompanyLanguage_Employee> getCompanylanguage_employees() {
        return companylanguage_employees;
    }

    public void addCompanylanguage_employee(Companylanguage_employee companylanguage_employee) {
        this.companylanguage_employees.add(companylanguage_employee);
    }
    public List<CompanyLanguage_CEO> getCompanylanguage_ceos() {
        return companylanguage_ceos;
    }

    public void addCompanylanguage_ceo(Companylanguage_ceo companylanguage_ceo) {
        this.companylanguage_ceos.add(companylanguage_ceo);
    }

}