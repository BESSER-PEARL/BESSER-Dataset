





import java.util.List;
import java.util.ArrayList;

public class Household_Family  {

    private String lastName;





    private Household_HouseholdRoot household_householdroot;


    public Household_Family(
        String lastName    ) {
        this.lastName = lastName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public Household_HouseholdRoot getHousehold_householdroot() {
        return household_householdroot;
    }

    public void setHousehold_householdroot(Household_HouseholdRoot household_householdroot) {
        this.household_householdroot = household_householdroot;
    }

}