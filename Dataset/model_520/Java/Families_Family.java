





import java.util.List;
import java.util.ArrayList;

public class Families_Family extends uncertainty_aFamily, uncertainty_ModelElement {

    private String lastName;
    private String address;



    public Families_Family(
        String lastName,        String address    ) {
        super(
        );
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


}