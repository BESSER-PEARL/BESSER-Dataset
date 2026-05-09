





import java.util.List;
import java.util.ArrayList;

public class ExtendedFamilies_Family  {

    private boolean isSingleParent;
    private String lastName;
    private int noOfChildren;



    public ExtendedFamilies_Family(
        boolean isSingleParent,        String lastName,        int noOfChildren    ) {
        this.isSingleParent = isSingleParent;
        this.lastName = lastName;
        this.noOfChildren = noOfChildren;
    }


    public boolean getIssingleparent() {
        return isSingleParent;
    }

    public void setIssingleparent(boolean isSingleParent) {
        this.isSingleParent = isSingleParent;
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


}