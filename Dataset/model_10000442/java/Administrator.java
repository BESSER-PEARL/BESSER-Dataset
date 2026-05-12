





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String Company;
    private String Name;
    private String Address;





    private Employer employer;


    public Administrator(
        String Company,        String Name,        String Address    ) {
        this.Company = Company;
        this.Name = Name;
        this.Address = Address;
    }


    public String getCompany() {
        return Company;
    }

    public void setCompany(String Company) {
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

    public Employer getEmployer() {
        return employer;
    }

    public void setEmployer(Employer employer) {
        this.employer = employer;
    }

}