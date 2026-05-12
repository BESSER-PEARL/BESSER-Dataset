





import java.util.List;
import java.util.ArrayList;

public class SWRC_Product  {

    private String name;





    private Organization organization;


    public SWRC_Product(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

}