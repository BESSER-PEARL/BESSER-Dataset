





import java.util.List;
import java.util.ArrayList;

public class families_Family  {

    private String street;
    private String lastName;
    private String town;



    public families_Family(
        String street,        String lastName,        String town    ) {
        this.street = street;
        this.lastName = lastName;
        this.town = town;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getTown() {
        return town;
    }

    public void setTown(String town) {
        this.town = town;
    }


}