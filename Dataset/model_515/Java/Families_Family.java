





import java.util.List;
import java.util.ArrayList;

public class Families_Family extends uncertainty_ModelElement, uncertainty_aFamily {

    private String lastName;
    private String address;





    private Families_Family families_family;


    public Families_Family(
        String lastName,        String address    ) {
        super(
        );
        this.lastName = lastName;
        this.address = address;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public Families_Family getFamilies_family() {
        return families_family;
    }

    public void setFamilies_family(Families_Family families_family) {
        this.families_family = families_family;
    }

}