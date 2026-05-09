





import java.util.List;
import java.util.ArrayList;

public class families_Member  {

    private String firstName;





    private families_Family families_family;




    private families_City families_city;


    public families_Member(
        String firstName    ) {
        this.firstName = firstName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public families_Family getFamilies_family() {
        return families_family;
    }

    public void setFamilies_family(families_Family families_family) {
        this.families_family = families_family;
    }
    public families_City getFamilies_city() {
        return families_city;
    }

    public void setFamilies_city(families_City families_city) {
        this.families_city = families_city;
    }

}