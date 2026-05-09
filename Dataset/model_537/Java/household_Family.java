





import java.util.List;
import java.util.ArrayList;

public class household_Family  {

    private String name;





    private household_HouseholdRoot household_householdroot;


    public household_Family(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public household_HouseholdRoot getHousehold_householdroot() {
        return household_householdroot;
    }

    public void setHousehold_householdroot(household_HouseholdRoot household_householdroot) {
        this.household_householdroot = household_householdroot;
    }

}