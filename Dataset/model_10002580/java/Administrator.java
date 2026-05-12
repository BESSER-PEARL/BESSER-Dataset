





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String Name;
    private String Address;
    private String Company;





    private Employer employer;


    public Administrator(
        String Name,        String Address,        String Company    ) {
        this.Name = Name;
        this.Address = Address;
        this.Company = Company;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
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