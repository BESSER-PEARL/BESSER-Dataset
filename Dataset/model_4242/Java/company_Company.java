





import java.util.List;
import java.util.ArrayList;

public class company_Company  {






    private List<company_Dept> company_depts;


    public company_Company(
    ) {
        this.company_depts = new ArrayList<>();
    }

    public company_Company(
        ArrayList<company_Dept> company_depts    ) {
        this.company_depts = company_depts;
    }


    public List<company_Dept> getCompany_depts() {
        return company_depts;
    }

    public void addCompany_dept(Company_dept company_dept) {
        this.company_depts.add(company_dept);
    }

}