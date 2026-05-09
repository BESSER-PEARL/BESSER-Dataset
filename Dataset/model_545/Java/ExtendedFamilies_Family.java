





import java.util.List;
import java.util.ArrayList;

public class ExtendedFamilies_Family  {

    private String lastName;
    private int noOfChildren;
    private boolean singleParent;



    public ExtendedFamilies_Family(
        String lastName,        int noOfChildren,        boolean singleParent    ) {
        this.lastName = lastName;
        this.noOfChildren = noOfChildren;
        this.singleParent = singleParent;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public int getNoofchildren() {
        return noOfChildren;
    }

    public void setNoofchildren(int noOfChildren) {
        this.noOfChildren = noOfChildren;
    }
    public boolean getSingleparent() {
        return singleParent;
    }

    public void setSingleparent(boolean singleParent) {
        this.singleParent = singleParent;
    }


}