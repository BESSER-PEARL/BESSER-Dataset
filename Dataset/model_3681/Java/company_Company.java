





import java.util.List;
import java.util.ArrayList;

public class company_Company  {

    private String name;





    private List<company_Department> company_departments;


    public company_Company(
        String name    ) {
        this.name = name;
        this.company_departments = new ArrayList<>();
    }

    public company_Company(
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

}