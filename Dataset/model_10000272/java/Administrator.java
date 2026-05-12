





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String Address;
    private String Name;
    private String Company;





    private Employer employer;


    public Administrator(
        String Address,        String Name,        String Company    ) {
        this.Address = Address;
        this.Name = Name;
        this.Company = Company;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getCompany() {
        return Company;
    }

    public void setCompany(String Company) {
        this.Company = Company;
    }

    public Employer getEmployer() {
        return employer;
    }

    public void setEmployer(Employer employer) {
        this.employer = employer;
    }

}