





import java.util.List;
import java.util.ArrayList;

public class Company_Person  {

    private String fullName;





    private Company_Unit company_unit;


    public Company_Person(
        String fullName    ) {
        this.fullName = fullName;
    }


    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }

    public Company_Unit getCompany_unit() {
        return company_unit;
    }

    public void setCompany_unit(Company_Unit company_unit) {
        this.company_unit = company_unit;
    }

}