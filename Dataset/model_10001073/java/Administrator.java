





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String Company;
    private String Address;
    private String Name;





    private Employer employer;


    public Administrator(
        String Company,        String Address,        String Name    ) {
        this.Company = Company;
        this.Address = Address;
        this.Name = Name;
    }


    public String getCompany() {
        return Company;
    }

    public void setCompany(String Company) {
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

    public Employer getEmployer() {
        return employer;
    }

    public void setEmployer(Employer employer) {
        this.employer = employer;
    }

}