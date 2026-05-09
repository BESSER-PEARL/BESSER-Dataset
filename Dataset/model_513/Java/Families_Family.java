





import java.util.List;
import java.util.ArrayList;

public class Families_Family  {

    private String address;
    private String lastName;





    private Families_FamilyRegistry families_familyregistry;


    public Families_Family(
        String address,        String lastName    ) {
        this.address = address;
        this.lastName = lastName;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public Families_FamilyRegistry getFamilies_familyregistry() {
        return families_familyregistry;
    }

    public void setFamilies_familyregistry(Families_FamilyRegistry families_familyregistry) {
        this.families_familyregistry = families_familyregistry;
    }

}