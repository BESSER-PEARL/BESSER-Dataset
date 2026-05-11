





import java.util.List;
import java.util.ArrayList;

public class Families2Persons_MemberToPerson  {

    private String firstName;
    private String familyName;



    public Families2Persons_MemberToPerson(
        String firstName,        String familyName    ) {
        this.firstName = firstName;
        this.familyName = familyName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getFamilyname() {
        return familyName;
    }

    public void setFamilyname(String familyName) {
        this.familyName = familyName;
    }


}