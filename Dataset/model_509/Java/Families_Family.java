





import java.util.List;
import java.util.ArrayList;

public class Families_Family  {

    private String lastName;
    private String address;





    private Families_Family families_family;




    private Families_FamilyRegistry families_familyregistry;


    public Families_Family(
        String lastName,        String address    ) {
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
    public Families_FamilyRegistry getFamilies_familyregistry() {
        return families_familyregistry;
    }

    public void setFamilies_familyregistry(Families_FamilyRegistry families_familyregistry) {
        this.families_familyregistry = families_familyregistry;
    }

}