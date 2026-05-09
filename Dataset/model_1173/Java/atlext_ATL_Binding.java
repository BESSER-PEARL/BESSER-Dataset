





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_Binding extends LocatedElement {

    private String propertyName;
    private String isAssignment;



    public atlext_ATL_Binding(
        String propertyName,        String isAssignment    ) {
        super(
        );
        this.propertyName = propertyName;
        this.isAssignment = isAssignment;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }
    public String getIsassignment() {
        return isAssignment;
    }

    public void setIsassignment(String isAssignment) {
        this.isAssignment = isAssignment;
    }


}