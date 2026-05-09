





import java.util.List;
import java.util.ArrayList;

public class Families_Family  {

    private String address;
    private String lastName;





    private List<Families_Family> families_familys;




    private Families_FamilyRegistry families_familyregistry;


    public Families_Family(
        String address,        String lastName    ) {
        this.address = address;
        this.lastName = lastName;
        this.families_familys = new ArrayList<>();
    }

    public Families_Family(
        String address,        String lastName        ArrayList<Families_Family> families_familys    ) {
        this.address = address;
        this.lastName = lastName;
        this.families_familys = families_familys;
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

    public List<Families_Family> getFamilies_familys() {
        return families_familys;
    }

    public void addFamilies_family(Families_family families_family) {
        this.families_familys.add(families_family);
    }
    public Families_FamilyRegistry getFamilies_familyregistry() {
        return families_familyregistry;
    }

    public void setFamilies_familyregistry(Families_FamilyRegistry families_familyregistry) {
        this.families_familyregistry = families_familyregistry;
    }

}