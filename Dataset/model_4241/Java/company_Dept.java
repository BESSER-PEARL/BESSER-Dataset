





import java.util.List;
import java.util.ArrayList;

public class company_Dept extends Subunit {

    private String name;





    private company_Company company_company;




    private List<company_Subunit> company_subunits;


    public company_Dept(
        String name    ) {
        super(
        );
        this.name = name;
        this.company_subunits = new ArrayList<>();
    }

    public company_Dept(
        String name        ArrayList<company_Subunit> company_subunits    ) {
        this.name = name;
        this.company_subunits = company_subunits;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }
    public List<company_Subunit> getCompany_subunits() {
        return company_subunits;
    }

    public void addCompany_subunit(Company_subunit company_subunit) {
        this.company_subunits.add(company_subunit);
    }

}