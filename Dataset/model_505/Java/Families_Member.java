





import java.util.List;
import java.util.ArrayList;

public class Families_Member  {

    private String firstName;





    private Families_City families_city;




    private Families_Family families_family;


    public Families_Member(
        String firstName    ) {
        this.firstName = firstName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public Families_City getFamilies_city() {
        return families_city;
    }

    public void setFamilies_city(Families_City families_city) {
        this.families_city = families_city;
    }
    public Families_Family getFamilies_family() {
        return families_family;
    }

    public void setFamilies_family(Families_Family families_family) {
        this.families_family = families_family;
    }

}