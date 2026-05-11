





import java.util.List;
import java.util.ArrayList;

public class company_Employee  {

    private String name;





    private company_Department company_department;




    private company_Company company_company;


    public company_Employee(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public company_Department getCompany_department() {
        return company_department;
    }

    public void setCompany_department(company_Department company_department) {
        this.company_department = company_department;
    }
    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}