





import java.util.List;
import java.util.ArrayList;

public class company_Department  {

    private String name;





    private List<company_Department> company_departments;




    private company_Company company_company;


    public company_Department(
        String name    ) {
        this.name = name;
        this.company_departments = new ArrayList<>();
    }

    public company_Department(
        String name        ArrayList<company_Department> company_departments    ) {
        this.name = name;
        this.company_departments = company_departments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<company_Department> getCompany_departments() {
        return company_departments;
    }

    public void addCompany_department(Company_department company_department) {
        this.company_departments.add(company_department);
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}