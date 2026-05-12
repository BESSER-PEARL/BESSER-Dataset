





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String Name;
    private String Company;
    private String Address;





    private Employer employer;


    public Administrator(
        String Name,        String Company,        String Address    ) {
        this.Name = Name;
        this.Company = Company;
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
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Employer getEmployer() {
        return employer;
    }

    public void setEmployer(Employer employer) {
        this.employer = employer;
    }

}