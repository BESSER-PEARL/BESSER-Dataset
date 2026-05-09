





import java.util.List;
import java.util.ArrayList;

public class families_Family  {

    private String lastName;





    private families_FamilyRegister families_familyregister;


    public families_Family(
        String lastName    ) {
        this.lastName = lastName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public families_FamilyRegister getFamilies_familyregister() {
        return families_familyregister;
    }

    public void setFamilies_familyregister(families_FamilyRegister families_familyregister) {
        this.families_familyregister = families_familyregister;
    }

}