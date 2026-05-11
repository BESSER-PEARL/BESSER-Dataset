





import java.util.List;
import java.util.ArrayList;

public class company_Supplier extends Addressable {

    private boolean preferred;





    private company_Company company_company;


    public company_Supplier(
        boolean preferred    ) {
        super(
        );
        this.preferred = preferred;
    }


    public boolean getPreferred() {
        return preferred;
    }

    public void setPreferred(boolean preferred) {
        this.preferred = preferred;
    }

    public company_Company getCompany_company() {
        return company_company;
    }

    public void setCompany_company(company_Company company_company) {
        this.company_company = company_company;
    }

}