





import java.util.List;
import java.util.ArrayList;

public class UML_14_ElementOwnership  {

    private String visibility;
    private boolean isSpecification;



    public UML_14_ElementOwnership(
        String visibility,        boolean isSpecification    ) {
        this.visibility = visibility;
        this.isSpecification = isSpecification;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getIsspecification() {
        return isSpecification;
    }

    public void setIsspecification(boolean isSpecification) {
        this.isSpecification = isSpecification;
    }


}