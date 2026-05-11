





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_PersonName  {

    private String middleInitial;
    private String lastName;
    private String firstName;



    public org_aries_common_PersonName(
        String middleInitial,        String lastName,        String firstName    ) {
        this.middleInitial = middleInitial;
        this.lastName = lastName;
        this.firstName = firstName;
    }


    public String getMiddleinitial() {
        return middleInitial;
    }

    public void setMiddleinitial(String middleInitial) {
        this.middleInitial = middleInitial;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}