





import java.util.List;
import java.util.ArrayList;

public class UML_14_ElementOwnership  {

    private boolean isSpecification;
    private String visibility;



    public UML_14_ElementOwnership(
        boolean isSpecification,        String visibility    ) {
        this.isSpecification = isSpecification;
        this.visibility = visibility;
    }


    public boolean getIsspecification() {
        return isSpecification;
    }

    public void setIsspecification(boolean isSpecification) {
        this.isSpecification = isSpecification;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}