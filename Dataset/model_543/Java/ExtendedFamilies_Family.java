





import java.util.List;
import java.util.ArrayList;

public class ExtendedFamilies_Family  {

    private int noOfChildren;
    private String lastName;



    public ExtendedFamilies_Family(
        int noOfChildren,        String lastName    ) {
        this.noOfChildren = noOfChildren;
        this.lastName = lastName;
    }


    public int getNoofchildren() {
        return noOfChildren;
    }

    public void setNoofchildren(int noOfChildren) {
        this.noOfChildren = noOfChildren;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }


}