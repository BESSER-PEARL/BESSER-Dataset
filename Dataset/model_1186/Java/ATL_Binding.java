





import java.util.List;
import java.util.ArrayList;

public class ATL_Binding extends LocatedElement {

    private String isAssignment;
    private String propertyName;



    public ATL_Binding(
        String isAssignment,        String propertyName    ) {
        super(
        );
        this.isAssignment = isAssignment;
        this.propertyName = propertyName;
    }


    public String getIsassignment() {
        return isAssignment;
    }

    public void setIsassignment(String isAssignment) {
        this.isAssignment = isAssignment;
    }
    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }


}